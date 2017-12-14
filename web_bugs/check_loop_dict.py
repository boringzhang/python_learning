#!/usr/bin/python
# -*- coding:utf-8 -*-  

from bs4 import BeautifulSoup 
import re
import urllib2
import time
import win32api,win32con  
import chardet
import sys
#reload(sys)
#sys.setdefaultencoding('gb2312')


class check_loop():
	url="http://bbs.macd.cn/forum.php?mod=viewthread&tid=2820739&page=9999&authorid=3833326"
	soup=0
	details = ""
	sell_cnt=0
	buy_cnt=0
	msg_cnt=0

	msg_list = []
	sell_list = []
	buy_list = []

	def __init__(self):
		self.refresh()
	
	def refresh(self):
		try:
			html=urllib2.urlopen(self.url, timeout=60).read()
		except Exception,e:
			print 'exp msg',str(e)
			return

		if (html=="") :
			return
		self.details = html.decode("gbk",'ignore')
		#self.save_file()
		self.soup = BeautifulSoup(self.details,"html.parser")
		#print(self.soup.prettify())

		self.msg_list=self.get_msg()
		self.msg_cnt=len(self.msg_list)
		
		self.sell_list=self.check_sell()
		self.sell_cnt=len(self.sell_list)
		
		self.buy_list=self.check_buy()
		self.buy_cnt=len(self.buy_list)

	def get_msg(self):
		msg_list=[]
		list_str=self.soup.find_all('div',id=re.compile("post_[0-9]+"))

		cnt=0
		for str in list_str:
			msg_set={}
			time=str.find_all('em')
			msg_set['time']=time[2].get_text()
			
			speech=str.find_all('td',class_="t_f")
			quote=speech[0].find_all('div',class_='quote')
			if len(quote):
				msgs = quote[0].next_sibling.next_sibling
			else:
				msgs = speech[0].contents[0]
				
			try:
				msgs.encode('gbk')
			except (UnicodeEncodeError),e:
				print "UnicodeEncodeError"
				msgs = "\n##################"
				
			if msgs[0]=='\n':
				msgs = msgs[1:]
			strreg = re.compile('\n[\n]+')#delete empty lines
			msgs = strreg.sub('\n',msgs)
			#print msgs
			msg_set['message']=msgs
			msg_list.append(msg_set)
			cnt += 1	
		return msg_list
	
	def check_pattern(self,pattern,type):
		cnt=0
		check_list=[]
		reg = re.compile(pattern,re.M)
		for item in self.msg_list:
			list_str = re.findall(reg, item['message'])
			if list_str :
				item[type]=True
				check_list.append(item)
				cnt+= 1	
			else:
				item[type]=False
		return check_list
	
	def check_sell(self):
		pattern = ur'([\u4e00-\u9fa5]*\u5356.*[0-9]{6}.*[^\n]+)'
		return self.check_pattern(pattern,'sell')
		
	def check_buy(self):
		pattern = ur'([\u4e00-\u9fa5]*\u4e70.*[0-9]{6}.*[^\n]+)'
		return self.check_pattern(pattern,'buy')

	def print_list(self,list_str):
		for	item in list_str:
			try:
				#print "----------------------------------------------"
				print item['time']
				print item['message']
				print "----------------------------------------------"
			except UnicodeEncodeError,e:
					print(e.message)
					continue
			
	def save_file(self):
		f=open("test.html","w+")
		f.write(self.details.encode('utf8'))
		f.close()


loop=check_loop()

sell_cnt = 0
buy_cnt = 0
msg_cnt = 0
cnt=0
while 1 :
	print "loop",cnt
	cnt += 1
	if(msg_cnt!=loop.msg_cnt):
		win32api.MessageBox(0, "new msg", "new msg",win32con.MB_OK) 
		print "new msg",msg_cnt,loop.msg_cnt
		msg_cnt = loop.msg_cnt
		loop.print_list(loop.msg_list)

		
	if(sell_cnt!=loop.sell_cnt):
		win32api.MessageBox(0, "sell msg %d" %loop.sell_cnt, "new msg",win32con.MB_OK) 
		print "new sell",sell_cnt,loop.sell_cnt
		loop.print_list(loop.sell_list)
		sell_cnt = loop.sell_cnt
	
	if(buy_cnt!=loop.buy_cnt):
		win32api.MessageBox(0, "buy msg %d" %loop.buy_cnt, "new msg",win32con.MB_OK) 
		print "new buy",buy_cnt,loop.buy_cnt
		loop.print_list(loop.buy_list)
		buy_cnt = loop.buy_cnt
	
	time.sleep(30)
	loop.refresh()
