# 导入依赖
import requests
from config import *

# Get Gas Oracle
def getGasOracle():
    # 获取 gas
    response = requests.get(gasOraclePath + apiKey).json()
    # 判断状态
    if response['status'] == '1' and response['message'] == 'OK':
        # 返回结果
        return response['result']
    # 状态错误
    else:
        # 错误
        return None

# 获取低, 中, 高, 及建议 gas
def getGasLevel(gasResult):
    # 返回结果
    return float(gasResult['SafeGasPrice']), float(gasResult['ProposeGasPrice']), float(gasResult['FastGasPrice']), float(gasResult['suggestBaseFee'])


# 显示结果
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