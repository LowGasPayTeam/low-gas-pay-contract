# ETH Endpoint Http
# taskendpointHttp = 'https://mainnet.infura.io/v3/aedb921ebff24c7dbafd665609a5520d'
# Rinkeby Endpoint Http
taskEndpointHttp = 'https://rinkeby.infura.io/v3/aedb921ebff24c7dbafd665609a5520d'
# BSC Endpoint Http
# taskendpointHttp = 'https://bsc-dataseed.binance.org/'

# 合约地址
taskContAddr = '0x5192D14aaD1602df4D8D63a1EDA515BEcBeA3424'
erc20Abi = '''
[
    {
        "constant": true,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_spender",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_from",
                "type": "address"
            },
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            },
            {
                "name": "_spender",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "payable": true,
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "from",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "to",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    }
]
'''
        
# 调用者地址
taskFromAddr = '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710'
# 合约 ABI
taskContAbi = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"token","type":"address[]"},{"internalType":"address[]","name":"from","type":"address[]"},{"internalType":"address[]","name":"to","type":"address[]"},{"internalType":"uint256[]","name":"amount","type":"uint256[]"}],"name":"transMultiToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address[]","name":"from","type":"address[]"},{"internalType":"address[]","name":"to","type":"address[]"},{"internalType":"uint256[]","name":"amount","type":"uint256[]"}],"name":"transOneToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
# 函数名称
taskFuncName = 'transMultiToken'

# Token 参数
taskTokenArg = ['0x2Ec4c6fCdBF5F9beECeB1b51848fc2DB1f3a26af', '0x2Ec4c6fCdBF5F9beECeB1b51848fc2DB1f3a26af', '0x2Ec4c6fCdBF5F9beECeB1b51848fc2DB1f3a26af', '0x2Ec4c6fCdBF5F9beECeB1b51848fc2DB1f3a26af', '0x2Ec4c6fCdBF5F9beECeB1b51848fc2DB1f3a26af', '0x2Ec4c6fCdBF5F9beECeB1b51848fc2DB1f3a26af']
# From 参数
taskFromArg = ['0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710']
# To 参数
taskToArg = ['0xE9A55bBCaf61c72FD760c30f1acd9c6908dd0B58', '0xE7AAe14FfB2f23A811d3412bac4bc427866f6C77', '0x1bF7ec8FeC60185863A12b3902204b2D565f602b', '0x5687fe3fd6F2802E56690E30B6257d30eFbce61D', '0xD5a573AA451054ff38DA139521d53bf4E709F27C', '0x915f17C3bc0A0b9F592DF268bd4d541d39660503']
# Amount 参数
taskAmountArg = [1000000000000,1000000000000,1000000000000,1000000000000,1000000000000,1000000000000]

# 调用地址
taskPubKey = '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710'
# 签名私钥
taskPriKey = '9999a4f6709b40f266b3c20a3f2495e2d5fd19b0d5c136a1167aebdf1dd56218'

# 交易链
taskChainId = 4
# Gas Fee 单位 Gwei
taskGasPrice = 2
# Gas Limit
taskGasLimit = 500000
# 编号
taskNonce = 0
# 交易 ETH 数目
taskValue = 0

# 循环间隔
taskLoopDelay = 3