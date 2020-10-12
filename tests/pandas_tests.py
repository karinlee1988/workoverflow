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
df_dict = pd.read_excel("1.xlsx", header=None, sheet_name=None)
for df in df_dict.keys():
    df_each = df_dict[df]
    list_each = df_each.values.tolist()
    for row_index,row in enumerate(list_each,start=1):
        for column_index,e in enumerate(row,start=1):
            # print(row_index,column_index,e)
            if e == "苹果":
                print(list_each[row_index-1])
    # print(list_each)

# df2 = pd.read_excel("2.xlsx",header=1)
# print(df1,"\n",df2)
# print("----------------------------")
# # 取df1有而df2没有的
# dfmerge_1 = pd.concat([df1, df2, df2], axis = 0, ignore_index=True)
# dfmerge_1 = dfmerge_1.drop_duplicates(subset="水果", keep=False)
# #取df2有但df1没有的
# print(dfmerge_1)
# print("----------------------------")
# dfmerge_2 = pd.concat([df2, df1, df1], axis = 0, ignore_index=True)
# dfmerge_2 = dfmerge_2.drop_duplicates(subset="水果", keep=False)
# print(dfmerge_2)
# df_all = dfmerge_1.append(dfmerge_2)
# print(df_all)

# l = [[1,2,3],[4,5,6],[7,8,9]]
#
# for row_index,row in enumerate(l,start=1):
#     for column_index,e in enumerate(row,start=1):
#         print (row_index,column_index,e)

