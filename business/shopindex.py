#! /usr/bin/env python
#-*- conding:utf-8 -*-
'''
@Time : 2020/5/8 12:42
@Author : 搁浅灬惜缘
@file : shopindex.py
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.BaseAction import WebDriver
from utils.logging_util import Logger
import time
logging = Logger().get_logger()

class Permission(WebDriver):
    username_loc = (By.XPATH,'/html/body/div/form/div[1]/div/div[1]/input')
    password_loc = (By.XPATH,'/html/body/div/form/div[2]/div/div[1]/input')
    verfy_loc = (By.XPATH, '/html/body/div/form/div[3]/div/div/div[1]/div/input')
    login_loc = (By.XPATH, '/html/body/div/form/div[4]/div/button')

    def login_info(self,username,password):
        self.input_value(self.username_loc,username)
        self.input_value(self.password_loc,password)
        input_test = int(input("请输入验证码：\n"))
        self.input_value(self.verfy_loc, input_test)
        self.click_element(self.login_loc)


if __name__ == '__main__':
    from base.driver import *
    driver = open_browser()
    t = Permission(driver)
    t.get_url("http://10.12.107.23/admin/#/login")
    time.sleep(2)
    driver.quit()