#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 11:57
# @Author  : 李加林
# @FileName: directory_tree.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/

import os
import openpyxl


def get_fullfilename(folder_path:str) -> list:

    filename_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if '.' in file:
                filename_list.append(os.path.join(root, file))
    return filename_list

wb = openpyxl.Workbook()
ws = wb.active
row = 2
path = r'D:\MyNutstore\PersonalStudy\Python\WorkOverflow\worktools'
l = len(path) + 1
ws['A1'].value = path
for filename in get_fullfilename(path):
    r_filename = filename[l:]
    r_list = r_filename.split('\\')
    c = 2
    for e in r_list:
        if '.' not in e:
            ws.cell(column=c,row=row).value = e+'\\'
        else:
            ws.cell(column=c, row=row).value = e
        c+=1
    row+=1
wb.save("tree.xlsx")