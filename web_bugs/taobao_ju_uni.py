
# -*- coding:utf-8 -*-  
'''
@author: Techzero
@email: techzero@163.com
@time: 2014-5-18 \u4E0B\u53485:06:29
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
    '''\u83B7\u53D6\u5F53\u524D\u6309\u94AE\u72B6\u6001'''
    content = urllib2.urlopen(URL,timeout=60).read() #\u83B7\u53D6\u9875\u9762\u5185\u5BB9
    
    buf = cStringIO.StringIO(content.decode('gbk').encode('utf8')) #\u5C06\u9875\u9762\u5185\u5BB9\u8F6C\u6362\u4E3A\u8F93\u5165\u6D41
    f=open("tb.html","w+")
    f.write(content)
    f.close
    current_button = None
    for line in buf:
        line = line.strip(' \n\r') #\u53BB\u6389\u56DE\u8F66\u6362\u884C
        #print "tyep is",type('')
        #print "line is",type(line)
        print type('\u5F00\u56E2\u63D0\u9192')

        if line.find(r'') != -1:
        	print line.decode('utf8')
        if line.find(r'< href="#" class="extra  notice J_BuyButtonSub">\u5F00\u56E2\u63D0\u9192</a>') != -1:
            current_button = '\u5F00\u56E2\u63D0\u9192'
            break
        elif line.find(r'<div class="main-box chance ">') != -1:
            current_button = '\u8FD8\u6709\u673A\u4F1A'
            break
        elif line.find(r'<span class="out floatright">\u5356\u5149\u4E86...</span>') != -1:
            current_button = '\u5356\u5149\u4E86'
            break
        elif line.find(r'<span class="out floatright">\u5DF2\u7ED3\u675F...</span>') != -1:
            current_button = '\u5DF2\u7ED3\u675F'
            break
        elif line.find(r'<input type="submit" class="buyaction J_BuySubmit"  title="\u9A6C\u4E0A\u62A2" value="\u9A6C\u4E0A\u62A2"/>') != -1:
            current_button = '\u9A6C\u4E0A\u62A2'
            break
        
    buf.close()
    return current_button


def notify():
    '''\u53D1\u51FA\u901A\u77E5\u5E76\u7528Chrome\u6253\u5F00\u79D2\u6740\u9875\u9762'''
    subprocess.Popen([MEDIA_PLAYER, MEDIA_FILE])
    if not NO_X11:
        subprocess.Popen([CHROME, URL])
        print '\u6253\u5F00\u9875\u9762'


def monitor_button(interval, last):
    '''\u5F00\u59CB\u76D1\u89C6\u6309\u94AE'''
    elapse = 0
    while elapse < last:
        current_button = get_current_button()

        now = datetime.now()
        print '%d-%d-%d %d:%d:%d - \u73B0\u5728\u6309\u94AE\u662F %s' % (now.year, now.month, now.day, now.hour, now.minute, now.second, current_button)

        if current_button == '\u9A6C\u4E0A\u62A2' or current_button == '\u8FD8\u6709\u673A\u4F1A':
            print '\u8D76\u7D27\u62A2\u8D2D\uFF01'
            notify()
            break
        elif current_button == '\u5356\u5149\u4E86' or current_button == '\u5DF2\u7ED3\u675F':
            print '\u4E0B\u6B21\u518D\u8BD5\u5427\uFF01'
            break
        else:
            print '\u8FD8\u6CA1\u5F00\u59CB\u5462\uFF0C\u518D\u7B49\u7B49\u5427\uFF01'

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