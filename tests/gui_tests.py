#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/12 23:54
# @Author : 李加林
# @FileName : gui_tests.py
# @Software : PyCharm
# @Blog : https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/
# @Personal website : https://karinlee.cn/


import PySimpleGUI as sg
def cookbook():
    sg.ChangeLookAndFeel('GreenTan')
    form = sg.FlexForm('Everything bagel', default_element_size=(40, 1))
    column1 = [[sg.Text('Column 1', background_color='#d3dfda', justification='center', size=(10,1))],
    [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
    [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
    [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]
    layout = [
    [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25))],
    [sg.Text('Here is some text.... and a place to enter text')],
    [sg.InputText('This is my text')],
    [sg.Checkbox('My first checkbox!'), sg.Checkbox('My second checkbox!', default=True)],
    [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
    [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
    sg.Multiline(default_text='A second multi-line', size=(35, 3))],
    [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 3)),
    sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
    [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
    sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
    sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
    sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
    sg.Column(column1, background_color='#d3dfda')],
    [sg.Text('_'  * 80)],
    [sg.Text('Choose A Folder', size=(35, 1))],
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
    sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Submit(), sg.Cancel()]
    ]
    button, values = form.Layout(layout).Read()
    sg.Popup(button, values)

# -----------------------------------------------------------------

def simple():
    layout = [
        [sg.Text('账号',font=("Helvetica", 25)), sg.Input(key='_USER_',font=("Helvetica", 25))],
        [sg.Text('密码'), sg.Input(password_char='*', key='_PWD_')],
        [sg.Btn('提交', key='_LOGIN_')]
    ]



    # 创建窗口，引入布局，并进行初始化
    # 创建时，必须要有一个名称，这个名称会显示在窗口上
    window = sg.Window('登录', layout=layout, finalize=True,default_button_element_size=(300,5))

    while True:  # 创建一个事件循环，否则窗口运行一次就会被关闭
        event, value = window.Read()  # event, value 的值分别是 _LOGIN_ {'_USER_': 'admin', '_PWD_': '123'}
        # print(event, value)  # 可以打印一下看看变量的内容
        if event is None:   # 如果事件的值为 None，表示点击了右上角的关闭按钮
            break
        if event == '_LOGIN_':  # 当获取到事件时，处理逻辑
            user = value['_USER_']
            password = value['_PWD_']
            if user == 'admin' and password == '123':
                sg.popup('登录成功!')
            else:
                sg.popup('登录失败!', text_color='red')


    window.close()

if __name__ == '__main__':
    cookbook()