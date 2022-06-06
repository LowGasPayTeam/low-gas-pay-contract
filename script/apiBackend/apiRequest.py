# 导入依赖
import requests

# Get Orders
def getOrders():
    # 获取 gas
    response = requests.get('http://47.242.89.124:5000/api/v1/tokens?page=1&size=10&address=0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710').json()
    # 返回结果
    return response

# 显示结果
orders = getOrders()
# 判断结果
print(orders)