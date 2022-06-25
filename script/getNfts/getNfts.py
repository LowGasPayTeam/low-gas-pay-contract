# 导入依赖
import requests

# 请求链接
url = "https://api.opensea.io/api/v1/assets?owner=0x000000fc3bd4cb95C4ae6307c63e2edc1212109A&order_direction=desc&limit=20&include_orders=false"

# Header
headers = {
    "Accept": "application/json",
    "X-API-KEY": "23eaf1789d914c6f91f1fa03ee65455c"
}

# 返回结果
response = requests.get(url, headers=headers)

# 显示 NFTs
print(response.text)