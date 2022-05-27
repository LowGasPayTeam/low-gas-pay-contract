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
tokenArg = ['0xc7AD46e0b8a400Bb3C915120d284AafbA8fc4735', '0x6D7F0754FFeb405d23C51CE938289d4835bE3b14', '0x52201ff1720134bBbBB2f6BC97Bf3715490EC19B', '0xD9BA894E0097f8cC2BBc9D24D308b98e36dc6D02', '0x577D296678535e4903D59A4C929B718e1D575e0A', '0x2fB298BDbeF468638AD6653FF8376575ea41e768']
# From 参数
fromArg = ['0xc07906dD2DAB79353408071b1C5A4B40696C363C', '0x444b40C4C8FF68B52E5C6749d6a97620c9A456e2', '0x10A03B8842FBF4f58350202C65D1e1E5c36d4068', '0xF59AE7b2C00CEe6B52C887A1088382d14Bca3456', '0x5FDf3008FAe527DC629C15258341301066442c4f', '0xaa18510CE16383Db7C5A2FA5880D7c6f889F6670']
# To 参数
toArg = ['0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710', '0x51A39C80Da2B7Ef85B5170Dd6F932F9Ecb767710']
# Amount 参数
amountArg = ['1100000000', '1200000000', '1300000000', '1400000000', '1500000000', '1600000000']