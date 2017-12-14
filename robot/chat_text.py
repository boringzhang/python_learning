#!/usr/bin/python
# -*- coding:utf-8 -*-  
from aip import AipSpeech
#from pydub import AudioSegment
import pyaudio 
import wave
import io
import subprocess
import os
import urllib
import json
import sys
import time
import numpy as np
from pyaudio import PyAudio, paInt16
from matplotlib import pyplot as plt
from scipy.io.wavfile import read,write

APP_ID = '10498410'
API_KEY = 'hqBZkOatj8KxWFYtmctlRbfW'
SECRET_KEY = 'c0067baad0a54c53e51b96f7c1b1b224'
SAMPLING_RATE = 8000 
tulingkey = 'fc3191b40e2243ff8df88a47fcc0d3a5'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def text_to_wav(text,filename):
	result  = client.synthesis(text, 'zh', 1, {
	    'vol': 5,
	})
	# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
	if not isinstance(result, dict):
	    with open('audio.mp3', 'wb') as f:
	        f.write(result)
	else:
		print "err_no",result['err_no']
		print "err_msg",result['err_msg']
		return
		
	mp3_to_wav('audio.mp3',filename)

def mp3_to_wav(mp3file,wavfile):
	#print mp3file,wavfile
	a=os.popen("wavmp3\lame.exe -h --decode %s %s" %(mp3file,wavfile))
	#sound = AudioSegment.from_mp3(mp3file)
	#sound.export(wavfile, format="wav")
	
def play_audio(filename):
	#subprocess.Popen([MEDIA_PLAYER, filename])
	#define stream chunk   
	chunk = 1024  
	#open a wav format music  
	f = wave.open(filename,"rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  channels = f.getnchannels(), rate = f.getframerate(), output = True)  
	#read data  
	data = f.readframes(chunk)  
	#paly stream  
	while data != '':  
		stream.write(data)  
		data = f.readframes(chunk)  

	#stop stream  
	stream.stop_stream()  
	stream.close()  
	#close PyAudio  
	p.terminate()  
    
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def wav_to_text(data):
	# 识别本地文件
	result = client.asr(data, 'wav', SAMPLING_RATE, {
	    'lan': 'zh',
	})
	if result['err_no']==0 :
		print result['result'][0]
		return result['result'][0]
	else:
		print "err_no",result['err_no']
		print "err_msg",result['err_msg']
		return ''

def getHtml(url):
	url.decode('utf-8')
	page = urllib.urlopen(url)
	html = page.read()
	return html

def tuling_chat(text):
	api = 'http://www.tuling123.com/openapi/api?key=' + tulingkey + '&userid=' + '123456' + '&info='
	request = api + urllib.quote(text)
	print request
	response = getHtml(request)
	dic_json = json.loads(response)
	if 'url' in dic_json:
		print dic_json['url']
		#os.system('chrome %s' %dic_json['url'])
	return dic_json['text']


# 将data中的数据保存到名为filename的WAV文件中
def save_wave_file(filename, data):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SAMPLING_RATE)
    wf.writeframes("".join(data))
    wf.close()


NUM_SAMPLES = 2000      # pyAudio内部缓存的块的大小
SAMPLING_RATE = 8000    # 取样频率
LEVEL = 1500            # 声音保存的阈值
COUNT_NUM = 20          # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
SAVE_LENGTH = 8         # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样

# 开启声音输入ｐｙａｕｄｉｏ对象

pa = PyAudio()
stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True,
              frames_per_buffer=NUM_SAMPLES)
              
def noise_prof(proffile):
	noise='noise.wav'
	wf = wave.open(noise, 'wb')
	wf.setnchannels(1)
	wf.setsampwidth(2)
	wf.setframerate(SAMPLING_RATE)
	cnt=0
	while True:
		# 读入NUM_SAMPLES个取样
		string_audio_data = stream.read(NUM_SAMPLES)
		wf.writeframes("".join(string_audio_data))
		cnt+=1
		if((cnt*NUM_SAMPLES/SAMPLING_RATE)>=1):
			break
	wf.close()
	a=os.popen("sox\sox.exe %s -n noiseprof %s" %(noise,proffile))
	
	
def record_audio():
	t = 0
	end_flag = 0
	power_low_cnt=0
	save_buffer = []
	while True:
		# 读入NUM_SAMPLES个取样
		string_audio_data = stream.read(NUM_SAMPLES)
		# 将读入的数据转换为数组
		audio_data = np.fromstring(string_audio_data, dtype=np.short)
		# 计算大于LEVEL的取样的个数
		large_sample_count = np.sum( audio_data > LEVEL )

		temp = np.max(audio_data)
		if temp > 2000:
			if t==0:
				t = 1 #开启录音
				print "start recording,",temp #"检测到信号，开始录音,计时五秒"
				begin = time.time()

		if t:	
			if temp < 1000:
				power_low_cnt +=1
			else:
				power_low_cnt = 0
			
			if power_low_cnt > 4:  #1s
				end_flag = 1
				print "power low"

			end = time.time()
			if end-begin>5:
				end_flag = 1
				print "timeout"	

			save_buffer.append(string_audio_data)

		if end_flag:
			break
	return save_buffer

def plot_audio(filename):
	rate,data = read(filename)
	print data
	print rate
	data=np.array(data,dtype=np.float64)
	x=np.linspace(0, len(data)/SAMPLING_RATE, len(data))     
	print data
	fig = plt.figure()  
	ax1 = fig.add_subplot(1,1,1)  
	ax1.plot(x,data)
	plt.show()

mode=1
proffile='noise.prof'
audiofile='audio.wav'
noise_prof(proffile)

while True:
	if mode == 0:
		text=raw_input("me:").decode('gbk').encode('utf-8')
		text_to_wav(text,audiofile)			
	else:
		audiodata=record_audio()
		save_wave_file(audiofile,audiodata)
		a=os.popen("sox\sox.exe %s %s noisered %s" %(audiofile,audiofile,proffile))
		#plot_audio(audiofile)
		text=wav_to_text(get_file_content(audiofile))

	if text=='' :
		continue

	if text=='audio':
		mode=1
		continue

	play_audio(audiofile)

	answer=tuling_chat(text)
	print "robot:",answer
	text_to_wav(answer,'answer.wav')
	play_audio('answer.wav')

