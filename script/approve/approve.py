# 导入依赖
import time
from web3 import Web3
from web3.providers import HTTPProvider
from multiprocessing import  Process
from approveConfig import *

# 发送交易
def sendTxn(w3, txn, priKey):
    # 账户
    signed_txn = w3.eth.account.signTransaction(txn, private_key=priKey)
    # 转十六进制
    res = w3.eth.sendRawTransaction(signed_txn.rawTransaction.hex())
    # 交易凭据
    txn_receipt = w3.eth.waitForTransactionReceipt(res)
    # 返回凭据
    return txn_receipt

# 授权
def approve(w3, contItem, pubKey, priKey, appAddr, appAmount, chainId, gasPrice, gasLimit):
    # 调用授权函数
    txn = contItem.functions.approve(appAddr, appAmount).buildTransaction( {
        'chainId': chainId,
        'gasPrice': w3.toWei(gasPrice,'gwei'),
        'nonce': w3.eth.getTransactionCount(pubKey),
        'gas': gasLimit
    })

    th = sendTxn(w3, txn, priKey)

# 主函数   
if __name__ == '__main__':
    # 构造 web3 实例
    w3 = Web3(HTTPProvider(endpointHttp))
    # 合约实例
    tokenItem = w3.eth.contract(address=tokenAddr, abi=tokenAbi)

    # 添加进程
    for i in range(len(pubKeyList)):
        # Arbitrum Bridge 跨链
        approve(w3, tokenItem, pubKeyList[i], priKeyList[i], approveAddr, approveAmount, chainId, gasPrice, gasLimit)
        # 等待
        time.sleep(5)