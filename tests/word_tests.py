#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 9:33
# @Author  : 李加林
# @FileName: word_tests.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/

import win32com.client as win32
import os
word = win32.gencache.EnsureDispatch('Word.Application')
#启动word对象应用
word.Visible = False
path = r'D:\MyNutstore\工作文档\01_工作项目\10_群众来信答复和投诉答复'
files = []
for filename in os.listdir(path):
    filename = os.path.join(path,filename)
    files.append(filename)
#新建合并后的文档
output = word.Documents.Add()
for file in files:
    output.Application.Selection.InsertFile(file)#拼接文档
#获取合并后文档的内容
doc = output.Range(output.Content.Start, output.Content.End)
output.SaveAs(r'D:\MyNutstore\工作文档\01_工作项目\10_群众来信答复和投诉答复\result.docx') #保存
output.Close()