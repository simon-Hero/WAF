import os

import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utils.common import WebDriverWaitTime, page_path, case_path


class BasePage(object):

    def __init__(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
        self.action = ActionChains(self.driver)

    def find(self, by, locator: tuple):
        """find element"""
        if WebDriverWait(self.driver, WebDriverWaitTime, 0.5).until(EC.element_to_be_clickable(locator)):
            ele = self.driver.find_element(by, locator)
            return ele
        else:
            return None

    def click(self, by, locator: tuple):
        """click element"""
        if self.find(by, locator):
            self.find(by, locator).click()
            return self
        else:
            return False

    def send(self, by, locator: tuple, value=None):
        """set value to the input box"""
        if value:
            self.find(by, locator).send_keys(value)
        return self

    def delete_send(self, by, locator: tuple):
        """delete input data"""
        ele = self.find(by, locator)
        ele.send_keys(Keys.CONTROL + 'a')
        ele.send_keys(Keys.BACK_SPACE)
        return self

    def select(self, by, locator: tuple, text):
        """choose the select"""
        ele = self.find(by, locator)
        if ele:
            select = Select(ele)
            select.deselect_by_visible_text(text)
            return

    def execute_js(self, js):
        """execute the js"""
        self.driver.execute_script(js)
        return self

    def parse_page_yaml(self):
        """
        1. 收集yml
        :return:
        """
        for yml_name in os.listdir(page_path):
            with open(page_path + '/' + yml_name, 'r') as f:
                page_data = yaml.safe_load(f)
            print(yml_name + " data is {}".format(page_data))

    def parse_case_yml(self):
        pass

    def switch_frame(self):
        """switch to frame"""
        pass

    def switch_window(self):
        """switch window handles"""
        pass

    def switch_alert(self):
        """switch alert, click yes or no or get text or send keys
        consider alert\confirm\prompt
        """
        pass


if __name__ == '__main__':
    BasePage().parse_page_yaml()
