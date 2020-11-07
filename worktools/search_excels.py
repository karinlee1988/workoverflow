#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/7 21:15
# @Author : 李加林
# @FileName : search_excels.py
# @Software : PyCharm
# @Blog : https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/
# @Personal website : https://karinlee.cn/

"""
在多个excel工作薄内找出指定元素的行
"""

import PySimpleGUI as sg
from workoverflow.search import ElementSearch


class ExcelsSearcher(object):

    def __init__(self):
        # 设置pysimplegui主题，不设置的话就用默认主题
        sg.ChangeLookAndFeel('GreenTan')
        # 定义2个常量，供下面的layout直接调用，就不用一个个元素来调字体了
        # 字体和字体大小
        self.FONT = ("微软雅黑", 16)
        # 可视化界面上元素的大小
        self.SIZE = (20, 1)
        # 界面布局
        self.layout = [
            # sg.Image()插入图片，支持gif和png
            [sg.Image(filename="images/qz.png", pad=(130, 0))],
            # sg.Text()显示文本
            [sg.Text('', font=self.FONT, size=self.SIZE)],
            # sg.Input()是输入框
            [sg.Text('请选择包含多个excel文件的文件夹：', font=self.FONT, size=(30, 1))],
            [sg.Input(key="_FOLDER_", readonly=True, size=(36, 1), font=self.FONT),
             sg.FolderBrowse(button_text='选择文件夹', size=(10, 1), font=self.FONT)],
            [sg.Text('')],
            [sg.Text('请输入要搜索的元素（需完全匹配）：', font=("微软雅黑", 16), size=(28, 1)),
             sg.Input(key='_ELEMENT_', size=(10, 1), font=self.FONT)],
            [sg.Btn('开始搜索', key='_SEARCH_', font=("微软雅黑", 16), size=(28, 1)),
             sg.Input(key='_RESULT_', readonly=True, size=(10, 1), font=self.FONT)],
        ]
        # 创建窗口，引入布局，并进行初始化
        # 创建时，必须要有一个名称，这个名称会显示在窗口上
        self.window = sg.Window('excel批量搜索by李加林', layout=self.layout, finalize=True)

    # 窗口持久化
    def run(self):
        # 创建一个事件循环，否则窗口运行一次就会被关闭
        while True:
            # 监控窗口情况
            event, value = self.window.Read()
            # 当获取到事件时，处理逻辑（按钮绑定事件，点击按钮即触发事件）
            if event == '_SEARCH_':
                folder = value['_FOLDER_']
                element = value['_ELEMENT_']
                # 生成目录树
                search = ElementSearch(source_path=folder,element=element)
                search.search_element_plus()
                # 函数完成后返回处理完成标志到窗口界面上
                self.window.Element("_RESULT_").Update("处理完成！")
            # 如果事件的值为 None，表示点击了右上角的关闭按钮，则会退出窗口循环
            if event is None:
                break
        self.window.close()

if __name__ == '__main__':
    app = ExcelsSearcher()
    app.run()
