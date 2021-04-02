#! /usr/bin/env python
# -*- conding:utf-8 -*-
"""
@Time : 2020/5/3 21:32
@Author : 搁浅灬惜缘
@file : driver.py
"""
from selenium import webdriver
from utils.logging_util import Logger
from utils.ini_util import ReadIni

logging = Logger().get_logger()
read_ini = ReadIni('sys_config.ini')


def open_browser(browertype=None):
    driver_path = read_ini.get_value('sys_default', 'driver_path')
    if browertype is not None:
        if "Chrome" in browertype:
            logging.info("启动Chrome浏览器,驱动位置:{0}".format(driver_path))
            driver = webdriver.Chrome(driver_path)
        elif "firefox" in browertype:
            logging.info("启动Firefox浏览器,驱动位置:{0}".format(driver_path))
            driver = webdriver.Firefox(driver_path)
        elif "ie" in browertype:
            logging.info("启动Ie浏览器,驱动位置:{0}".format(driver_path))
            driver = webdriver.Ie(driver_path)
        elif "PhantomJS" in browertype:
            logging.info("启动PhantomJS浏览器,驱动位置:{0}".format(driver_path))
            driver = webdriver.PhantomJS(driver_path)
        else:
            logging.info("启动默认Chrome浏览器,驱动位置:{0}".format(driver_path))
            driver = webdriver.Chrome(driver_path)
    else:
        logging.info("启动默认Chrome浏览器,驱动位置:{0}".format(driver_path))
        driver = webdriver.Chrome(driver_path)
    Logger().close_logger()
    return driver


if __name__ == '__main__':
    t = open_browser("Chrome")
