#!/usr/bin/python
# -*- coding:utf-8 -*-  

import re
import urllib

contents = {'����˭','˭����','��','����','û��'}

pattern = r'(\xe5\x8f\x91\xe8\xa1\xa8\xe4\xba\x8e[^<]+)'
reg = re.compile(pattern)
str = re.findall(reg,contents)

print str