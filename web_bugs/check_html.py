#!/usr/bin/python
# -*- coding:utf-8 -*-  

import re
import urllib

url="http://bbs.macd.cn/forum.php?mod=viewthread&tid=2820739&page=9999&authorid=3833326"
html=urllib.urlopen(url).read()
details = html.decode("gbk").encode("utf-8")

f=open("test.html","w+")
f.write(details)
f.close()

pattern_sell = r'(\xe5\x8d\x96\xe5\x87\xba[^<]+)'
reg_sell = re.compile(pattern_sell)
sell_list = re.findall(reg_sell,details)

#print "sell list",sell_list
for	str in sell_list:
	print str.decode('utf-8')

pattern_buy = r'(\xe4\xb9\xb0\xe5\x85\xa5[^<]+)'
reg_buy = re.compile(pattern_buy)
buy_list = re.findall(reg_buy,details)

#print "buy list",buy_list
for	str in buy_list:
	print str.decode('utf-8')

pattern_time = r'(\xe5\x8f\x91\xe8\xa1\xa8\xe4\xba\x8e[^<]+)'
reg_time = re.compile(pattern_time)
time_list = re.findall(reg_time,details)

#print "time_list",time_list
for	str in time_list:
	print str.decode('utf-8')
	
#pattern_quote = r'([.+][<blockquote>](.+)[</blockquote>])'
pattern_quote = r'<div class="quote">.+[</blockquote>]'
reg_quote = re.compile(pattern_quote)
quote_list = re.findall(reg_quote,details)

print "len",len(quote_list)
#print "quote_list",quote_list[0]
#print "quote_list",quote_list
for	str in quote_list:
	print str.decode('utf-8')

for	str in sell_list:
	for quote in quote_list:
		if str in quote:
			print str.decode('utf-8'),"remove"
			print quote.decode('utf-8'), "asdfsadf"
			sell_list.remove(str)
			break

for	str in sell_list:
	print str.decode('utf-8')

