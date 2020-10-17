#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 9:33
# @Author  : 李加林
# @FileName: word_tests.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/

import docx
from docx import Document  # 导入库
from workoverflow.fileio import record_csv

path = 'source.docx'  # 文件路径
document = Document(path)  # 读入文件
tables = document.tables  # 获取文件中的表格集
print(tables)
for table in tables:
    for i, row in enumerate(table.rows):  # 读每行
        row_content = []
        for cell in row.cells:  # 读一行中的所有单元格
            c = cell.text
            row_content.append(c)
        record_csv(row_content,"result1.csv")

        # print (row_content) #以列表形式导出每一行数据


