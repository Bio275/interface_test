import os


def new_report(testreport):
    # 返回指定的文件夹包含的文件或文件夹的名字的列表
    lists = os.listdir(testreport)
    # 以修改时间（getmtime）从小到大排序
    lists.sort(key=lambda fn: os.path.getmtime(testreport+"\\"+fn))
    # 取最后一个值（最新的一个报告）
    new_file = os.path.join(testreport, lists[-1])
    return new_file
