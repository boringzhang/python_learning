import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist      

def saveImg(Images):
	x=0
	for imgurl in Images:
		urllib.urlretrieve(imgurl,'images/%s.jpg' % x)
		x+=1

html = getHtml("http://tieba.baidu.com/p/2460150866")
#print html
Images=getImg(html)
saveImg(Images)
