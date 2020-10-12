#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 16:49
# @Author  : 李加林
# @FileName: search.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/

"""
本模块用于批量查找搜索数据
"""
import pandas as pd
import openpyxl
from workoverflow.fileio import get_allfolder_fullfilename,record_csv

class ElementSearch(object):
    """
    用于某个数据(或excel表中某列数据)在一堆其他excel文件中查找,找出对应行后进行记录.

    """

    def __init__(self, source_path, element) :

        self.source_path = source_path
        self.element = element

    @staticmethod
    def transfer(x):
        return '\t' + str(x)


    def search_element(self):
        # 获取文件名
        file_list = get_allfolder_fullfilename(self.source_path, [".xlsx", ])
        record_csv(['文件路径','工作表名','行号','列号'], self.element + "_搜索结果.csv")
        # print(len(file_list))
        for filename in file_list:
            wb = openpyxl.load_workbook(filename)
            for sheet in wb:
                for row in range(1, sheet.max_row + 1):
                    for column in range(1, sheet.max_column + 1):
                        if sheet.cell(row=row, column=column).value == self.element:
                            # row_list 存放查找出来服刑人员数据行
                            row_list = [filename,sheet.title,row,column,]
                            for column_result in range(1,sheet.max_column+1):
                                # row_list 添加查找数据所在行的值（值统一转为str）。\t 是为了添加身份证等长数字后，
                                # 写入csv时不会出现科学计数法现象。
                                row_list.append('\t' + str(sheet.cell(row=row, column=column_result).value))

                            # 数据写入
                            record_csv(row_list, self.element + "_搜索结果.csv")
                            break


    def search_element_plus(self):
        file_list = get_allfolder_fullfilename(self.source_path, [".xlsx",".xls" ])
        record_csv(['文件路径', '工作表名', '行号', '列号'], self.element + "_搜索结果.csv")
        for filename in file_list:
            df_dict = pd.read_excel(filename, header=None, sheet_name=None)
            for sheetname in df_dict.keys():
                df_sheet = df_dict[sheetname]
                list_sheet = df_sheet.values.tolist()
                for row_index, row in enumerate(list_sheet, start=1):
                    for column_index, e in enumerate(row, start=1):
                        # print(row_index,column_index,e)
                        if e == self.element:
                            list_content = list(map(self.transfer,list_sheet[row_index-1]))
                            row_list = [filename, sheetname, row_index,column_index] + list_content
                            record_csv(row_list,self.element + "_搜索结果.csv")
                            break


if __name__ == '__main__':
    s = ElementSearch(r"D:\MyNutstore\PersonalStudy\Python\WorkOverflow\tests\source","440228196608156369")
    s.search_element_plus()

