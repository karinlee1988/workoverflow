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
from openpyxl.styles import Font
# from openpyxl.utils import get_column_letter

"""
从一个文件夹路径生成目录树（常用格式文件会被写入），并写入excel文档（带超链接）
"""

class DirectoryTree(object):
    """
    目录树生成并写入excel
    """
    def __init__(self, folder_path):
        """
        :param folder_path: 文件夹路径
        :type folder_path: str
        """
        self.folder_path = folder_path
        # 创建空列表用于存放文件夹下所有文件的绝对路径
        self.absolute_path_list = []
        # 自定义常见文件类型，文件夹里面文件的类型符合才会被写入excel
        self.filetype = ('.doc',
                         '.docx',
                         '.xls',
                         '.xlsx',
                         '.ppt',
                         '.pptx',
                         '.pdf',
                         '.jpg',
                         '.jpeg',
                         '.png',
                         '.bmp',
                         '.gif',
                         '.txt',
                         '.csv',
                         '.md',
                         '.py',
                         '.mp4',
                         '.avi',
                         '.mkv',
                         '.mp3',
        )
        # 创建工作薄用于写目录树
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        # 计算文件夹路径长度，用于后续计算相对路径
        self.path_lenth = len(folder_path)
        # 执行
        self.get_absolute_path()
        self.write_workbook()

    def get_absolute_path(self) :
        """
        获取文件夹下所有绝对路径文件名
        """
        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                if os.path.splitext(file)[1] in self.filetype:
                    self.absolute_path_list.append(os.path.join(root, file))

    def write_workbook(self):
        """
        按步骤将文件名拆分并写入excel，形成目录树
        """
        # 设置字体类型（该字体类型为添加下划线）
        font = Font(underline='single')
        self.ws['A1'].value = self.folder_path+'\\'
        # 设置超链接
        self.ws['A1'].hyperlink = self.folder_path
        # 应用字体
        self.ws['A1'].font = font
        # row,column 是临时的变量，用于逐行或逐列按需写入数据用
        row = 2
        for each_path in self.absolute_path_list:
            # 计算相对路径，并按文件夹深度进行拆分
            relative_path = each_path[self.path_lenth+1:]
            r_list = relative_path.split('\\')
            column = 2
            for e in r_list:
                # 判断拆分后的路径是文件夹还是文件
                if os.path.splitext(e)[1] not in self.filetype :
                    self.ws.cell(column=column, row=row).value = e + '\\'
                else:
                    self.ws.cell(column=column, row=row).value = e
                    # 添加超链接与下划线
                    self.ws.cell(column=column, row=row).hyperlink = r'' + each_path
                    self.ws.cell(column=column, row=row).font = font
                column += 1
            row += 1
        self.wb.save("tree.xlsx")
        # 保存后直接打开excel文件
        # os.startfile("tree.xlsx")

if __name__ == '__main__':
    DirectoryTree(r"D:\MyNutstore\工作文档\01_工作项目\01_社保基金安全@[广东省人社厅,清远市人社局,清远市社保局,英德市人社局]")







