import ddt
import unittest
testdata1 = [{'username':'zhangsan','age':'20'},
             {'username':'lisi','age':'21'},
             {'username':'wangwu','age':'13'}
             ]
testdata2 = [{'username':'zzzz','age':'25'},
             {'username':'llll','age':'24'},
             {'username':'wwww','age':'12'}
             ]
@ddt.ddt
class Testcase(unittest.TestCase):
    def setUp(self):
        print('start')
    def tearDown(self):
        print('end')
    @ddt.data(*testdata1)
    def test01(self,data):
        print(data)
    @ddt.data(*testdata2)
    def test02(self,data):
        print(data)
    if __name__ == '__main__':
        unittest.main()