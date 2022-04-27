import os

# 根路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 配置文件地址
TEST_CONFIG = os.path.join(BASE_DIR, "database", "config.ini")
# 测试用例地址
SOURCE_FILE = os.path.join(BASE_DIR, "database", "testexcel1.xls")
# 测试用例报告
TEST_REPORT = os.path.join(BASE_DIR, "report")
# 测试结果地址
TARGET_FILE = os.path.join(BASE_DIR, "report", "excelReport", "apiresultexcel.xls")
# 测试用例地址
TEST_CASES = os.path.join(BASE_DIR, "testcases")
