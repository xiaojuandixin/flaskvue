import csv
import requests
from bs4 import BeautifulSoup

# 发起 HTTP 请求，获取网页 HTML 源代码
url = 'https://gs.amac.org.cn/amac-infodisc/res/cancelled/manager/index.html'
response = requests.get(url)
html = response.text

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

# 获取所有的表格行（tr 标签）
trs = soup.find_all('tr')

print(trs)

# # 创建 csv 文件并写入表头
# with open('product_info.csv', 'w', newline='') as csvfile:
#     fieldnames = ['管理人名称', '统一社会信用代码', '成立时间', '登记时间', '注销时间', '注销类型']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()

# # 遍历所有的表格行，获取所需要的数据并写入 csv 文件
# for tr in trs:
#     tds = tr.find_all('td')
#     if len(tds) == 6:
#         name = tds[0].text.strip()
#         code = tds[1].text.strip()
#         establish_time = tds[2].text.strip()
#         register_time = tds[3].text
