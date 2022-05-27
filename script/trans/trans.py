# 导入依赖
from web3 import Web3
from web3.providers import HTTPProvider
from transConfig import *

# 构造 web3 实例
w3 = Web3(HTTPProvider(endpointHttp))
contractItem = w3.eth.contract(address=contAddr, abi=contAddr)

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
    


     

    def send_txn(self, txn):
        # 账户
        signed_txn = self.web3.eth.account.signTransaction(txn, private_key=self.my_private_key)
        # 转十六进制
        res = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction.hex())
        # 交易凭据
        txn_receipt = self.web3.eth.waitForTransactionReceipt(res)
        # 返回凭据
        return txn_receipt

    def bnbtransfer(self,value):
        to_address =self.alladdress
        txn =self.bnbtool.functions.transferEthsAvg(to_address).buildTransaction( {
            'chainId': 56,
            'gasPrice': Web3.toWei(5, "gwei"),
            'nonce': self.web3.eth.getTransactionCount(self.my_address),
            'value': Web3.toWei(value,'ether'),
            'gas':900000
        })

        th = self.send_txn(txn)
if __name__ == '__main__':
    bnbtool=BNBTOOL()
    bnbtool.bnbtransfer(0.008)


