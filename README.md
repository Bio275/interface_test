## 框架介绍
Python接口自动化测试
框架使用了python3+selenium+unittest,利用ddt进行数据驱动，Excel管理用例等集成测试数据方式。
项目结构:
* 1.common：基础类和方法---读取excel数据类和方法（ReadExcel），执行接口请求类型和方法(SendRequest)，写入excel数据类和方法（WriteExcel），发送邮件类和方法（SendMail）
* 2.config：存放一些路径和配置
* 3.database：放测试用例数据和基础配置文件conf.ini
* 4.packages：包文件夹，这里是用来存放自定义的HtmlTestRunner的测试报告文件
* 5.report：测试报告存放
* 6.testcases：测试用例
* 7.main.py：执行的主程序

## 基本流程
* 大致流程为：
* 1.读取excel用例数据（ReadExcel）
* 2.将读取的内容传递到SendRequest请求方法里（ddt的方式）
* 3.将请求返回的内容断言后,将结果写入到Excel里（WriteExcel）
* 4.将测试结果生成html报告（HtmlTestRunner ---python3的很多语法不适用于这个报告,需要手动修改一些python3和python2里面不同的地方,我代码里面的已经做了修改，也可自己添加一些方法来优化测试报告文件）
* 5.将测试报告发送到指定邮箱（SendMail ---这里使用的是QQ邮箱的STMP服务，需要获取授权码，具体操作可百度到）

## 测试结果（截图 ---项目里面包含了用例文件和结果）
* 1.用例截图：
![接口用例截图](https://user-images.githubusercontent.com/40814664/165670659-eac3ea96-eac2-4fff-bb50-6663fbfadbb8.png)

* 2.测试结果截图（Excel）：
![用例结果截图](https://user-images.githubusercontent.com/40814664/165670787-f2b0f54e-93a1-4933-b84f-ab03f53474f4.png)

* 3.测试结果报告截图(html)：
![测试结果报告截图](https://user-images.githubusercontent.com/40814664/165670967-bba42191-2252-46f3-86f2-75543c8ebef1.png)
