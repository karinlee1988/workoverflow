#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/25 21:20
# @Author : 李加林
# @FileName : worder.py
# @Software : PyCharm
# @Blog : https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/
# @Personal website : https://karinlee.cn/

"""
本模块用于对word文档进行各种处理操作
"""
import docx
from docx import Document

def replace_text(doc:[Document],old_text:str, new_text:str) -> None:
    """
    将某个文档的某个词进行替换（可以制作模板后用于套打）

    :param doc:   要处理的文件
    :type doc: class Document

    :param old_text:  旧的词
    :type old_text: str

    :param new_text: 新的词
    :type new_text: str

    :return: None
    """
    for p in doc.paragraphs:
        if old_text in p.text:
            inline = p.runs
            for i in inline:
                if old_text in i.text:
                    text = i.text.replace(old_text, new_text)
                    i.text = text
