#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/11 23:44
# @Author : 李加林
# @FileName : fileio_tests.py
# @Software : PyCharm
# @Blog : https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/
# @Personal website : https://karinlee.cn/

import os
# def findAllFile(base):
#     l = []
#     for root, ds, fs in os.walk(base):
#         for f in fs:
#             fullname = os.path.join(root, f)
#             l.append(fullname)
#
#     return l
#
f = r"D:\MyNutstore\PersonalStudy\Python\WorkOverflow"
# print(findAllFile(f))
print(os.path.splitext(f))