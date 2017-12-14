#!/usr/bin/python
# -*- coding:utf-8 -*-  

from bs4 import BeautifulSoup 
import re
import urllib2
import time
import win32api,win32con  
import chardet

class check_loop():
	url="http://bbs.macd.cn/forum.php?mod=viewthread&tid=2820739&page=9999&authorid=3833326"
	soup=0
	sell_cnt=0
	sell_str=""
	buy_cnt=0
	buy_str=""
	msg_str=""
	time_str=""
	msg_cnt=0
	details = ""

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
		self.save_file()
		self.soup = BeautifulSoup(self.details,"html.parser")
		self.msg_str,self.time_str=self.get_msg()
		
		self.sell_str=self.check_sell()
		self.sell_cnt=len(self.sell_str)
		
		self.buy_str=self.check_buy()
		self.buy_cnt=len(self.buy_str)

	def get_msg(self):
		time_str=""
		msg_str=""
		list_str=self.soup.find_all('div',id=re.compile("post_[0-9]+"))
		self.msg_cnt = len(list_str)
		for str in list_str:
			time=str.find_all('em')
			time_str=time_str + u"\n" + time[2].get_text()

			speech=str.find_all('td',class_="t_f")
			quote=speech[0].find_all('div',class_="quote")
			print time[2].get_text()
			if len(quote):
				print "start"
				for child in speech[0].stripped_strings:
					print(child)
					print "111111111"
				print "end"
				#print '222',speech[0].contents
#				text = quote[0].find_next_sibling('br').get_text()
#				print '222',text
#				text=text.split("\n")
#				msg_str += '\n' + text[0]
#				print '3333',text
			else:
				msg_str += '\n' + speech[0].get_text()
				try:
					print "4444",speech[0].get_text()
				except ZeroDivisionError,e:
					print(e.message)
				
			strreg = re.compile('\n\n+')
			msg_str = strreg.sub('\n',msg_str)
		return msg_str,time_str
	
	def check_pattern(self,pattern):
		reg = re.compile(pattern,re.M)
		list_str = re.findall(reg, self.msg_str)
		return list_str
	
	def check_sell(self):
		pattern = ur'([\u4e00-\u9fa5]*\u5356[^\n]+)'
		return self.check_pattern(pattern)
		
	def check_buy(self):
		pattern = ur'([\u4e00-\u9fa5]*\u4e70[^\n]+)'
		return self.check_pattern(pattern)

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
		#print loop.msg_str
		try:
			loop.print_list(loop.msg_str)
		except ZeroDivisionError,e:
			print(e.message)
		
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
