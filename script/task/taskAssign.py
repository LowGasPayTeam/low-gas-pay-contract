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
from web3 import Web3
from web3.providers import HTTPProvider
import threading

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
        # 任务发出者字典集
        self.taskOwner = {}

    # 根据 Gas 分配任务: 从总的任务中提取到满足 Gas Fee 的任务到任务列表, 并设为 Pending 状态
    def taskAssignByGas(self):
        # 循环获取 Gas
        while True:
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
                    # 显示结果
                    print('[成功提示] Gas Fee 获取成功: Low: {0}, Medium: {1}, High: {2}, Suggest: {3}'.format(low, medium, high, suggest))
                # 显示错误
                else:
                    # gas 未获取成功
                    print('[错误提示] Gas Fee 获取失败')
                # 对每个任务进行 Gas 区间判定
                for i in range(len(ordersL)):
                    # gas fee 判断
                    if float(ordersL[i]['trans_gas_fee_max']) <= suggest:
                        # 逐个判断
                        if (len(ordersL[i]['transactions']) > 0):
                            # 添加到任务列表
                            self.taskList.append(ordersL[i])
                            # 设置 transactions status
                            # 
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
    
    # 无充值转账任务: 将需要完成的任务按照任务比例分配 Gas
    def inputTrans(self):
        # 循环获取 Gas
        while True:
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
                for i in range(len(self.taskList)):
                    # 计算 Gas
                    gasLimit = getGasLimit(w3, contractItem, taskFuncName, [inputTokenArg, inputFromArg, inputToArg, inputAmountArg], 0, taskFromAddr, taskContAddr)
                    # 调用结果
                    transBasic(w3, contractItem, taskFuncName, inputTokenArg, inputFromArg, inputToArg, inputAmountArg, taskChainId, gasPrice, gasLimit)
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
        # 解锁
        finally:
            # 释放锁
            self.lock.release()
        

# 主函数
if __name__ == '__main__':
    # 任务
    task = Tasks()
    # 循环任务分配
    task.taskAssignByGas()