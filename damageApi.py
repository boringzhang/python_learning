#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Prerequisite:
	damage Api functions,convert from EmulatorAPI.dll

Usage:
	for client
Other
	unknown
"""
#commit test
import ctypes
import cstruct

EmulatorAPI = ctypes.WinDLL("EmulatorAPI.dll")

def ConnectToServer(ip):
	"""
	Prerequisite:
	 connect to server
	Arguments:
		ip -- server ip string
	Return:
		socket id
	"""
	EmulatorAPI.ConnectToServer.argytpes = (ctypes.c_char_p, ctypes.POINTER(ctypes.c_int))
	EmulatorAPI.ConnectToServer.restype = ctypes.c_int
	sd = ctypes.c_int(0)
	EmulatorAPI.ConnectToServer(ip,ctypes.pointer(sd))
	return sd

def DisconnectToServer(sd):
	EmulatorAPI.ConnectToServer.argytpes = (ctypes.c_int)
	EmulatorAPI.ConnectToServer.restype = ctypes.c_int
	return EmulatorAPI.DisconnectToServer(sd)

def DamAddTemplate(id,dam):
	dwLen = len(dam)
	array_type = ctypes.c_char * dwLen	
	read_buffer = dam.pack()
	EmulatorAPI.DamAddTemplate.argytpes = (ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong), array_type)
	EmulatorAPI.DamAddTemplate.restype = ctypes.c_int
	ret = EmulatorAPI.DamAddTemplate(0,ctypes.pointer(id),read_buffer)
	dam.unpack(read_buffer)
	return ret
def DamStartAllTemplate():
	EmulatorAPI.DamStartAllTemplate(0)

def StaGetPortData(port):
	dwLen = 64
	array_type = ctypes.c_ulonglong * dwLen	
	read_buffer = array_type()
	EmulatorAPI.StaGetPortData.argytpes = (ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(array_type))
	EmulatorAPI.StaGetPortData.restype = ctypes.c_int
	slot = ctypes.c_ulong(0)
	return EmulatorAPI.StaGetPortData(0,port,read_buffer)


class DAM_FRAME_LOSS_S(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		unsigned int bEdit;  
		unsigned int ulModel;   
		unsigned int ulBurstRange; 
		unsigned int resv1;
		double ulContinuePercentage;
		unsigned int  bCycle;
		unsigned int resv2;
		double  dDamPeriod;	
		double  dDamTotalTime;
	"""
class DAM_FRAME_SEQUENCE_ERROR_S(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		unsigned int bEdit; 
		unsigned int ulModel; 
		unsigned int ulDepthRange;
		unsigned int resv1;
	"""
class DAM_FRAME_REPEAT_S(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		unsigned int bEdit; 
		unsigned int ulMode;  
		unsigned int ulBurstRange; 
		unsigned int resv1;
		double ulContinuePercentage;
		unsigned int bCycle;
		unsigned int resv2;
		double  dDamPeriod;	
		double  dDamTotalTime; 
	"""	
class DAM_QUEUE_DEPTH_S(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		unsigned int bEdit; 
		unsigned int ulDepthRange; 
	"""

class DAM_LINK_LAYER_S(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		unsigned int bEdit;  
		unsigned int ulErrorType;
		unsigned int ulModel;  
		unsigned int ulBurstRange; 
		double ulContinuePercentage;
		unsigned int  bCycle;
		unsigned int resv1;
		double  dDamPeriod;	
		double  dDamTotalTime;
	"""

class DAM_FRAME_DAMAGE_S(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		unsigned int  bEdit;   
		unsigned int  ulModel; 
		unsigned int  ulCorruptionType; 
		unsigned int  ulBurstRange; 
		double ulContinuePercentage;
		unsigned int   bCycle;	
		unsigned int resv1;
		double  dDamPeriod;	
		double  dDamTotalTime; 
	"""

class DAM_FRAME_FILTER_COND_S(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		unsigned int bEnable;
		unsigned int ulOffset;
		unsigned char ucValue[6];
		unsigned char ucMask[6];   
	"""
class DAM_FRAME_FILTER_S(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		unsigned int bEdit;
	       struct DAM_FRAME_FILTER_COND_S stCondition[8];
		char cExpression[256];
	"""

class DAM_LATENCY_S(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		unsigned int bEdit; 
		unsigned int ulLatency;
	       unsigned int ul10gLatency0;
	       unsigned int ul10gLatency1;
	       unsigned int ul10gLatency2;
	       unsigned int ul1000mLatency0;
	       unsigned int ul1000mLatency1;
	       unsigned int ul1000mLatency2;
	       unsigned int ul100mLatency0;
	       unsigned int ul100mLatency1;
	       unsigned int ul100mLatency2;  
	"""

class DAM_REPLACE_S(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		unsigned int bReversal;
		unsigned int bReplace;   
		unsigned int bUdpCorrect; 
		unsigned int bTcpCorrect; 
		unsigned char ucValue[256];
		unsigned char ucMask[256];  
	"""

class DAM_LATENCY_JITTER(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		unsigned int bEdit;  
		unsigned int ulModel;
		unsigned int ulJitterMode;
		unsigned int ulTimeMode;
		unsigned int ulFitValue;
		unsigned int ulPointCount;
		double dMinDelay;
		double dMaxDelay;	
		double dAlphaVal;  
		double dBeataVal;
		double dPortAToPortB;
		double dPortBToPortA;
		unsigned int ulValue[100]; 
	"""
class DAM_BANDWIDTH_POLICER(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		unsigned int bEnable;
		unsigned int bIncL1Bytes;
		unsigned int ulCommitSpeed;
		unsigned int ulExcessSpeed;
		unsigned int ulBurstExcessBytes;
		unsigned int ulBurstCommitBytes;
	"""
class DAM_BANDWIDTH_SHAPER(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		unsigned int bEnable;
		unsigned int bOverSizeDrop;
		unsigned int bIncL1Bytes;
		unsigned int ulCommitSpeed;
		unsigned int ulBurstExcessBytes;
		unsigned int ulBurstCommitBytes; 
	"""
class DAM_BANDWIDTH_CONTROL(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		struct DAM_BANDWIDTH_POLICER stPolicer;
		struct DAM_BANDWIDTH_SHAPER stShaper;
	"""
#typedef struct tag_DAM_TEMPLATE
#{
#	UINT uiDamageID;
#	unsigned int bEnabled;
#	unsigned int bDAMDirection;
#	DAM_FRAME_LOSS_S stFrameLoss;  
#	DAM_FRAME_SEQUENCE_ERROR_S stFrameSequenceError; 
#	DAM_FRAME_REPEAT_S stFrameRepeat;  
#	DAM_QUEUE_DEPTH_S stQuenuDepth;   
#	DAM_LINK_LAYER_S stLinkLayer;    
#	DAM_FRAME_DAMAGE_S stFrameDamager; 
#	DAM_FRAME_FILTER_S stFrameFilter;  
#	DAM_LATENCY_S stLaytency;       
#	DAM_REPLACE_S stReplace;
#	DAM_LATENCY_JITTER stLatcnyJitter; 
#	DAM_BANDWIDTH_CONTROL stBandwidthControl;
#}DAM_TEMPLATE_S;
class DAM_TEMPLATE(cstruct.CStruct):    
	__byte_order__ = cstruct.LITTLE_ENDIAN    
	__struct__ = """
		unsigned int uiDamageID;
		unsigned int bEnabled;
		unsigned int bDAMDirection;
		unsigned int resv1;
		struct DAM_FRAME_LOSS_S stFrameLoss;
		struct DAM_FRAME_SEQUENCE_ERROR_S stFrameSequenceError; 
		struct DAM_FRAME_REPEAT_S stFrameRepeat;  
		struct DAM_QUEUE_DEPTH_S stQuenuDepth;   
		struct DAM_LINK_LAYER_S stLinkLayer;    
		struct DAM_FRAME_DAMAGE_S stFrameDamager; 
		struct DAM_FRAME_FILTER_S stFrameFilter;  
		struct DAM_LATENCY_S stLaytency;       
		struct DAM_REPLACE_S stReplace;
		struct DAM_LATENCY_JITTER stLatcnyJitter; 
		struct DAM_BANDWIDTH_CONTROL stBandwidthControl;
	"""
def damage_test():
	damid=ctypes.c_ulong(0)
	stDamTemplate = DAM_TEMPLATE()

	stDamTemplate.bEnabled = 1

	stDamTemplate.stFrameLoss.bEdit = 1
	stDamTemplate.stFrameLoss.ulModel = 2
	stDamTemplate.stFrameLoss.ulBurstRange = 3
	stDamTemplate.stFrameLoss.ulContinuePercentage = 4
	stDamTemplate.stFrameLoss.bCycle = 5

	stDamTemplate.stLatcnyJitter.bEdit = 1;
	stDamTemplate.stLatcnyJitter.dAlphaVal = 2.0;
	stDamTemplate.stLatcnyJitter.dBeataVal = 2.0;
	stDamTemplate.stLatcnyJitter.ulJitterMode = 0;
	stDamTemplate.stLatcnyJitter.ulPointCount = 100;

	stDamTemplate.stFrameFilter.bEdit = 1;
	stDamTemplate.stFrameFilter.stCondition[2].bEnable = 1;
	stDamTemplate.stFrameFilter.stCondition[2].ulOffset = 0x10;
	stDamTemplate.stFrameFilter.stCondition[2].ucMask[0] = 0xff;
	stDamTemplate.stFrameFilter.stCondition[2].ucMask[1] = 0xff;
	stDamTemplate.stFrameFilter.stCondition[2].ucValue[0] = 0x12;
	stDamTemplate.stFrameFilter.stCondition[2].ucValue[1] = 0x34;
	stDamTemplate.stFrameFilter.stCondition[2].ucValue[2] = 0x56;
	stDamTemplate.stFrameFilter.stCondition[2].ucValue[3] = 0x78;
	stDamTemplate.stFrameFilter.stCondition[2].ucValue[4] = 0x9a;
	stDamTemplate.stFrameFilter.stCondition[2].ucValue[5] = 0xbc;
	stDamTemplate.stFrameFilter.cExpression=b'(a|b|f)&!g'
    
	stDamTemplate.stLaytency.bEdit = 1;
	stDamTemplate.stLaytency.ulLatency = 100;

	stDamTemplate.stLaytency.ul10gLatency0 = 10;
	stDamTemplate.stLaytency.ul10gLatency1 = 20;
	stDamTemplate.stLaytency.ul10gLatency2 = 30;
	stDamTemplate.stLaytency.ul1000mLatency0 = 40;
	stDamTemplate.stLaytency.ul1000mLatency1 = 50;
	stDamTemplate.stLaytency.ul1000mLatency2 = 60;
	stDamTemplate.stLaytency.ul100mLatency0 = 70;
	stDamTemplate.stLaytency.ul100mLatency1 = 80;
	stDamTemplate.stLaytency.ul100mLatency2 = 90;
	i=0
	while i<8:
		stDamTemplate.uiDamageID = i
		stDamTemplate.bDAMDirection = 0
		stDamTemplate.stReplace.bReplace = 1;
		stDamTemplate.stReplace.bTcpCorrect = 1;
		ret = DamAddTemplate(damid,stDamTemplate)
		if ret != 0:
			print("DamAddTemplate ",i,"ret error", ret)
		stDamTemplate.bDAMDirection = 1;
		ret = DamAddTemplate(damid,stDamTemplate)
		if ret != 0:
			print("DamAddTemplate ",i,"ret error", ret)
		i+=1
	DamStartAllTemplate()
	
def main():
	ip=b'192.168.1.3'
	sd = ConnectToServer(ip)
	if sd.value==0:
		print("ConnectToServer ret error ", sd.value)
		return
	print("ConnectToServer ", sd.value)
	ret = StaGetPortData(2)
	if ret != 0:
		print("StaGetPortData ret error ", ret)
		return
	damage_test()
	DisconnectToServer(sd)

if __name__ == '__main__':
    main()

