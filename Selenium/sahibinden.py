import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

from sahibindenUserInfo import username, password
from selenium import webdriver


class Sahibinden:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        #self.followers = []

    def signIn(self):
        self.browser.get("https://secure.sahibinden.com/giris")

        username=self.browser.find_element(By.NAME, "loginSelectionPageEmail")
        username.send_keys(self.username)
        username.send_keys(Keys.ENTER)
        password=self.browser.find_element(By.NAME, "password")
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)





sahibinden = Sahibinden(username, password)
sahibinden.signIn()
# github.getFollowers()
