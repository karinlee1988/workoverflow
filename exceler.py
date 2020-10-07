#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/6 14:16
# @Author : 李加林
# @FileName : exceler.py
# @Software : PyCharm
# @Blog : https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/

"""
本模块用于对excel表格进行各种处理操作
"""
import pandas as pd

def split_workbook_by_column(workbook_path,sheet_index,title_index,column_index):
    """
    将一个excel工作薄中指定的工作表，按列字段进行拆分，拆分后的多个excel表格分别以列字段命名

    @param workbook_path: 要拆分的工作薄文件路径
    @type workbook_path:  str

    @param sheet_index: 要拆分的工作薄的工作表序号（从0开始）
    @type sheet_index:  int

    @param title_index: 拆分后表头的行数（从1开始）
    @type title_index:  int

    @param column_index: 根据某列的列索引号进行拆分（从0开始）
    @type column_index: int
    """
    # 将要拆分的工作薄读取为dataframe对象
    workbook_df = pd.read_excel(io=workbook_path,sheet_name=sheet_index,header=None)
    # 获取工作薄的表头部分和数据部分，生成2个dataframe
    workbook_header_df = workbook_df[0:title_index]
    workbook_source_df = workbook_df[title_index:]
    # 对单位列去重复,返回一个numpy数组col，包含所有不重复的列字段
    col = workbook_source_df.iloc[:,column_index].unique()
    # 遍历数组
    for x in col:
        # 循环，得到每一个列字段的dataframe
        each_workbook_source_df = workbook_source_df[workbook_source_df.iloc[:,column_index] == x]
        # 拼接dataframe，表头部分与数据部分
        each_workbook_df = workbook_header_df.append(each_workbook_source_df)
        # 将得到的dataframe保存成Excel格式，文件名为列字段。
        each_workbook_df.to_excel(x + '.xlsx', index=False,header=False)

if __name__ == '__main__':
    split_workbook_by_column("示例.xlsx",0,2,3)