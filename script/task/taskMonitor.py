# 解析数据并拆分为所有任务
def runAllTasks():
    # 任务列表
    transList = []
    # 测试循环
    for i in range (10):
        # 测试添加
        transList.append({'from': 'fm'+str(i), 'to': 'to'+str(i), 'token': 'tk'+str(i), 'amount': i, 'transGasFeeMax': 30, 'transGasLimitMax':350000})
    # 任务总表
    taskList = {}
    # 订单编号
    taskList['orderId'] = '10086'
    # 订单任务
    taskList['transaction'] = transList

    # 返回任务
    return taskList

# 显示结果
print(runAllTasks())