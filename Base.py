from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.common import WebDriverWaitTime


class TestBase(object):

    def __init__(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)

    def find_element(self, locator: tuple) -> WebDriver:
        return WebDriverWait(self.driver, WebDriverWaitTime).until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple):
        self.find_element(locator).