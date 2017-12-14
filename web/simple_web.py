#!/usr/bin/python
# -*- coding:utf-8 -*-  

import os	#Python�ı�׼���е�osģ������ձ�Ĳ���ϵͳ����
import re	#����������ʽ����
import urllib	#���ڶ�URL���б����
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler  #����HTTP������ص�ģ��


#�Զ��崦��������ڴ���HTTP����
class TestHTTPHandler(BaseHTTPRequestHandler):
	#����GET����
    def do_GET(self):
		#ҳ�����ģ���ַ���
        templateStr = '''  
<html>  
<head>  
<title>QR Link Generator</title>  
</head>  
<body>  
%s
<br>  
<br>  
<form action="/qr"  accept-charset="UTF-8" name=f method="GET"><input maxLength=1024 size=70  
name=s value="" title="Text to QR Encode"><input type=submit  
value="Show QR" name=qr>  
</form>
</body>  
</html> '''


	# ��������ʽ�����Pattern����
	pattern = re.compile(r'/qr\?s=([^\&]+)\&qr=Show\+QR')
	# ʹ��Patternƥ���ı������ƥ�������޷�ƥ��ʱ������None
	print "path",self.path
	match = pattern.match(self.path)
	qrImg = ''
		
	if match:
		print "match 0",match.group(0) 
		print "match 1",match.group(1) 
		# ʹ��Match��÷�����Ϣ
		#qrImg = '<img src="http://chart.apis.google.com/chart?chs=300x300&cht=qr&choe=UTF-8&chl=' + match.group(1) + '" /><br />' + urllib.unquote(match.group(1)) 
		qrImg = '<img src="http://qr.liantu.com/api.php?text=' + match.group(1) + '" /><br />' + urllib.unquote(match.group(1)) 

	self.protocal_version = 'HTTP/1.1'	#����Э��汾
	self.send_response(200)	#������Ӧ״̬��
	self.send_header("Welcome", "Contect")	#������Ӧͷ
	self.end_headers()
	self.wfile.write(templateStr % qrImg)	#�����Ӧ����
	
#����������
def start_server(port):
    http_server = HTTPServer(('', int(port)), TestHTTPHandler)
    http_server.serve_forever()	#����һֱ��������������

#os.chdir('static')	#�ı乤��Ŀ¼�� static Ŀ¼
start_server(8000)	#�������񣬼���8000�˿�