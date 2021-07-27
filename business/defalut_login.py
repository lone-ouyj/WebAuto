#! /usr/bin/env python
# -*- conding:utf-8 -*-
"""
@Time : 2021/7/9 16:18
@Author : 搁浅灬惜缘
@file : defalut_login.py
"""

from selenium.webdriver.common.by import By
from base.BaseAction import WebDriver
from utils.env_util import *
from utils.logging_util import Logger
import time

logging = Logger().get_logger()
address = SERVERIP + '/login.html#/'
message = '登录成功'

username_loc = (By.XPATH, "/html/body/section/div/section/form/div[1]/div[2]/div/div/input")
password_loc = (By.XPATH, "/html/body/section/div/section/form/div[2]/div[2]/div/div/input")
login_loc = (By.XPATH, "/html/body/section/div/section/form/div[3]/div[2]/button")
error_loc = (By.XPATH, "/html/body/div/div/div[1]/p")


class DefaultLogin(WebDriver):
    def default_login(self, username=LOGIN_USER, password=LOGIN_PASSWORD):
        for i in range(5):
            if address not in self.get_current_url:
                print(self.get_current_url)
                self.get_url(address)
            self.input_value(username_loc, username)
            logging.info("用户名:{0}".format(username))
            self.input_value(password_loc, password)
            logging.info("密码:{0}".format(password))
            self.click_element(login_loc)
            logging.info("点击登录按钮")
            success_message = self.get_element_text(error_loc)
            if message in success_message:
                break


if __name__ == '__main__':
    t = DefaultLogin()
    t.default_login(LOGIN_USER,LOGIN_PASSWORD)
    time.sleep(2)
    t.quit()