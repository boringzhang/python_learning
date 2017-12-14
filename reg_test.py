# encoding: UTF-8
import re
 
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'Chapter [1-9][0-9]')
 
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
print pattern.group()
 
 
### 输出 ###
# hello