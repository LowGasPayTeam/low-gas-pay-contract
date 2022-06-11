# 路径维护依赖
import sys
# 路径维护
sys.path.append('script/gasCal')
sys.path.append('script/apiBackend')

# 获取依赖
import time
from gasTracker import *
from apiRequest import *

# 任务类
class Tasks:
    # 参数初始化
    def __init__(self):
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

    # 根据 Gas 分配任务
    def taskAssignByGas(self):
        # 循环获取 Gas
        while True:
            # 等待延迟
            time.sleep(5)
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
                # 逐个判断
                if (len(ordersL['transactions']) > 0):
                    # 跳过
                    pass

# 主函数
if __name__ == '__main__':
    # 任务
    task = Tasks()
    # 循环任务分配
    task.taskAssignByGas()