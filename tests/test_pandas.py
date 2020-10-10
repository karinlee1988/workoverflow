#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/9 19:31
# @Author : 李加林
# @FileName : test_pandas.py
# @Software : PyCharm
# @Blog : https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/
# @Personal website : https://karinlee.cn/

import pandas as pd
df1 = pd.read_excel("1.xlsx",header=1)
df2 = pd.read_excel("2.xlsx",header=1)
print(df1,"\n",df2)
print("----------------------------")
# 取df1有而df2没有的
dfmerge_1 = pd.concat([df1, df2, df2], axis = 0, ignore_index=True)
dfmerge_1 = dfmerge_1.drop_duplicates(subset="水果", keep=False)
#取df2有但df1没有的
print(dfmerge_1)
print("----------------------------")
dfmerge_2 = pd.concat([df2, df1, df1], axis = 0, ignore_index=True)
dfmerge_2 = dfmerge_2.drop_duplicates(subset="水果", keep=False)
print(dfmerge_2)
df_all = dfmerge_1.append(dfmerge_2)
print(df_all)

