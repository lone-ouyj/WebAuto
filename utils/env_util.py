#! /usr/bin/env python
# -*- conding:utf-8 -*-
"""
@Time : 2020/5/16 22:42
@Author : 搁浅灬惜缘
@file : env_util.py
"""
# import pymysql
from utils.ini_util import ReadIni

read_ini = ReadIni("env_config.ini")

SERVERIP = read_ini.get_value("service", "address")
MYSQL_LOCALHOST = read_ini.get_value("mysql", "localhost")
MYSQL_PORT = int(read_ini.get_value("mysql", "port"))
MYSQL_USER = read_ini.get_value("mysql", "user")
MYSQL_PASSWORD = read_ini.get_value("mysql", "password")
MYSQL_DATABASE = read_ini.get_value("mysql", "databasename")
LOGIN_USER = read_ini.get_value("login", "username")
LOGIN_PASSWORD = read_ini.get_value("login", "password")


# def connect_mysql():
#     db = pymysql.connect(host=localhost,
#                          user=user,
#                          port=port,
#                          password=password,
#                          db=databasename,
#                          charset="utf8")
#     cursor = db.cursor()
#     sql = "select * from ap_t_label"
#     cursor.execute(sql)
#     print(cursor.fetchone())
#     cursor.close()
#     db.close()
#
#
# connect_mysql()
