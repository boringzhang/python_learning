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
	def refresh(self):
		html=urllib.urlopen(self.url).read()
		self.details = html.decode("gbk").encode("utf-8")
		self.sell_str=self.check_sell()
		self.sell_cnt=len(self.sell_str)
		self.buy_str=self.check_buy()
		self.buy_cnt=len(self.buy_str)

		self.msg_cnt=len(self.check_time())

	def check_pattern(self,pattern):
		reg = re.compile(pattern)
		list_str = re.findall(reg,self.details)
		return list_str
		
	def check_sell(self):
		#pattern = r'([.]*\xe5\x8d\x96\xe5\x87\xba[^<]+)'
		pattern = r'([.]*\xe5\x8d\x96[^<]+)'
		return self.check_pattern(pattern)
		
	def check_buy(self):
		#pattern = r'([.]*\xe4\xb9\xb0\xe5\x85\xa5[^<]+)'
		pattern = r'([.]*\xe4\xb9\xb0[^<]+)'
		return self.check_pattern(pattern)
		
	def check_time(self):
		pattern = r'(\xe5\x8f\x91\xe8\xa1\xa8\xe4\xba\x8e[^<]+)'
		return self.check_pattern(pattern)

	def check_quote(self):
		pattern = r'<div class="quote">.+[</blockquote>]'
		return self.check_pattern(pattern)

	def print_list(self,list_str):
		for	str in list_str:
			print str.decode('utf-8')


loop=check_loop()

sell_cnt = 0
buy_cnt = 0
msg_cnt = 0
while 1 :
	loop.refresh()
	if(msg_cnt!=loop.msg_cnt):
		win32api.MessageBox(0, "new msg", "new msg",win32con.MB_OK) 
		print "new msg"
		msg_cnt = loop.msg_cnt
		
	if(sell_cnt!=loop.sell_cnt):
		win32api.MessageBox(0, "new msg 1", "new msg",win32con.MB_OK) 
		print "new sell"
		loop.print_list(loop.sell_str)
		sell_cnt = loop.sell_cnt
	
	if(buy_cnt!=loop.buy_cnt):
		win32api.MessageBox(0, "new msg 2", "new msg",win32con.MB_OK) 
		print "new buy"
		loop.print_list(loop.buy_str)
		buy_cnt = loop.buy_cnt
	
	time.sleep(5)
