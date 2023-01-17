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

        self.browser.find_element(By.NAME, "loginSelectionPageEmail").send_keys(self.username)
        time.sleep(1)
        self.browser.find_element(By.LINK_TEXT, "E-Posta ile Giriş Yap").click()

        time.sleep(1)

        self.browser.find_element(By.NAME, "password").send_keys(self.password)
        self.browser.find_element(By.LINK_TEXT, "Giriş Yap").click()




sahibinden = Sahibinden(username, password)
sahibinden.signIn()
# github.getFollowers()
