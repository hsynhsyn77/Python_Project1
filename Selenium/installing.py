from selenium import webdriver
import time
driver = webdriver.Chrome()

url="http://github.com"
driver.get(url)

time.sleep(1)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")

url="http://github.com/hsynhsyn77"
driver.get(url)

print(driver.title)

if "hsynhsyn77" in driver.title:
    driver.save_screenshot("github-hsynhsyn77.png")

time.sleep(1)
driver.back()
#driver.forward()
time.sleep(1)
driver.close()