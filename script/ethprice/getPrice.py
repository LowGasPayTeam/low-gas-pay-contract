# 导入依赖
import requests
from priceConfig import *

# Get ETH Price
def getETHPrice():
    # 获取 gas
    response = requests.get(getETHPricePath + apiKey).json()
    # 判断状态
    if response['status'] == '1' and response['message'] == 'OK':
        # 返回结果
        return response['result']
    # 状态错误
    else:
        # 错误
        return None

# 获取低, 中, 高, 及建议 gas
def parseETHPrice(ethResult):
    # 返回结果
    return float(ethResult['ethusd'])

# 显示结果
ethPrice = getETHPrice()
# 判断结果
if ethPrice is not None:
    # 显示结果
    print('[成功提示] ETH Price 获取成功: {0}'.format(parseETHPrice(ethPrice)))
# 显示错误
else:
    # gas 未获取成功
    print('[错误提示] ETH Price 获取失败')