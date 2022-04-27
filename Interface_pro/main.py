# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

from config import setting
import unittest
from packages import HtmlTestRunner
from common import newreport
from common.sendmail import send_mail
import os
import urllib3
# 忽略证书警告
urllib3.disable_warnings()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# 将用例放入
def add_case(run_path=setting.TEST_CASES):
    discover = unittest.defaultTestLoader.discover(run_path, "*API.py")
    return discover


# 执行用例,生成报告,发送邮件
def run_case(all_case, result_path=setting.TEST_REPORT):
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = result_path + "\\" + now + "result.html"
    # 创建html文件
    fp = open(filename, "wb")
    # 定义测试报告
    runner = HtmlTestRunner.HTMLTestRunner(stream=fp, title="测试接口自动化测试", description="这是描述-可以写环境配置等", tester="Csj")
    # 运行测试用例，运行测试容器中的用例，并将结果写入到报告中
    runner.run(all_case)
    # 关闭文件流，将html内容写进测试报告文件
    fp.close()
    # 取测试报告目录中最新的一个
    report = newreport.new_report(setting.TEST_REPORT)
    # 发送邮件
    # send_mail(report)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cases = add_case()
    run_case(cases)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
