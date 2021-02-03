#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/3 13:26
# @Author : 李加林
# @FileName : oop_tests.py
# @Software : PyCharm
# @Blog : https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/
# @Personal website : https://karinlee.cn/

class Base(object):

    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.c = 10

    def sum(self):
        print(self.a + self.b)

    def retur(self):
        return self.b


class New(Base):

    def __init__(self,x,y,c):
        super(New, self).__init__(x,y)
        self.c = c

    @property
    def muti(self):
        return self.b * self.c




class Over(Base):

    def __init__(self,*args):
        super(Over, self).__init__(*args)
        self.b = 33


over = Over(1,2)
print(over.retur())

