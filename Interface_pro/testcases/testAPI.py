import unittest
import requests
import ddt, json
from common.readexcel import ReadExcel
from common.writeexcel import WriteExcel
from config import setting
from common.sendrequests import SendRequests

testData = ReadExcel(setting.SOURCE_FILE, "Sheet1").read_excel()


@ddt.ddt
class Demo_API(unittest.TestCase):

    # 前置
    def setUp(self):
        self.s = requests.session()

    # 后置
    def tearDown(self):
        pass

    @ddt.data(*testData)
    def test_api(self, data):
        # 通过ID来获取对应的行数，便于输出对应结果到对应行
        rowNum = int(data["ID"].split("_")[1])
        print("正在执行用例------->{0}".format(data["ID"]))
        print("请求地址为----->{0}，方法为------>{1}".format(data["url"], data["method"]))
        print("请求参数为------>{0}".format(data["params"]))
        print("请求体类型为{0},请求体内容为{1}".format(data["type"], data["body"]))
        re = SendRequests().sendrequests(self.s, data)
        re_txt = re.text
        self.result = json.loads(re_txt)
        # self.result = re.json()

        # 断言返回的内容
        read_code = data["status_code"]
        read_msg = data["msg"]
        # 因为接口文档的问题，这里暂时的逻辑是状态码和msg其中一个断言成功就算PASS（实际上应该是两者都要满足才行）
        if read_code == self.result["code"] or read_msg == self.result["message"]:
            OK_data = "PASS"
            print("测试结果为通过：{0}----->{1}".format(data["ID"], OK_data))
            # 写入测试结果
            WriteExcel(setting.TARGET_FILE, "Sheet1").write_data(rowNum, OK_data)
        if read_code != self.result["code"] and read_msg != self.result["message"]:
            No_data = "FAIL"
            print("测试结果为不通过：{0}----->{1}".format(data["ID"], No_data))
            # 写入测试结果
            WriteExcel(setting.TARGET_FILE, "Sheet1").write_data(rowNum, No_data)
        self.assertEqual(self.result['code'], read_code, "返回实际结果是->:%s" % self.result['code'])

if __name__=='__main__':
    unittest.main()
