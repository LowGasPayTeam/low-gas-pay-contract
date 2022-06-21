# 导入依赖
import requests

# Get Orders
def getOrders():
    # 获取 gas
    response = requests.get('https://lowgaspay.com/api/v1/tokens?status=Created').json()
    # 返回结果
    return response['data']['orders']

# 显示结果
ordersL = getOrders()
# 判断结果s
print(ordersL)