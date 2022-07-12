# 导入依赖
from traceback import print_tb
from matplotlib.font_manager import json_load
from web3 import Web3
from web3.providers import HTTPProvider
from transConfig_NFT import *
from collections import Counter
import requests
import json
import copy
# 构造 web3 实例
w3 = Web3(HTTPProvider(endpointHttp))
contractItem = w3.eth.contract(address=MultNFTaddr, abi=contAbi)

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

# 基础转账功能
def transBasic(w3, tokenAddressL, fromAddressL, toAddressL, amountL, functionName, arguments):
    # 地址转换
    tokenAddrList = addrChecksum(tokenAddressL)
    # 地址转换
    fromAddrList = addrChecksum(fromAddressL)
    # 地址转换
    toAddrList = addrChecksum(toAddressL)
    # 转账
    


     

def send_txn(txn):
        # 账户
        signed_txn = w3.eth.account.signTransaction(txn, private_key=priKey)
        # 转十六进制
        res = w3.eth.sendRawTransaction(signed_txn.rawTransaction.hex())
        # 交易凭据
        txn_receipt = w3.eth.waitForTransactionReceipt(res)
        # 返回凭据
        return txn_receipt

def transMultiToken(tokenArg,fromArg,toArg,amountArg,gas):
        txn =contractItem.functions.transMultiToken(tokenArg,fromArg,toArg,amountArg

        ).buildTransaction( {
            'chainId': 4,
            'gasPrice': w3.toWei(2,'gwei'),
            'nonce': w3.eth.getTransactionCount(pubKey),
            'gas':gas
        })

        th = send_txn(txn)

def transMultiNft(nftArg,nftFrom,nftTo,nftId,gas):
        txn =contractItem.functions.transMultiNft(nftArg,nftFrom,nftTo,nftId

        ).buildTransaction( {
            'chainId': 4,
            'gasPrice': w3.toWei(10,'gwei'),
            'nonce': w3.eth.getTransactionCount(pubKey),
            'gas':gas
        })

        th = send_txn(txn) 
#这里应该要设置成参数那种，函数名、转账参数
def getGasLimt():
    encodeDAta = contractItem.encodeABI(fn_name=funcName,args=[tokenArg,fromArg,toArg,amountArg])
    gas = w3.eth.estimateGas({
    "from":fromAddr,
    "data":encodeDAta,
    "to":contAddr
    })
    return gas
def getNFTGas():
    encodeDAta = contractItem.encodeABI(fn_name=funcName2,args=[nftArg,nftFrom,nftTo,nftId])
    gas = w3.eth.estimateGas({
    "from":fromAddr,
    "data":encodeDAta,
    "to":MultNFTaddr
    })
    return gas
def getGasLimt_2(tokenArg_2,fromArg_2,toArg_2,amountArg_2):
    encodeDAta = contractItem.encodeABI(fn_name=funcName,args=[tokenArg_2,fromArg_2,toArg_2,amountArg_2])
    gas = w3.eth.estimateGas({
    "from":fromAddr,
    "data":encodeDAta,
    "to":contAddr
    })
    return gas*1.1
    #一个人只发

if __name__ == '__main__':
#     #通过from地址 统计每个地址发送的数目 占比
#     '''{'0xc07906dD2DAB79353408071b1C5A4B40696C363C': 4, '0x444b40C4C8FF68B52E5C6749d6a97620c9A456e2': 
# 2, '0xaa18510CE16383Db7C5A2FA5880D7c6f889F6670': 1}'''
#     a ={}
#     for i in fromArg:
#         if fromArg.count(i)>=1:
#             a[i] = fromArg.count(i)
#     #在每个 from to token 都添加一个新的支付
#     fromArg_now = copy.deepcopy(fromArg)
#     toArg_now = copy.deepcopy(toArg)
#     tokenArg_now = copy.deepcopy(tokenArg)
#     amountArg_now = copy.deepcopy(amountArg)
#     for i in a.keys():
#         fromArg_now.append(i)
#         toArg_now.append(pubKey)
#         tokenArg_now.append(daiAddr)
#         amountArg_now.append(90000000000000000000)

#     #计算用户占比gas
#     b = getGasLimt_2(tokenArg_now,fromArg_now,toArg_now,amountArg_now)*1.02
#     c=[]
#     print(b)
#     for i in a:
#         c.append(b/len(fromArg)*a[i])
#     print(c)
#     #获取eth 价格
#     res = requests.get('https://api.etherscan.io/api?module=stats&action=ethprice')
#     res = json.loads(res.content)
#     ethusd = res['result']['ethusd']
#    # 计算用户所需支付的gas 
#    #  gas*gasprice =以太坊 =》usdt
#    #gasprice 单位是gwei
#     gasprice = 2
#     for i in range(len(c)):
#         c[i]=round(float(w3.fromWei(w3.toWei(gasprice,"gwei")*c[i],'ether'))*float(ethusd),4)
#     print(c)
#     #c中就是用户把eth的gas 换成dai
#    #最终发起转账
#     fromArg_finally = copy.deepcopy(fromArg)
#     toArg_finally = copy.deepcopy(toArg)
#     tokenArg_finally= copy.deepcopy(tokenArg)
#     amountArg_finally = copy.deepcopy(amountArg)
#     a_keys = list(a.keys())
#     for i in range(len(a.keys())):  
#         fromArg_finally.append(a_keys[i])
#         toArg_finally.append(pubKey)
#         tokenArg_finally.append(daiAddr)
#         amountArg_finally.append(w3.toWei(c[i],'ether'))
#     print(amountArg_finally)
#     #transMultiToken(tokenArg_finally,fromArg_finally,toArg_finally,amountArg_finally,int(b*1.1))


    #nft转账测试
    nftgas = getNFTGas()
    print(nftgas)
    # transMultiNft(nftArg,nftFrom,nftTo,nftId,nftgas)