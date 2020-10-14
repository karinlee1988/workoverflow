#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/13 18:40
# @Author : 李加林
# @FileName : calculate_months.py
# @Software : PyCharm
# @Blog : https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/
# @Personal website : https://karinlee.cn/

import PySimpleGUI as sg

FONT = ("微软雅黑", 20)
SIZE = (10,1)

def calc(begin_month,end_month):
    full_month = (int(end_month[0:4]) - int(begin_month[0:4])) * 12 + (
                int(end_month[4:6]) - int(begin_month[4:6])) + 1

    return full_month


layout = [
    [sg.Text("社保月数参保计算器by 英德社保李加林 2020.10.13",font=("微软雅黑",12))],
    [sg.Text('',font=FONT,size=SIZE)],
    [sg.Text('开始日期',font=FONT,size=SIZE), sg.Input(key='_BEGIN_',font=FONT,size=SIZE)],
    [sg.Text('结束日期',font=FONT,size=SIZE), sg.Input(key='_END_',font=FONT,size=SIZE)],
    [sg.Text('',font=FONT,size=SIZE)],
    [sg.Btn('开始计算', key='_SUMMIT_',font=FONT,size=(10,2)),sg.Input(key='_VALUE_',font=FONT,size=SIZE)],
]

window = sg.Window('计算器', layout=layout, finalize=True)
while True:  # 创建一个事件循环，否则窗口运行一次就会被关闭
    event, value = window.Read()
    if event == '_SUMMIT_':
        begin = value['_BEGIN_']
        end = value['_END_']
        result = calc(begin,end)
        window.Element("_VALUE_").Update(result)


    if event is None:   # 如果事件的值为 None，表示点击了右上角的关闭按钮
        break
window.close()