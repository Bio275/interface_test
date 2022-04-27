import configparser as cparser
import os
import shutil
import xlrd
import xlwt
from xlutils.copy import copy
# from openpyxl import styles    openyxl不支持xls格式的表格，xlrd的新版又不支持xlsx格式的，所以这里读取和写入统一为xls格式-使用xlrd,xlwt

from config import setting

cf = cparser.ConfigParser()
cf.read(setting.TEST_CONFIG, encoding="UTF-8")
name = cf.get("tester", "name")


class WriteExcel:

    def __init__(self, filename, sheetname):
        self.filename = filename
        # 判断目标表格是否存在，不存在的话，把用例表格复制一份过去
        # if not os.path.exists(self.filename):
        #     shutil.copy(setting.SOURCE_FILE, setting.TARGET_FILE)
        # 获取sheet对象
        # self.wb = load_workbook(self.filename)
        # self.ws = self.wb.active
        self.wb = xlrd.open_workbook(self.filename)
        self.xls_copy = copy(self.wb)
        self.ws = self.xls_copy.get_sheet(sheetname)

    def write_data(self, row_n, value):
        # RED = ['ffc7ce', '9c0006']  # 红
        # GREEN = ['c6efce', '006100']  # 绿
        # 加上文字颜色和样式,导入colors的包，可以直接用颜色名，但源码被注释了很多颜色，所以这里用的Color,16进制来代表颜色
        # font_Green = Font(name='宋体', color=GREEN, bold=True)
        # font_Red = Font(name='宋体', color=RED, bold=True)

        if value == "PASS":
            self.ws.write(row_n, 11, value, style=xlwt.easyxf('pattern: pattern solid, fore_colour %s;' % "green"))
        if value == "FAIL":
            self.ws.write(row_n, 11, value, style=xlwt.easyxf('pattern: pattern solid, fore_colour %s;' % "red"))
        self.ws.write(row_n, 12, name)
        self.xls_copy.save(self.filename)
