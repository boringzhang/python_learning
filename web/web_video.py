#!/usr/bin/python
# -*- coding:utf-8 -*-  

import os	#Python的标准库中的os模块包含普遍的操作系统功能
import re	#引入正则表达式对象
import urllib	#用于对URL进行编解码
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler  #导入HTTP处理相关的模块

channels ={
	'1':"http://api.47ks.com/webcloud/?v=",
	'2':"http://vip.72du.com/api/?url=",
	'3':"http://qtzr.net/s/?qt=",
	'4':"http://000o.cc/jx/ty.php?url=",
	'5':"http://yyygwz.com/index.php?url=",
	'6':"http://www.wmxz.wang/video.php?url=",
	'7':"http://yun.zihu.tv/play.html?url=",
	'8':"http://www.vipjiexi.com/yun.php?url=",
	'9':"https://jxapi.nepian.com/ckparse/?url=",
	'10':"http://2gty.com/apiurl/yun.php?url=",
	'11':"http://www.chepeijian.cn/jiexi/vip.php?url=",
	'12':"https://apiv.ga/magnet/",
};

auto_select = {'youku': channels['8'], 
		'iqiyi':  channels['6'],
		'qq': channels['10'],
		'le': channels['1'],
		'sohu': channels['1'],
		'mgtv': channels['1'],
		'pptv': channels['1'],
		'wasu': channels['1'],
		};
	
#自定义处理程序，用于处理HTTP请求
class TestHTTPHandler(BaseHTTPRequestHandler):
	#处理GET请求
    def do_GET(self):
		#页面输出模板字符串
        templateStr = '''  
<html>  
<head>  

<title>QR Link Generator</title>  
</head>  
<body>  
%s
<br> 
<iframe src="%s" id="player" height="450px" width="100%%" allowtransparency="true" frameborder="0" scrolling="no"></iframe>
<br>
<form action="/video"  accept-charset="UTF-8" name=f method="GET">
<select class="form-control input-lg" name=api id="jk">
	<option value="auto"  style="color:red">自动选择</option>
	<option value="1"  style="color:red">1号通用接口</option>
	<option value="2" style="color:red">2号通用接口</option>
	<option value="3">3号通用接口</option>
	<option value="4">4号通用接口</option>
	<option value="5">5号通用接口</option>
	<option value="6">6号通用接口</option> 
	<option value="7">7号通用接口</option>
	<option value="8">8号通用接口</option>
	<option value="9">9号通用接口</option>
	<option value="10">10号通用接口</option>
	<option value="11">11号通用接口</option>	
	<option value="12">12号通用接口</option></select>
<input maxLength=1024 size=70  name=v value="" title="video"><input type=submit  value="Vip Video">  
</form>
</body>  
</html> '''

	qrImg = ''
	isImg = 0

	pattern_img = re.compile(r'/([^\&]+)\.png')
	match = pattern_img.match(self.path)
	
	if match:
		isImg = 1
		imgFile = "%s.png" %urllib.unquote(match.group(1)).decode('utf-8')
		print "isImag",isImg
		
	video_url=''
	
	pattern_video = re.compile(r'/video\?api=([^\&]+)\&v=([^\&]+)')
	match = pattern_video.match(self.path)
	if match:
		channel = urllib.unquote(match.group(1)).decode('utf-8')
		site_url = urllib.unquote(match.group(2)).decode('utf-8')
		if  channels.has_key(channel) :
			video_url = channels[channel] + site_url
		else:
			for site_key in  auto_select.keys():
				if site_key in site_url:
					video_url = auto_select[site_key] + site_url
					break

		imgFile = "url.png"
		urllib.urlretrieve("http://qr.liantu.com/api.php?text=%s" %video_url.encode('utf-8'), imgFile)
		qrImg = '<img src='+imgFile+'/>'
		print "real url is 111",video_url
		
	
	if isImg==1 :
		print "response isImag"
		self.protocal_version = 'HTTP/1.1'	#设置协议版本
		self.send_response(200)	#设置响应状态码
		self.send_header('Contect-type', 'image/png')	#设置响应头
		self.end_headers()
		self.wfile.write(open(imgFile,'rb').read())
	else:
		print "response others"
		self.protocal_version = 'HTTP/1.1'	#设置协议版本
		self.send_response(200)	#设置响应状态码
		self.send_header("Welcome", "Contect")	#设置响应头
		self.end_headers()
		self.wfile.write(templateStr %(qrImg,video_url.encode('utf-8')))	#输出响应内容
    
#启动服务函数
def start_server(port):
    http_server = HTTPServer(('', int(port)), TestHTTPHandler)
    http_server.serve_forever()	#设置一直监听并接收请求

os.chdir('.')	#改变工作目录到 static 目录
start_server(8000)	#启动服务，监听8000端口