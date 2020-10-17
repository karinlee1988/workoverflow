#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/17 12:26
# @Author : 李加林
# @FileName : split_workbook.py
# @Software : PyCharm
# @Blog : https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/
# @Personal website : https://karinlee.cn/

"""
将excel工作薄中某工作表按列字段拆分
"""
from workoverflow.exceler import split_workbook_by_column
import PySimpleGUI as sg

class WorkbookSplit(object):
    """
    可视化界面
    """
    def __init__(self):
        # 设置pysimplegui主题，不设置的话就用默认主题
        # sg.ChangeLookAndFeel('Purple')
        # 定义2个常量，供下面的layout直接调用，就不用一个个元素来调字体了
        # 字体和字体大小
        self.FONT = ("微软雅黑", 16)
        # 可视化界面上元素的大小
        self.SIZE = (20,1)
        # 界面布局
        self.layout = [
            # sg.Image()插入图片，支持gif和png
            [sg.Image(filename="images/pq1.png",pad=(120,0))],
            # sg.Text()显示文本
            [sg.Text('',font=self.FONT,size=self.SIZE)],
            # sg.Input()是输入框
            [sg.Text('请选择要拆分的文件：',font=self.FONT, size=(30,1))],
            [sg.Input('     (*.xls,*.xlsx文件)      ',key="_FILE_",readonly=True,size=(36,1),font=self.FONT),
                sg.FileBrowse(button_text='选择文件',size=(10,1),font=self.FONT)],
            [sg.Text(' 请输入sheet页序号：',font=self.FONT,size=self.SIZE),
                sg.Input(key='_SHEET_',font=self.FONT,size=(10,1))],
            [sg.Text(' 请输入表头行数:  ', font=self.FONT, size=self.SIZE),
             sg.Input(key='_TITLE_', font=self.FONT, size=(10,1))],
            [sg.Text(' 请输入列号:  ', font=self.FONT, size=self.SIZE),
             sg.Input(key='_COLUMN_', font=self.FONT, size=(10,1))],
            [sg.Text('')],
            [sg.Btn('开始拆分', key='_SUMMIT_', font=("微软雅黑", 16), size=(20, 1)),
             sg.Input(key='_RESULT_',readonly=True,size=(10,1),font=self.FONT)],
        ]
        # 创建窗口，引入布局，并进行初始化
        # 创建时，必须要有一个名称，这个名称会显示在窗口上
        self.window = sg.Window('按列拆分excel工作表by李加林', layout=self.layout, finalize=True)

    # 窗口持久化
    def run(self):
        # 创建一个事件循环，否则窗口运行一次就会被关闭
        while True:
            # 监控窗口情况
            event, value = self.window.Read()
            # 当获取到事件时，处理逻辑（按钮绑定事件，点击按钮即触发事件）
            if event == '_SUMMIT_':
                file = value['_FILE_']
                sheet = int(value['_SHEET_']) - 1
                title = int(value['_TITLE_'])
                column = int(value['_COLUMN_']) - 1
                # 调用函数拆分表格
                split_workbook_by_column(file,sheet,title,column)
                # 函数完成后返回处理完成标志到窗口界面上
                self.window.Element("_RESULT_").Update("处理完成！")
            # 如果事件的值为 None，表示点击了右上角的关闭按钮，则会退出窗口循环
            if event is None:
                break
        self.window.close()

if __name__ == '__main__':
    app = WorkbookSplit()
    app.run()