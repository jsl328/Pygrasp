
from selenium import webdriver


def googleDriver() -> webdriver:
    driver = webdriver.Chrome(executable_path="/Users/mac/Downloads/chromedriver-4")
    driver.get("https://mp.weixin.qq.com/s/91qi7Q2iEviHK_42K6Oj4A")
    return driver

