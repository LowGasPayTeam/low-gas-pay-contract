# -*- coding:utf-8 -*-
import time
from web3 import Web3
from web3.providers import HTTPProvider
from threading import Thread
import re
import requests
import json


class BNBTOOL:
    def __init__(self, parent=None):

        self.mainnet_url = 'https://bsc-dataseed4.ninicoin.io'
        # 构造 web3 实例
        self.web3 = Web3(HTTPProvider(self.mainnet_url))

        self.bnbToolAddress = Web3.toChecksumAddress('0x5A23De909C5F4E987190f6023387B2e666d9c688')
        self.bnbToolAbi = '[{"constant":false,"inputs":[{"name":"_tos","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"transferEths","outputs":[{"name":"","type":"bool"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"}],"name":"transferEth","outputs":[{"name":"","type":"bool"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"caddress","type":"address"},{"name":"_tos","type":"address[]"},{"name":"v","type":"uint256"}],"name":"transferTokensAvg","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_tos","type":"address[]"}],"name":"transferEthsAvg","outputs":[{"name":"","type":"bool"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[],"name":"destroy","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"caddress","type":"address"},{"name":"_tos","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"transferTokens","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"checkBalance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":true,"stateMutability":"payable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"}]'
        self.bnbtool = self.web3.eth.contract(address=self.bnbToolAddress, abi=self.bnbToolAbi)

        self.alladdress = ['0x5795dd7D7367BccEC489153E4cB62dB5221F884e',
                           '0xA3E9C3a8A9C577340F7f99Cb13d26EB76ca19F79',
                          ]

        # '0xb0e9dE837e3f652cbE1c1dc2D34785f511541315', '0x9D8171080591Fe1f5C65250e6AB67B8Dfa63E3A6',
        # '0x1c327384b7fD346baBbbDF7DB74A78014fa37832', '0xA7b091957ADc7cF5f847FCB2f0F4B2c6eb3979dF',
        # '0x83E3C71EDcF8e8ED08A4530BF4b1818730743e6A',
        # '0xF2fba2c9A61645cC532fD6424D72480D4ea1D28D', '0x328093BB605a34564d174389e6Ba595B8abC4984',
        # '0x79733034e890bffb1A76c0c57E0CA383F7B6C76e',
        # '0x8cc1336016b788F6F4eb0F051B05E7C912dB17fb', '0xD730a551f53Dc00AE364B43084dB3F3e99BC20eE',
        # '0xd854EcC102E198a56B6e65B7a37c827487831656'

        self.my_address=Web3.toChecksumAddress('0xdD54526f211119E80B2a3bdaE5722804eF7E8498')
        self.my_private_key='5d830ad480d6ded8bbde35ee3f22665b2a4616ecce41769997207d14fa2f9deb'


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


