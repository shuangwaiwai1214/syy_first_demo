from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 配置Chrome选项
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 设置Service
service = Service(r"D:\software\Python\pythonProject\Web自动化测试\chapter4\chromedriver.exe")

driver = webdriver.Chrome(service=service,options=chrome_options)
driver.get("https://www.baidu.com")
driver.maximize_window()

# 等待页面加载
time.sleep(1)

# 使用JavaScript方式（最稳定，避免交互问题）
driver.execute_script("document.getElementById('chat-textarea').value = '老师';")
driver.execute_script("document.getElementById('chat-submit-button').click();")

print("搜索完成！")

# 等待查看结果
time.sleep(3)

# 关闭浏览器
driver.quit()