from bs4 import BeautifulSoup 
import re
import urllib2
import requests

url="http://bbs.macd.cn/forum.php?mod=viewthread&tid=2820739&page=9999&authorid=3833326"
html=urllib2.urlopen(url, timeout=60).read()
details = html.decode("gbk")

#r = requests.get(url)
#details = r.text

soup = BeautifulSoup(details,"html.parser")

#print soup.prettify().encode('utf-8')

list_str=soup.find_all('div',id=re.compile("post_[0-9]+"))
print "len",len(list_str)
for str in list_str:
	print "\n"
	time=str.find_all('em')
	print time[2].get_text()

	speech=str.find_all('td',class_="t_f")
	#quote=speech[0].find_all('div',class_="quote")
	quote=speech[0].find_all('blockquote')
	if len(quote):
		#print "has quote"
		text = speech[0].get_text()
		text=text.split("\n")
		#print "len text",len(text)
		print text[3]
		#print "end"
	else:
		#print "no quote"
		print speech[0].get_text()
	print "\n"