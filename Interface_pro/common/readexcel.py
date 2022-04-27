import xlrd


class ReadExcel:

    # 初始化时传入文件名称，获取对应文件
    def __init__(self, file_name, sheetname):
        # 获取文件
        self.data = xlrd.open_workbook(file_name)
        # 获取对应Sheet，这里默认设置为Sheet1
        self.table = self.data.sheet_by_name(sheetname)

        # 初始化时获取行数和列数
        self.row_nums = self.table.nrows
        self.col_nums = self.table.ncols

    # 读取文件内容
    def read_excel(self):
        if self.row_nums > 1:
            # 获取第一行的数据(表格的title作为key)
            keys = self.table.row_values(0)
            # 新建一个用于存放表格数据的listApiData
            listApiData = []
            for row in range(1, self.row_nums):
                values = self.table.row_values(row)
                api_dict = dict(zip(keys, values))
                listApiData.append(api_dict)
            return listApiData
        else:
            print("该表格是空的，请检查表格数据")
            return None





