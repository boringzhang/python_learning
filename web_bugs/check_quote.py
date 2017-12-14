#!/usr/bin/python
# -*- coding:utf-8 -*-  

import re
import urllib
import time
import win32api,win32con  

class check_loop():
	url="http://bbs.macd.cn/forum.php?mod=viewthread&tid=2820739&page=9999&authorid=3833326"
	details = ""
	sell_cnt=0
	sell_str=""
	buy_cnt=0
	buy_str=""
	msg_cnt=0
	
	quote_str=""
	def __init__(self):
		self.refresh()
	
	def refresh(self):
		html=urllib.urlopen(self.url).read()
		self.details = html.decode("gbk")
		
		self.quote_str=self.check_quote()
		
		self.sell_str=self.check_sell()
		#self.sell_str=self.remove_quote(self.sell_str)
		self.sell_cnt=len(self.sell_str)
		
		self.buy_str=self.check_buy()
		#self.buy_str=self.remove_quote(self.buy_str)
		self.buy_cnt=len(self.buy_str)
		

		
		self.msg_cnt=len(self.check_time())

	def check_pattern(self,pattern):
		reg = re.compile(pattern)
		list_str = re.findall(reg,self.details)
		return list_str
		
	def check_sell(self):
		pattern = ur'([\u4e00-\u9fa5]*\u5356[^<]+)'
		return self.check_pattern(pattern)
		
	def check_buy(self):
		pattern = ur'([\u4e00-\u9fa5]*\u4e70[^<]+)'
		return self.check_pattern(pattern)
		
	def check_time(self):
		pattern = ur'(\u53d1\u8868[^<]+)'
		return self.check_pattern(pattern)

	def check_quote(self):
		pattern = ur'(.*blockquote.*)'
		return self.check_pattern(pattern)

	def remove_quote(self,list_str):
		for	str in list_str:
			for quote in self.quote_str:
				if str in quote:
					list_str.remove(str)
		return list_str

	def print_list(self,list_str):
		for	str in list_str:
			print str
			
	def save_file(self):
		f=open("test.html","w+")
		f.write(self.details.encode('utf8'))
		f.close()


loop=check_loop()
#loop.refresh()
#loop.save_file()

print loop.print_list(loop.sell_str)

print loop.print_list(loop.buy_str)