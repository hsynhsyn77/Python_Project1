from selenium.webdriver.common.by import By

from instagramInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        usernameInput = self.browser.find_element(By.NAME, "username")
        passwordInput = self.browser.find_element(By.NAME, "password")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        time.sleep(2)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(4)


    def getFollwers(self):
        #self.browser.find_element(By.XPATH, "//*[@id='ff389100c9c4f4']/div/div/a").click()

        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(4)
        self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_bU']/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div").click()
        time.sleep(2)

        fallowers=self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog] ul").find_element(By.CSS_SELECTOR,"li")

        for user in fallowers:
            link= user.find_element(By.CSS_SELECTOR,"a").get.attribute("href")
            print(link)

instagram = Instagram(username, password)
instagram.signIn()
instagram.getFollwers()
