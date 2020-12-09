#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/9 19:55
# @Author : 李加林
# @FileName : pdfer.py
# @Software : PyCharm
# @Blog : https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/
# @Personal website : https://karinlee.cn/


from fpdf import FPDF
from PIL import Image
from workoverflow.fileio import get_singlefolder_fullfilename

def pic_to_pdf(pdf_filename: str, pic_path: list) -> None:
	"""
	:param pdf_filename : 生成的pdf绝对路径
    :type  pdf_filename : str

    :param pic_path: 由图片的绝对路径组成的列表
    :type  pic_path: list

	"""
	# 打开第一个图片返回一个PIL对象
	cover = Image.open(pic_path[0])
	# 获取第一个图片的宽高参数
	width, height = cover.size
	# 按照上面的宽高参数生成一个空白的fpdf对象
	pdf = FPDF(unit = "pt", format = [width, height])
	# 遍历所有图片
	for pic in pic_path:
		# pdf对象添加新页面并放置图片
		pdf.add_page()
		pdf.image(pic, 0, 0)
	#pdf另存为
	pdf.output(pdf_filename, "F")

pic_list = get_singlefolder_fullfilename(r"D:\MyNutstore\PersonalStudy\Python\WorkOverflow\tests\images",
										 ['.JPG','.jpg','.jpeg','.gif','.png','.PNG'])


if __name__ == '__main__':
	pic_to_pdf("result.pdf",pic_list)