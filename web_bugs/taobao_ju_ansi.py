#!/usr/bin/python
# -*- coding:utf-8 -*-  
'''
@author: Techzero
@email: techzero@163.com
@time: 2014-5-18 ����5:06:29
'''
import cStringIO
import getopt
import time
import urllib2
import subprocess
import sys

from datetime import datetime

MEDIA_PLAYER = 'C:/Program Files/Windows Media Player/wmplayer.exe'
MEDIA_FILE = 'D:/onestop.mid'
CHROME = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
URL = 'https://detail.ju.taobao.com/home.htm?spm=608.8866757.J_8xb0my4lz18.6.854152Qr8LB8&id=10000063276602&item_id=555589089023'
NO_X11 = False

def get_current_button():
    '''��ȡ��ǰ��ť״̬'''
    content = urllib2.urlopen(URL,timeout=60).read() #��ȡҳ������
    
    buf = cStringIO.StringIO(content.decode('gbk').encode('utf8')) #��ҳ������ת��Ϊ������
    f=open("tb.html","w+")
    f.write(content)
    f.close
    current_button = None
    for line in buf:
        line = line.strip(' \n\r') #ȥ���س�����
        #print "tyep is",type('')
        #print "line is",type(line)
        #print type('��������')

        if line.find(r'��������') != -1:
        	print line.decode('utf8')
        if line.find(r'< href="#" class="extra  notice J_BuyButtonSub">��������</a>') != -1:
            current_button = '��������'
            break
        elif line.find(r'<div class="main-box chance ">') != -1:
            current_button = '���л���'
            break
        elif line.find(r'<span class="out floatright">������...</span>') != -1:
            current_button = '������'
            break
        elif line.find(r'<span class="out floatright">�ѽ���...</span>') != -1:
            current_button = '�ѽ���'
            break
        elif line.find(r'<input type="submit" class="buyaction J_BuySubmit"  title="������" value="������"/>') != -1:
            current_button = '������'
            break
        
    buf.close()
    return current_button


def notify():
    '''����֪ͨ����Chrome����ɱҳ��'''
    subprocess.Popen([MEDIA_PLAYER, MEDIA_FILE])
    if not NO_X11:
        subprocess.Popen([CHROME, URL])
        print '��ҳ��'


def monitor_button(interval, last):
    '''��ʼ���Ӱ�ť'''
    elapse = 0
    while elapse < last:
        current_button = get_current_button()

        now = datetime.now()
        print '%d-%d-%d %d:%d:%d - ���ڰ�ť�� %s' % (now.year, now.month, now.day, now.hour, now.minute, now.second, current_button)

        if current_button == '������' or current_button == '���л���':
            print '�Ͻ�������'
            notify()
            break
        elif current_button == '������' or current_button == '�ѽ���':
            print '�´����԰ɣ�'
            break
        else:
            print '��û��ʼ�أ��ٵȵȰɣ�'

        time.sleep(interval)
        elapse += interval


def usage():
    print '''
usage: monitor_mac_price.py [options]

Options:
    -i interval: 30 seconds by default.
    -l last: 1800 seconds by default.
    -h: Print this usage.
    -X: Run under no X11.
'''

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'i:l:hX')
    except getopt.GetoptError, err:
        print str(err)
        sys.exit(1)

    interval = 10
    last = 1800

    for opt, val in opts:
        if opt == '-i':
            interval = int(val)
        elif opt == '-l':
            last = int(val)
        elif opt == '-X':
            NO_X11 = True
        elif opt == '-h':
            usage()
            sys.exit()

    monitor_button(interval, last)