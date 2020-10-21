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


class DirectoryTree(object):

    def __init__(self,folder_path):
        self.folder_path = folder_path
        self.absolute_path_list = []
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.path_lenth = len(folder_path)
        self.get_absolute_path()
        self.write_workbook()

    def get_absolute_path(self) :
        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                if '.' in file:
                    self.absolute_path_list.append(os.path.join(root, file))

    def write_workbook(self):
        self.ws['A1'].value = self.folder_path
        self.ws['A1'].hyperlink = self.folder_path
        row = 2
        for each_path in self.absolute_path_list:
            relative_path = each_path[self.path_lenth+1:]
            r_list = relative_path.split('\\')
            column = 2
            for e in r_list:
                if '.' not in e:
                    self.ws.cell(column=column, row=row).value = e + '\\'

                else:
                    self.ws.cell(column=column, row=row).value = e
                    self.ws.cell(column=column, row=row).hyperlink = r'' + each_path
                    break

                column += 1
            row += 1
        self.wb.save("tree.xlsx")


if __name__ == '__main__':

    DirectoryTree(r"D:\MyNutstore\PersonalStudy\Python\WorkOverflow\worktools")







