#!/usr/bin/python
# -*- coding:utf-8 -*-  
import sys
print sys.getdefaultencoding()

#!/usr/bin/env python 
#coding=utf-8 
s='����'
su = 'u''�й�' #not support???
print su
print type(s)
print s
#print s.encode('GB2312') 

#default is gbk
print s.decode('gbk').encode('utf-8')
print s
#if isinstance(s, unicode): 
#	#s=u"����" 
#	print s.encode('gb2312') 
#else: 
#	#s="����" 
#	print s.decode('utf-8').encode('gb2312')