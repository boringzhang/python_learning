# encoding: UTF-8
import re
 
# ��������ʽ�����Pattern����
pattern = re.compile(r'Chapter [1-9][0-9]')
 
# ʹ��Patternƥ���ı������ƥ�������޷�ƥ��ʱ������None
print pattern.group()
 
 
### ��� ###
# hello