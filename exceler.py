#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/6 14:16
# @Author : 李加林
# @FileName : exceler.py
# @Software : PyCharm
# @Blog : https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/

import pandas as pd

def split_workbook_by_column_field(workbook_path,sheet_index,title_index,column_index):

    wb = pd.read_excel(io=workbook_path,sheet_name=sheet_index,header=title_index)  # 打开工作薄
    col = wb.iloc[:,column_index].unique()  # 对单位列去重复
    for x in col:
        child_wb = wb[wb.iloc[:,column_index] == x]  # 循环，得到每一个单位列表，
        child_wb.to_excel(x + '.xlsx', index=False)  # 将得到的表保存成Excel格式

if __name__ == '__main__':
    split_workbook_by_column_field("示例.xlsx",0,1,3)