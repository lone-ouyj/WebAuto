#! /usr/bin/env python
# -*- conding:utf-8 -*-
"""
@Time : 2021/7/2 16:33
@Author : 搁浅灬惜缘
@file : test_login.py
"""

from business.login_page import Login
from business.login_page import address
import unittest
import time


class LoginTest(unittest.TestCase):
    login = Login()
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.login.maximize_window
        self.login.get_url(address)

    def tearDown(self):
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                self.login.get_screenshot(case_name)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.login.quit()
    #
    # def test_login1_empty_username(self):
    #     self.login.login()
    #     context = self.login.username_error_message()
    #     self.assertIn('必须填写用户名', context)
    #
    # def test_login2_empty_password(self):
    #     self.login.login(username='admin')
    #     context = self.login.password_error_message()
    #     self.assertIn('必须填写密码', context)
    #
    # def test_login3_error_password(self):
    #     self.login.login('admin', '123')
    #     context = self.login.password_error_message()
    #     self.assertIn('密码长度必须在6~20位之间', context)
    #
    # def test_login4_error_username(self):
    #     self.login.login('admintest', '12345678')
    #     context = self.login.login_message()
    #     self.assertIn('账号不存在', context)
    #
    # def test_login5_error_password(self):
    #     self.login.login('admin', '1234567899')
    #     context = self.login.login_message()
    #     self.assertIn('密码错误', context)

    def test_login6_success(self):
        self.login.login('admin', '12345678')
        context = self.login.login_message()
        self.assertIn('登录成功', context)

    def test_login7_out(self):
        self.login.login_out()
        url = self.login.login_out_url()
        self.assertIn('login.html#/', url)


if __name__ == '__main__':
    unittest.main()

