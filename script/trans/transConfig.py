# ETH Endpoint Http
# endpointHttp = 'https://mainnet.infura.io/v3/aedb921ebff24c7dbafd665609a5520d'
# Rinkeby Endpoint Http
endpointHttp = 'https://rinkeby.infura.io/v3/aedb921ebff24c7dbafd665609a5520d'
# BSC Endpoint Http
# endpointHttp = 'https://bsc-dataseed.binance.org/'

# 合约地址
contAddr = '0x5192D14aaD1602df4D8D63a1EDA515BEcBeA3424'
# 调用者地址
fromAddr = '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710'
# 合约 ABI
contAbi = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"token","type":"address[]"},{"internalType":"address[]","name":"from","type":"address[]"},{"internalType":"address[]","name":"to","type":"address[]"},{"internalType":"uint256[]","name":"amount","type":"uint256[]"}],"name":"transMultiToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address[]","name":"from","type":"address[]"},{"internalType":"address[]","name":"to","type":"address[]"},{"internalType":"uint256[]","name":"amount","type":"uint256[]"}],"name":"transOneToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
# 函数名称
funcName = 'transMultiToken'

# Token 参数
tokenArg = ['0x2Ec4c6fCdBF5F9beECeB1b51848fc2DB1f3a26af', '0x2Ec4c6fCdBF5F9beECeB1b51848fc2DB1f3a26af', '0x2Ec4c6fCdBF5F9beECeB1b51848fc2DB1f3a26af', '0x2Ec4c6fCdBF5F9beECeB1b51848fc2DB1f3a26af', '0x2Ec4c6fCdBF5F9beECeB1b51848fc2DB1f3a26af', '0x2Ec4c6fCdBF5F9beECeB1b51848fc2DB1f3a26af']
# From 参数
fromArg = ['0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710']
# To 参数
toArg = ['0xE9A55bBCaf61c72FD760c30f1acd9c6908dd0B58', '0xE7AAe14FfB2f23A811d3412bac4bc427866f6C77', '0x1bF7ec8FeC60185863A12b3902204b2D565f602b', '0x5687fe3fd6F2802E56690E30B6257d30eFbce61D', '0xD5a573AA451054ff38DA139521d53bf4E709F27C', '0x915f17C3bc0A0b9F592DF268bd4d541d39660503']
# Amount 参数
amountArg = [1000000000000,1000000000000,1000000000000,1000000000000,1000000000000,1000000000000]

# 调用地址
pubKey = '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710'
# 签名私钥
priKey = '9999a4f6709b40f266b3c20a3f2495e2d5fd19b0d5c136a1167aebdf1dd56218'

# 交易链
chainId = 4
# Gas Fee 单位 Gwei
gasPrice = 2
# Gas Limit
gasLimit = 500000
# 编号
nonce = 0
# 交易 ETH 数目
value = 0