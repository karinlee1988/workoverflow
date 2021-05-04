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

import os
from fpdf import FPDF
from PIL import Image
from PyPDF2 import PdfFileReader, PdfFileWriter,PdfFileMerger
from workoverflow.fileio import get_singlefolder_fullfilename

def pic_to_pdf(pdf_filename: str, pic_path_list: list) -> None:
	"""
	将多个图片合成一个pdf
	（注意：这种方式按照第一张图片的尺寸生成pdf模板，比较适用于图片尺寸相等的情况）

	:param pdf_filename : 生成的pdf绝对路径
    :type  pdf_filename : str

    :param pic_path_list: 由图片的绝对路径组成的列表
    :type  pic_path_list: list

	"""
	# 打开第一个图片返回一个PIL对象
	cover = Image.open(pic_path_list[0])
	# 获取第一个图片的宽高参数
	width, height = cover.size
	# 按照上面的宽高参数生成一个空白的fpdf对象
	pdf = FPDF(unit = "pt",format=(width,height))
	# 遍历所有图片
	for pic in pic_path_list:
		# pdf对象添加新页面并放置图片
		pdf.add_page()
		pdf.image(pic, 0, 0)
	#pdf另存为
	pdf.output(pdf_filename, "F")

def combine_pic_to_pdf(pdf_filename:str,png_files:list) -> None :
	"""
	将多个图片合成一个pdf
	（注意：这种方式按照pic_size将图片进行缩放，适合大小不一的图片）

	:param pdf_filename : 生成的pdf绝对路径
    :type  pdf_filename : str

    :param png_files: 图片的绝对路径列标
    :type  png_files: list
	"""
	# 设置图片默认尺寸，A4默认(96ppi)
	pic_size = (794, 1123)
	sources = []
	output = Image.open(png_files[0])
	png_files.pop(0)
	# 每张图片读取为PIL对象，并进行缩放至默认尺寸
	for file in png_files:
		png_file = Image.open( file )
		w,h = png_file.size
		# 计算缩放比例
		n = w / pic_size[0] if (w / pic_size[0]) >= (h / pic_size[1]) else h / pic_size[1]
		# 缩放图片
		png_file.thumbnail((w / n, h / n))
		# 需调整格式
		if png_file.mode == "RGBA":
			png_file = png_file.convert("RGB")
			sources.append(png_file)
		else:
			sources.append(png_file)
	# 另存为pdf
	output.save(pdf_filename, "pdf", resolution=100.0, save_all=True, append_images=sources)

def merge_pdfs(pdf_file_paths:iter) -> None:
	"""
	将多个pdf文件进行合并

	:param pdf_file_paths: pdf文件列表
	:type pdf_file_paths: iter

	:return: None
	"""
	# 创建一个空白的PdfFileWriter对象
	pdf_writer = PdfFileWriter()
	# 对路径下所有pdf文件进行遍历
	for pdf_file_path in pdf_file_paths:
		# 读取为PdfFileReader对象
		pdf_reader = PdfFileReader(pdf_file_path)
		# 遍历每个pdf文件的页面
		for page in range(pdf_reader.getNumPages()):
			# 将每页添加到writer对象
			pdf_writer.addPage(pdf_reader.getPage(page))
	# 写入合并的pdf
	with open('mergedx.pdf', 'wb') as out:
		pdf_writer.write(out)

if __name__ == '__main__':
	path = get_singlefolder_fullfilename(r"D:\MyNutstore\PersonalStudy\Python\WorkOverflow\tests\images",[".pdf"])
	path.sort()
	merge_pdfs(path)






