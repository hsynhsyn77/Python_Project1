from selenium.webdriver.common.by import By
import time
from twitterIUserinfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Twitter:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(3)

        self.browser.find_element(By.XPATH, "//input[@autocomplete='username']").send_keys(self.username)
        self.browser.find_element(By.XPATH, "(//*[@role='button'])[3]").click()
        time.sleep(2)

        passwordInput = self.browser.find_element(By.XPATH, "//*[@name='password']")
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(4)

    def search(self, hashtag):
        searchınput = self.browser.find_element(By.XPATH,
                                                "/html//div[@id='react-root']/div/div/div[2]/main[@role='main']/div/div/div/div[2]/div[@class='css-1dbjc4n r-1pi2tsx']/div[2]/div/div[@class='css-1dbjc4n']//form[@role='search']//label/div[@class='css-1dbjc4n r-16y2uox r-1wbh5a2']/div/input[@role='combobox']")
        searchınput.send_keys(hashtag)
        time.sleep(3)

        searchınput.send_keys(Keys.ENTER)
        time.sleep(3)
        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 5:
                break
                self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter+=1
        list = self.browser.find_elements(By.XPATH,
                                          "//article[@data-testid='tweet']/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]")
        for item in list:
            print("***************** ")
            print(item.text)
        print(len(list))


twitter = Twitter(username, password)
twitter.signIn()
twitter.search("python")
