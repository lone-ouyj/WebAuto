# python+selenium+unittest+BSTestRunner框架介绍
本框架能实现web端ui自动化测试，结合日志收集、发邮件、配置文件读取等功能。
###### **1.环境准备**
提前将浏览器驱动文件下载放在安装python的目录下即可

python版本：python3.8

selenium版本：selenium3.141.0 [使用python自带的pip命令安装即可，下同]

ddt版本：ddt1.4.1

pymysql版本：pymysql0.9.3

openpyxl版本：openpyxl3.0.7

###### **2.项目介绍**
base：存放封装好各类方法;

business：存放各个业务模块的封装

config：存放一些配置文件，如邮件配置，数据库配置等

data：可存放xls格式的测试用例

log：存放运行的日志，自动生成

report：存放运行测试用例的报告结果，通过BSTestRunner生成

screenshot：存放运行中的截图

testcase：存放各个业务模块的用例

utils：存放日志收集、邮件信息、excel操作、msyql数据库操作、获取配置信息等功能类和方法

run_alltest.py：运行testcase中所有的用例集

###### **3.后期工作**
1.完善对mysql数据库的操作

2.增加对excel文件的写入操作

3.ddt数据驱动管理