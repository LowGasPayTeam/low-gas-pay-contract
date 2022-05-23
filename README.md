# LowGasPay
Transfer and trade with low Gas.

## 概述
对于绝大多数的链上交易，用户并不急于完成，立即执行会造成极大的 gas fee 损失，通过我们的平台，用户授权后，系统自动托管，帮助用户在指定时间内，最低的 gas 价格时进行交易，面向 Uniswap 等平台链上交易，Metamask 等平台转账，Binance 等交易所冲提币，质押，领取奖励，Opensea 批量挂单，Opensea 批量撤单等所有 Web3.0 操作。该项目目的有以下几点：1. ETH 生态优化，类似于 Layer1 Layer2 的意义，让链上不再拥挤，更加人性化；2. 满足用户的低手续费需求，70% Web3.0 操作其实并不急需完成，0.02 的 gas 去购买 0.01 的 NFT 屡屡发生，通过我们的工具可以降低成本；3. 订单拆分，将企业级 1000wu 的交易，延迟拆分为多单，保证有效性和安全性，以及低成本。

## 优点
1. 转账钱包里不需要 ETH
2. ETH 链上压力分摊

## 开发周期
1. 第一阶段: 2022.05.21 - 2022.06.04
2. 第二阶段: 2022.06.05 - 2022.06.18
3. 第三阶段: 2022.06.19 - 2022.07.02

## 开发人员
1. 合约底层开发: Wiger, Soth
2. 网页前端开发: Locky
3. 网页后端开发: 爆爆, Bill

## 开发流程
1. 合约底层开发
2. 链上实时 Gas 费
3. 链上历史 Gas 费
4. 钱包授权

## 平台功能对接
1. Token 低 Gas 择时转账: 1 to 1
2. Token 低 Gas 择时转账: 1 to n
3. NFT 低 Gas 择时转账: 1 to 1
4. NFT 低 Gas 择时转账: n to m
5. Binance 等 CEX 低 Gas 择时充币
6. Uniswap 等 DEX 低 Gas 择时交易 (附带价格范围限制)
7. Opensea 等 NFT 平台 低 Gas 择时购买 (附带价格范围限制)
8. Gem 配合 低 Gas 择时批量购买 (附带价格范围限制)
9. 多链支持
10. 多平台支持
- 第一阶段计划: 1 - 4
- 第二阶段计划: 5 - 8
- 第三阶段计划: 9 - 10

## 网页前端开发
1. Connect Wallet: 连接 Metamask (暂不考虑 Phantom 等钱包)
2. 功能选择: Token 转账, NFT 转账, 冲提币 (其他)
3. Token 转账 / 交易所充币:
  - a. Token 转出地址栏
  - b. Token 转入地址栏 (点击加号可扩展为多个)
  - c. Token 转出金额栏
  - d. Token 转入金额栏 (伴随着地址栏加号扩展, 同步增加)
  - e. 转出地址 txt 文件导入 (一个按钮, 点击后上传文件)
  - f. 显示历史 24h, 12h, 1h, 5min Gas 费
  - g. 手动输入 Gas 范围 (默认值为 24 小时最低)
  - h. 授权按钮
  - i. 确认按钮

4. NFT 转账:
  - a. 钱包中 NFT 可视化展示
  - b. 勾选需转账的 NFT
  - c. NFT 转出地址栏
  - d. NFT 转入地址栏 (点击加号可扩展为多个)
  - e. NFT 转出金额栏
  - f. NFT 转入金额栏 (伴随着地址栏加号扩展, 同步增加)
  - g. 转出地址 txt 文件导入 (一个按钮, 点击后上传文件)
  - h. 显示历史 24h, 12h, 1h, 5min Gas 费
  - i. 手动输入 Gas 范围 (默认值为 24 小时最低)
  - j. 授权按钮
  - k. 确认按钮

5. 订单列表:
  a. 查看当前钱包下订单列表
  b. 修改转账金额
  c. 修改预期 Gas
  d. 删除订单

## 网页后端开发
1. 钱包账户验证
2. 增加订单
3. 删除订单
4. 查询订单
5. 修改订单
6. 向脚本发起调用: 1 - 8 功能
7. 获取脚本传回 Gas, 返回前端
8. 获取脚本传回 Gas History, 返回前端
9. 获取脚本传回 Transfer Result, 返回前端
10. 获取脚本传回 Order Result, 返回前端

## 技术文档
### Gas 实时与历史数据
1. Gas 获取 Ethereum Gas Tracker 网页: https://etherscan.io/gastracker
2. Gas 获取 Ethereum Gas Tracker API: https://docs.etherscan.io/api-endpoints/gas-tracker

### 转账
1. 部署转账合约
2. web3.py 实现调用

## 核心
### 第一次交易
1. 授权: 合约

### 第二次交易: WETH 交易, 因为 ETH 无法授权
1. ETH: 用户发送地址 => 用户接收地址
2. ETH Gas: Low Gas Pay => ETH 矿工
3. WETH 等值 Gas: 用户 => Low Gas Pay

## Gas 实时与历史数据
1. Gas 获取 Ethereum Gas Tracker 网页: https://etherscan.io/gastracker
2. Gas 获取 Ethereum Gas Tracker API: https://docs.etherscan.io/api-endpoints/gas-tracker

## 转账
1. 部署转账合约
2. web3.py 实现调用
