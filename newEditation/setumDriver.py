
from selenium import webdriver
import time


class seleniumDriver:

    def __init__(self):
        # def webdriver;
        self.driver = webdriver.Chrome(executable_path="/Users/mac/Downloads/chromedriver-3")
        self.driver.get("https://mp.weixin.qq.com/s/91qi7Q2iEviHK_42K6Oj4A")
        pass

    def webdriver(self):

        return self.driver