# 导入依赖
from web3 import Web3
from web3.providers import HTTPProvider
from config import *

# 对指定的函数, 及指定的输入参数, 估计 Gas Limit
def getGasEstimate(w3, contractAddr, fromAddress, data):
    # 获取 Gas Limit
    gasLimit = w3.eth.estimateGas(
        {
            'to': contractAddr, 
            'from': fromAddress, 
            'data': data
        }
    )
    # 返回 Gas Limit
    return gasLimit

# 某一用户(fromAddress) 调用某个合约(contractAddress)
# 使用其 ABI (contractAbi) 选择其中某个函数(functionName)
# 输入指定的参数(arguments)
def getGasLimit(w3, fromAddress, contractAddress, contractAbi, functionName, arguments):
    # to 合约地址
    contractAddr = Web3.toChecksumAddress(contractAddress)
    # from 发起者地址
    fromAddr  = Web3.toChecksumAddress(fromAddress)
    # 合约实例
    contractItem = w3.eth.contract(address=contractAddr, abi=contractAbi)
    # 参数编码
    encodeData = contractItem.encodeABI(fn_name=functionName, args=arguments)
    # 获取 Gas
    gasLimit = getGasEstimate(w3, contractAddr, fromAddr, encodeData)
    # 返回结果
    return gasLimit


# 构造 web3 实例
w3 = Web3(HTTPProvider(endpointHttp))
# 获取 Gas Limit
gasLimit = getGasLimit(w3, fromAddr, contAddr, contAbi, funcName, argu)
# 显示 Gas
print('[成功提示] Gas Limit: {0}'.format(gasLimit))