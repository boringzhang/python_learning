#!/usr/bin/python
# -*- coding:utf-8 -*-  

import re
import urllib,urllib2
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
		try:
			html=urllib2.urlopen(self.url, timeout=60).read()
		except Exception,e:
			print 'exp msg',str(e)
    
		if (html=="") :
			return
		
		self.details = html.decode("gbk")
		
		self.quote_str=self.check_quote()
		
		self.sell_str=self.check_sell()
		self.sell_str=self.remove_quote(self.sell_str)
		self.sell_cnt=len(self.sell_str)
		
		self.buy_str=self.check_buy()
		self.buy_str=self.remove_quote(self.buy_str)
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

sell_cnt = 0
buy_cnt = 0
msg_cnt = 0
while 1 :
	loop.refresh()
	if(msg_cnt!=loop.msg_cnt):
		win32api.MessageBox(0, "new msg", "new msg",win32con.MB_OK) 
		print "new msg",msg_cnt,loop.msg_cnt
		msg_cnt = loop.msg_cnt
		
	if(sell_cnt!=loop.sell_cnt):
		win32api.MessageBox(0, "new msg 1", "new msg",win32con.MB_OK) 
		print "new sell",sell_cnt,loop.sell_cnt
		loop.print_list(loop.sell_str)
		sell_cnt = loop.sell_cnt
	
	if(buy_cnt!=loop.buy_cnt):
		win32api.MessageBox(0, "new msg 2", "new msg",win32con.MB_OK) 
		print "new buy",buy_cnt,loop.buy_cnt
		loop.print_list(loop.buy_str)
		buy_cnt = loop.buy_cnt
	
	time.sleep(30)
