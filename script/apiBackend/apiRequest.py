# 导入依赖
from msilib.schema import ODBCAttribute
import requests

# Get Orders
def getOrders():
    # 获取 gas
    response = requests.get('http://47.242.89.124:5000/api/v1/tokens?status=Created').json()
    # 返回结果
    return response

# 解析结果
def parseOrders(rawOrders):
    # 获取 Orders 内容
    orderList = rawOrders['data']['orders']
    # 返回结果
    return orderList

# 显示结果
ordersL = getOrders()
# 结果
orders = parseOrders(ordersL)
# 判断结果
print(orders)