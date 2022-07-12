# 路径维护依赖
import sys
# 路径维护
sys.path.append('script/gasCal')
sys.path.append('script/apiBackend')
sys.path.append('script/trans')

# 获取依赖
import time
from gasTracker import *
from apiRequest import *
from taskConfig import *
from transWithGas import *
from transConfig import *
# from web3 import Web3
# from web3.providers import HTTPProvider
import threading

# 计算向上取整 
import math

# 任务类
class Tasks:
    # 参数初始化
    def __init__(self):
        # 线程锁
        self.lock = threading.RLock()
        # Low Gas
        self.gasLow = 0
        # Medium Gas
        self.gasMedium = 0
        # High Gas
        self.gasHigh = 0
        # Suggest Gas
        self.gasSuggest = 0
        # 当前任务列表
        self.taskList = []
        # 交易打包列表
        self.packinglist = []
        # 任务发出者字典集
        self.taskOwner = {}
        # 任务出发者的总交易数目
        self.taskCount = []
        # 任务出发者支付gas费
        self.gasfee = {}

    # 根据 Gas 分配任务: 从总的任务中提取到满足 Gas Fee 的任务到任务列表, 并设为 Pending 状态
    def taskAssignByGas(self):
        # 尝试
        flag = True
        while flag:
            # 等待延迟
            time.sleep(taskLoopDelay)
            # 加锁
            self.lock.acquire()
            # 尝试任务分配
            try:
                # 获取任务列表
                ordersL = getOrders()
                # 获取 Gas
                gasRes = getGasOracle()
                # 判断结果
                if gasRes is not None:
                    # 返回低中高
                    low, medium, high, suggest = getGasLevel(gasRes)
                    # 添加到类的状态
                    self.gasHigh = high
                    self.gasLow = low
                    self.gasMedium = medium
                    self.gasSuggest = suggest
                    # 显示结果
                    print('[成功提示] Gas Fee 获取成功: Low: {0}, Medium: {1}, High: {2}, Suggest: {3}'.format(low, medium, high, suggest))

                    # flag = False循环结束
                    flag = False
                    # 任务进行 Gas 区间判定
                    for i in range(len(ordersL)):
                        # 判断订单状态'tran_gas_fee_max'是否为空
                        if ordersL[i]["trans_gas_fee_max"] == None:
                            if (len(ordersL[i]["transactions"]) > 0):
                                # 添加到任务列表
                                print("订单"+str(i)+"进入任务列表！")
                                self.taskList.append(ordersL[i])
                                # 设置 transactions status
                                print("订单"+str(i)+"状态修改为pending")
                                self.taskList[-1]["order_exec_status"] = "pending"
                        if ordersL[i]["trans_gas_fee_max"] != None:
                            # gas fee 判断
                            if float(ordersL[i]["trans_gas_fee_max"]) >= suggest:
                                # 逐个判断
                                if (len(ordersL[i]["transactions"]) > 0):
                                    # 添加到任务列表
                                    print("订单"+str(i)+"进入任务列表！")
                                    self.taskList.append(ordersL[i])
                                    # 设置 transactions status
                                    print("订单"+str(i)+"状态修改为pending")
                                    self.taskList[-1]["order_exec_status"] = "pending"


                    # 显示错误
                else:
                    # gas 未获取成功
                    print('[错误提示] Gas Fee 获取失败')
                    # 继续循环获取gas
                    flag = True

            # 解锁
            finally:
            # 释放锁
                self.lock.release()
        
    # 任务列表地址数统计
    def taskCount(self):
        # 加锁
        self.lock.acquire()
        # 尝试
        try:
            # 地址数目统计
            for i in range(len(self.taskList)):
                # 地址统计
                self.taskCount[self.taskList[i]['order_create_addr']] += len(self.taskList[i]['transactions'])
        # 解锁
        finally:
            # 释放锁
            self.lock.release()
    
    # 将获得的列表打成包,每N个交易打成一个包,将数据构建成交易所需的形式
    def taskpacking(self, N=5):
        if N < 0:
            print("N can't be negative")
            exit()
        # 将各任务的交易都放进去，同时每个交易包含"order_create_addr"
        # 加锁
        self.lock.acquire()
        #尝试
        try:
            print("-----------------------------\n将交易分配成包")
            transactions = []
            for order in self.taskList:
                if order != None: 
                    for transaction in order["transactions"]:
                        # 交易信息中加入"order_create_addr"
                        transaction["order_create_addr"] = order["order_create_addr"]
                        transactions.append(transaction)

            #print("展示 transactions")
            #print(transactions)
            transaction_num = len(transactions)
            pack_num = math.ceil(transaction_num/N)

            for i in range(pack_num):
                # 检查这是是否是最后一个包
                if i < pack_num-1:
                    print("打包: 第"+str(i+1)+"个包")
                    self.packinglist.append(transactions[i*N : (i+1)*N])
                # 检查这是是否是最后一个包
                if i == pack_num-1:
                    print("打包: 第"+str(i+1)+"个包")
                    self.packinglist.append(transactions[i*N: ])

            print("展示 packinglist")
            print(self.packinglist)
            print("------------------------------")
            # 释放锁

        # 解锁
        finally:
            # 释放锁
            self.lock.release()  
          

    # 无充值转账任务: 将需要完成的任务按照任务比例分配 Gas，并且完成转账 
    def inputTrans(self):
        print("----------------------------\n将打包的交易形成合约并发送")
        # 循环获取 Gas
        flag = True
        while flag:
            # 等待延迟
            time.sleep(taskLoopDelay)
            # 加锁
            self.lock.acquire()
            # 尝试任务分配
            try:
                # 构造 web3 实例
                w3 = Web3(HTTPProvider(taskEndpointHttp))
                # 合约实例
                contractItem = w3.eth.contract(address=taskContAddr, abi=taskContAbi)
                # 逐个订单打包
                for i in range(len(self.packinglist)):
                    # 计算交易所需的信息
                    inputTokenArg = [x['token_contract'] for x in self.packinglist[i] ]
                    inputFromArg = [x['from_addr'] for x in self.packinglist[i] ]
                    inputToArg = [x['to_addr'] for x in self.packinglist[i] ]
                    ercItem = w3.eth.contract(address=inputTokenArg[0],abi=erc20Abi)
                    decimal = 'ether' if  ercItem.functions.decimals().call() ==18 else  'mwei'
                   
                    inputAmountArg = [w3.toWei(x['token_amount'],decimal) for x in self.packinglist[i] ]
            
                    print("展示 inputAmountArg")
                    print((inputAmountArg))
                    # 计算 Gas
          
                    gasLimit = getGasLimit(w3, contractItem, taskFuncName,[inputTokenArg, inputFromArg, inputToArg, inputAmountArg], 0, taskFromAddr, taskContAddr)
                    # 调用结果
                    print(gasLimit)
                    exit()
                    transBasic(w3, contractItem, taskFuncName, inputTokenArg, inputFromArg, inputToArg, inputAmountArg, taskChainId, gasPrice, gasLimit)
                    # 根据调用结果计算各用户承担的 gas 费
                    # 如何计算
                    # flag = False 打包的交易构成智能合约已经完成并且上传到链上
                    flag = False
            # 解锁
            finally:
                # 释放锁
                self.lock.release()
    
    # 清空任务列表 任务字典
    def cleanTask(self):
        # 加锁
        self.lock.acquire()
        # 尝试
        try:
            # 清空任务列表
            self.taskList = []
            # 清空任务字典
            self.taskOwner = {}
            # 清空交易包裹
            self.packinglist = []
            
        # 解锁
        finally:
            # 释放锁
            self.lock.release()
        

# 主函数
if __name__ == '__main__':
    # 任务
    task = Tasks()
    # 循环
    while True:
        # 循环任务分配
        task.taskAssignByGas()
        task.taskpacking()
        task.inputTrans()
        task.cleanTask()
        # 等待
        time.sleep(2)


# 1. A: 3, B: 5, C: 10
#    => (A: 3, B: 2), (B: 3, C: 2), (C: 5), (C: 3)

# 2. A: 3, B: 5, C: 10
#    >= 5 => 打包
#    => (B: 5), (C: 10), (A: 3)

# 3. A => B: (B1, B2, B3, ...)
#    => A => B1: 3, B2: 8, B3: 10, B4: 5, B5: 7

# 防止 A 调用 B 账户
# 1. 签名
#    B 的所有账户 B1 - Bn 只对 B 生效
# 2. 私钥单次认证
#    B 的所有账户 B1 - Bn 私钥导入一次 => 仅在前端做验证, 后端接受验证结果, 不保留私钥 => 存入数据库