from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver') 

driver.get('https://gs.amac.org.cn/amac-infodisc/res/cancelled/manager/index.html')

# driver.implicitly_wait(3)

input = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div[2]/div[3]/input")

print(input)
# input.send_keys("2")

# button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div[2]/div[3]/button")
# button.click()

# driver.implicitly_wait(3)

# with open("./fox.html", "w") as f:
#     f.write(driver.page_source)





# driver.find_element_by_id("goInput").send_keys("2")

# from selenium import webdriver, service

# service = Service(executable_path='/home/yan/Python/chromeselenium/chromeselenium/chromedriver')

# driver = webdriver.Chrome(service=service)

# driver.get("网址")

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver') 

# service = Service(chrome_options=chrome_options, executable_path='./chromedriver')

# driver = webdriver.Chrome(service=service)

# driver.get('https://gs.amac.org.cn/amac-infodisc/res/cancelled/manager/index.html')
# driver.implicitly_wait(3)

# inputTag = driver.find_element(By.ID, "goInput")



# # driver.find_element_by_id("goInput").send_keys("2")
# # driver.implicitly_wait(3)



