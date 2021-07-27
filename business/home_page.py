#! /usr/bin/env python
# -*- conding:utf-8 -*-
"""
@Time : 2021/7/6 16:58
@Author : 搁浅灬惜缘
@file : home_page.py
"""
import time

from selenium.webdriver.common.by import By
from base.BaseAction import WebDriver
from utils.env_util import SERVERIP
from utils.logging_util import Logger
import time


logging = Logger().get_logger()
address = SERVERIP + "/#/"


class Home(WebDriver):
    system_setting_loc = (By.XPATH, "/html/body/div/main/div[2]/div[2]/div[7]/div")
    data_center_loc = (By.XPATH, "/html/body/div/main/div[2]/div[1]/div[3]/div/div[1]")
    medical_workstation_loc = (By.XPATH, "/html/body/div/main/div[2]/div[1]/div[1]/div/div[1]")
    data_check_loc = (By.XPATH, "/html/body/div/main/div[2]/div[2]/div[5]/div")
    medical_service_loc = (By.XPATH, "/html/body/div/main/div[2]/div[2]/div[1]/div")
    disease_map_loc = (By.XPATH, "/html/body/div/main/div[2]/div[2]/div[3]/div")

    def dump_system_setting(self):
        self.click_element(self.system_setting_loc)

    def dump_data_center(self):
        self.click_element(self.data_center_loc)

    def dump_medical_workstation(self):
        self.click_element(self.medical_workstation_loc)

    def dump_data_check(self):
        self.click_element(self.data_check_loc)

    def dump_medical_service(self):
        self.click_element(self.medical_service_loc)

    def dump_disease_map_loc(self):
        self.click_element(self.disease_map_loc)

if __name__ == '__main__':
    if '123456'not in 'sdfjaslfk12345':
        print(1)
    else:
        print(2)