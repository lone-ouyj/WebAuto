#! /usr/bin/env python
# -*- conding:utf-8 -*-
"""
@Time : 2021/7/2 16:55
@Author : 搁浅灬惜缘
@file : login_page.py
"""

from selenium.webdriver.common.by import By
# from base.BaseAction import WebDriver
from business.defalut_login import DefaultLogin
from utils.logging_util import Logger
from utils.env_util import SERVERIP
import time

logging = Logger().get_logger()
address = SERVERIP + '/login.html#/'


class Login(DefaultLogin):
    username_loc = (By.XPATH, "/html/body/section/div/section/form/div[1]/div[2]/div/div/input")
    password_loc = (By.XPATH, "/html/body/section/div/section/form/div[2]/div[2]/div/div/input")
    login_loc = (By.XPATH, "/html/body/section/div/section/form/div[3]/div[2]/button")
    error_loc = (By.XPATH, "/html/body/div/div/div[1]/p")
    username_error_loc = (By.XPATH, "/html/body/section/div/section/form/div[1]/div[2]")
    password_error_loc = (By.XPATH, "/html/body/section/div/section/form/div[2]/div[2]")
    quit_exit_loc = (By.XPATH, "/html/body/div/main/div[1]/div/span")
    exit_loc = (By.XPATH, "/html/body/ul/li[2]")
    define_loc = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]')

    def login(self, username=None, password=None):
        if username is not None:
            self.input_value(self.username_loc, username)
            logging.info("用户名:{0}".format(username))
        if password is not None:
            self.input_value(self.password_loc, password)
            logging.info("密码:{0}".format(password))
        self.click_element(self.login_loc)
        logging.info("点击登录按钮")
        Logger().close_logger()

    def login_out(self):
        if self.is_element_exist(self.username_loc):
            self.default_login()
        try:
            self.click_element(self.quit_exit_loc)
            self.click_element(self.exit_loc)
            self.click_element(self.define_loc)
        except:
            logging.error("退出登录失败")
        Logger().close_logger()

    def username_error_message(self):
        message = self.get_element_attribute(self.username_error_loc, 'textContent')
        return message

    def password_error_message(self):
        message = self.get_element_attribute(self.password_error_loc, 'textContent')
        return message

    def login_message(self):
        message = self.get_element_text(self.error_loc)
        return message

    def login_out_url(self):
        self.is_element_exist(self.username_loc)
        return self.get_current_url


if __name__ == '__main__':
    t = Login()
    t.maximize_window
    t.get_url("http://test2-followup.myweimai.com/#/")
    t.login_out()
    time.sleep(2)
    t.quit()
