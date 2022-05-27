# 导入依赖
from web3 import Web3
from web3.providers import HTTPProvider
from transConfig import *

# 地址转换
def addrChecksum(addrList):
    # 列表
    addrChecksumList = []
    # 循环
    for i in addrList:
        # 转化
        addrChecksumList.append(Web3.toChecksumAddress(i))
    # 返回结果
    return addrChecksumList

# 发送交易
def send_txn(w3, txn):
    # 账户
    signed_txn = w3.eth.account.signTransaction(txn, private_key=priKey)
    # 转十六进制
    res = w3.eth.sendRawTransaction(signed_txn.rawTransaction.hex())
    # 交易凭据
    txn_receipt = w3.eth.waitForTransactionReceipt(res)
    # 返回凭据
    return txn_receipt

# 基础转账功能
def transBasic(w3, contItem, tokenAddressL, fromAddressL, toAddressL, amountL, chainId, gasPrice, gasLimit, nonce, value):
    # 地址转换
    tokenAddrList = addrChecksum(tokenAddressL)
    # 地址转换
    fromAddrList = addrChecksum(fromAddressL)
    # 地址转换
    toAddrList = addrChecksum(toAddressL)
    # 转账
    txn = contItem.functions.transMultiToken(tokenAddrList, fromAddrList, toAddrList, amountL).buildTransaction( {
        'chainId': chainId,
        'gasPrice': Web3.toWei(gasPrice, "gwei"),
        'gas': gasLimit,
        'nonce': w3.eth.getTransactionCount(pubKey),
        'value': Web3.toWei(value, 'ether')
    })
    # 发送请求
    res = send_txn(w3, txn)
    # 显示结果
    print('[普通提示] 函数调用结果: {0}'.format(res))

# 主函数   
if __name__ == '__main__':
    # 构造 web3 实例
    w3 = Web3(HTTPProvider(endpointHttp))
    # 合约实例
    contractItem = w3.eth.contract(address=contAddr, abi=contAbi)
    # 调用结果
    transBasic(w3, contractItem, tokenArg, fromArg, toArg, amountArg, chainId, gasPrice, gasLimit, nonce, value)