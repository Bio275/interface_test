# interface_test
Python接口自动化测试
框架使用了python3+selenium+unittest,利用ddt进行数据驱动，Excel管理用例等集成测试数据方式。
项目结构:
1.common:基础类和方法---读取excel数据类和方法（ReadExcel），执行接口请求类型和方法(SendRequest)，写入excel数据类和方法（WriteExcel），发送邮件类和方法（SendEmail）
2.config：存放一些路径和配置
3.database:放测试用例数据和基础配置文件conf.ini
4.packages:包文件夹，这里是用来存放自定义的HtmlTestRunner的测试报告文件
5.report：测试报告存放
6.testcases:测试用例
7.main.py：执行的主程序


    
