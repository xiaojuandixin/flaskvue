from selenium import webdriver
 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox') # 这个配置很重要
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver')    # 如果没有把chromedriver加入到PATH中，就需要指明路径
 
driver.get("https://gs.amac.org.cn/amac-infodisc/res/cancelled/manager/index.html")

driver.implicitly_wait(10)  # seconds
html = driver.page_source
with open("data.html", "w") as f:
    f.write(html)
driver.close()