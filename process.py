import sys, time

line=60

def view_bar(num, total): 
	
	rate = num / total 
	rate_num = int(rate * 100) 
	cnt=int(line*rate)
	r = '[%s%s]%d%%\r' % ("="*cnt, " "*(line-cnt), rate_num) 
	sys.stdout.write(r) 
	sys.stdout.flush() 
  
for i in range(0, 101):
	time.sleep(0.1)
	view_bar(i, 100) 
