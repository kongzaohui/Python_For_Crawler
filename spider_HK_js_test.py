# -*- coding: utf-8 -*-
import re
from urllib.parse import urlencode
import requests
from requests.exceptions import ConnectionError
import json
from json.decoder import JSONDecodeError
import urllib.request
from furl import furl
import datetime
import ast
import os, errno

#获取目标股票代码
def get_stock_no():

	# 文件的相对路径
	txt_filename = 'C:\\Users\\38964\Desktop\codes\stockNo_HK_new.txt'

	# 打开文件
	file_obj = open(txt_filename, 'r', encoding='utf-8')

	# 逐行读取
	#stockNos = file_obj.readlines()
	stockNos = file_obj.read().splitlines()

	return stockNos

def get_page_index():
	#print("get_page_index begin...stockNo--->")
	#print(stockNo)
	#stockNo=stockNo[:5]

	#if(stockNo<'08000' or stockNo=='80737'):
	url = 'http://www.cninfo.com.cn//disclosure/fulltext/stocks/hkmblatest/00182.js?'
	#else:
	url2 = 'http://www.cninfo.com.cn//disclosure/fulltext/stocks/hkgemlatest/00182.js?'

	current_time = datetime.datetime.now().strftime('%Y%m%d%H%M')
	params ={
		'ver': current_time
	}
	_url = furl(url).add(params).url
	#print(_url)

	try:
		response = requests.get(_url)
		if response.status_code == 200:
			#print(response.text)
		   # print("get_page_index over...")
			return response.text
		return None
	except ConnectionError:
		#print('Error occurred')
		#print("get_page_index over...")
		return None

def parse_page_index(html):
	#print("parse_page_index begin...")
	#html = get_page_index()
	html = html[html.find('[')+1:html.rfind(']')]
	html = ast.literal_eval(html)
	print(html)

	pattern1 = re.compile(r".*年.?报\(?(?!.*报告)\)?")
	pattern2 = re.compile(r".*年.?报(?!.*通)")
	basePdfUrl = "http://www.cninfo.com.cn/"

	i = 0
	for index,myList in enumerate(html):
		html_text = html[index][2].encode('latin1').decode('gbk')
		#print('html_text--->')
		#print(html_text)

		match1 = pattern1.match(html_text)
		match2 = pattern2.match(html_text)

		if match1 and match2:
			i+=1
			#print(html[0])
			PdfUrl = basePdfUrl + html[index][1]
			#print(PdfUrl)
			#print("parse_page_index over...")
			yield PdfUrl
			#print(html[0][2].encode('latin1').decode('gbk'))

	if(i==0):
		stockNo = html[index][0]
		# 保存到文件中
		with open('C:\\Users\\38964\Desktop\codes\_Nothing_HK.txt', 'a', encoding='utf-8') as f:
			f.write('{}\n'.format(stockNo))

		#return None

def download_file(url):
	file_name = url[url.find('/120') + 1:url.find('PDF') + 6]
	#print(file_name)

	folder_path = 'D:\\python-projects\HK_PDF\\00182\\'
	#stockNo[0:-1]
	try:
		os.makedirs(folder_path)
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise

	urllib.request.urlretrieve(url, folder_path + file_name)

def main():
	html = get_page_index()
	PdfUrl = parse_page_index(html)
	for url in PdfUrl:
		download_file(url)

if __name__=='__main__':
	#stockNos = get_stock_no()
	#for stockNo in stockNos:
	main()
		#for pageNum in range(10):


