#! /user/bin/env python3
#--coding=utf-8--

import base64

print("===================")
origin = "python"
print("origin",origin)
encode = base64.b64encode(origin.encode())
print("encode:",encode)
decode = base64.b64decode(encode)
print('decode:',decode)

origin = (1,10,1000,1000,10000)


def int2bytes(arr):
	res=[]
	for x in arr:
		res.append(x>>24&0xff)
		res.append(x>>16&0xff)
		res.append(x>>8&0xff)
		res.append(x&0xff)
	return res


def bytes2int(arr):
	res=[]
	for x in range(0,len(arr),4):
		tmp = arr[x:x+4]
		res.append((tmp[0]&0xff)<<24|(tmp[1]&0xff)<<16|(tmp[2]&0xff)<<8|tmp[3]&0xff)
	return res

def bytes2intL(arr):
	res=[]
	for x in range(0,len(arr),4):
		tmp = arr[x:x+4]
		res.append((tmp[3]&0xff)<<24|(tmp[2]&0xff)<<16|(tmp[1]&0xff)<<8|tmp[0]&0xff)
	return res

print(origin)
res = int2bytes(origin)
print(res)
rr = bytes2int(res)
print(rr)

origin = "AE4ATgBOAE0ATQBNAE0ATQBNAE0ATQBNAFAAUABQAE0ASwBKAEkASQBIAEgASABJAEkASQBIAEkASQBKAEoASgBLAEsASwBKAEoASgBKAEkASQBJAEoASwBLAEoASQBKAEkASgBKAEkASQBJAEkASQBJAEkASQBJAEoASgBKAEkASgBKAEsASgBLAEsASgBKAEoASwBLAEsASwBLAEsATABMAEwATABMAEwATQBNAE0ASwBLAEsATABNAEwASwBMAEsATABLAEsASwBLAEsASwBLAEsASgBKAEsASwBLAEoASQBKAEoASgBKAEoASgBLAEwATABNAE0ATABLAEkASQBKAEsASwBLAEsASwBKAEoARwBHAEcASQBJAEoASgBLAEsASgBKAEkASQBJAEkASgBKAEsASwBLAEsASwBLAEsASgBJAEgASABJAEkASQBIAEgASQBKAEsASwBIAEgASABJAEoASgBKAEkASQBIAEgASQBKAEoASQBIAEQAQwBFAEYARwBHAEgASABJAEkASQBJAEgARwBHAEcASABIAEgASABIAEkASQBIAEgASQBJAEkASQBJAEkASQBJAEkASQBJAEkASgBKAEoASgBKAEkASABGAEYARgBIAEkASQBJAEkASwBNAE0ATABIAEUARQBFAEYARwBHAEgASABJAEoASQBJAEkASQBJAEoASgBJAEkASQBJAEkASQBIAEgASABIAEkASQBJAEgASABHAEgASABHAEcARwBIAEgASQBJAEgASABJAEkASQBJAEkASgBKAEoASgBJAEkASgBLAEoASwBKAEkASQBJAEkASQBJAEkASgBKAEoASgBJAEkASQBJAEgASABHAEcASABIAEkASQBJAEkASQBIAEgASABJAEkASQBJAEgASABJAEoASgBIAEcARgBHAEgASABJAEkASQBIAEcARwBJAEoASgBKAEkASQBJAEgASQBIAEoASQBIAEYARQBGAEcASABIAEgASABIAEkASQBJAEcARwBHAEgASQBJAEkASQBJAEoASgBKAEkASQBJAEgASABHAEcASABJAEkASgBKAEoASQBIAEgASABJAEgASABHAEYARgBHAEgASQBIAEgASABIAEgASABIAEgASABIAEkASQBJAEkASQBJAEkASQBIAEgASQBJAEoASQBJAEkASgBKAEgARgBFAEUARwBHAEcASABJAEkASQBJAEgASABIAEkASQBJAEkASABHAEYARgBIAEkASQBJAEkASQBKAEkARwBGAEcASABIAEgARwBHAEcASABIAEkASABIAEcARwBHAEgASABJAEoASgBIAEYARQBFAEYARwBHAEcASABJAEkASQBJAEgASABHAEcARwBHAEcASABIAEkASABIAEgARwBIAEgASABHAEcASABJAEkASQBIAEcASABJAEgASABHAEcARwBIAEkASQBIAEgARwBHAEcARwBHAEgASABIAEgARwBHAEcASABJAEoASgBKAEoASgBKAEkASQBJAEkASABHAEcASABJAEoASgBJAEgARwBGAEcASABIAEgASABIAEgASABJAEkASQBKAEoASgBKAEkASQBIAEgASABHAEcARwBHAEgASABIAEgASABIAEkASQBJAEkASQBJAEkASQBKAEoASQBIAEgASABIAEkASQBKAEoASgBJAEkASQBJAEkASQBKAEkASQBJAEkASABHAEcARwBIAEgASABIAEgASABHAEcARwBIAEgASQBJAEgASQBJAEkASQBJAEgARwBHAEcASABIAEkASQBJAEkASQBJAEgASQBJAEkASQBIAEcARwBHAEcASABIAEgASABJAEkASQBKAEoASgBIAEcARwBHAEgASQBJAEkASABIAEgASABIAEkASQBJAEkASABIAEgASQBJAEkASQBJAEkASQBIAEgASQBJAEkASABIAEgASABJAEkASQBJAEkASQBJAEkASABHAEgASABIAEkASQBJAEgARwBGAEcASABJAEkASQBJAEkASQBJAEsAUQBWAFUATwBMAEsATwBQAE4ASQBFAEMARQBFAEUARQBFAEUARQBFAEYARwBFAEMAQwBEAEkASwBMAEkARwBGAEUARQBFAEYARgBGAEYARgBHAEcARwBHAEgASABHAEcARwBIAEcASABHAEcARgBGAEcARwBIAEkASQBJAEkASQBIAEcARwBHAEwAUgBWAFUAUwBRAE4ATABLAEsASQBJAEgASABIAEgASgBNAFIAVABVAFQAUQBPAE0ASwBKAEcARwBGAEYARgBIAEgASQBJAEsATgBPAFAATQBLAEkARwBHAEcARwBHAEgASABKAEgARwBHAEcASgBLAEsASwBLAEsASwBNAEwASgBHAEYARQBGAEcASABKAEsATABLAEsASQBJAEgASABIAEkASwBKAEgARwBHAEsATQBNAEoARgBFAEUASABJAEsASwBLAEsATABMAEwATgBRAFMAUQBNAEkARwBGAEUARQBFAEcASgBMAEsASABGAEYARwBIAEkATABPAFEAUQBRAFEAUQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYAFcAVQBUAFMAVQBUAFAASgBFAEQARABHAEgASABIAEcARQBFAEYASABKAEgARgBFAEUASABKAEsASwBLAEwATgBSAFUAVQBRAEwASgBKAEoASABIAEkASgBLAEkASABGAEYASQBJAEgARgBGAEgASQBMAEwATQBOAFEAUgBSAFEAUQBRAFIAUABNAEwASwBLAEkASQBLAEsASgBIAEgASQBJAEkASQBJAEkASQBJAEoASgBKAEoASQBKAEoASwBLAE0AUABSAFEATgBMAEsASwBMAE0ATQBMAEsASgBJAEoASgBLAEoASgBJAEkASQBKAEsATQBQAFQAUwBRAFEAUQBPAE4ATgBOAFMAVgBXAFcAVgBVAFAATgBLAEsASwBJAEkASQBIAEgASABIAEoASgBJAEgARgBGAEYARwBIAEgASABIAEcARwBHAEgASABIAEkASgBKAEkARwBHAEcASABKAEoASQBIAEgASABIAEkASwBLAEsASABFAEUARgBHAEgASABIAEkASQBJAEkASgBJAEkASQBKAEoASgBKAEoASgBLAEsASwBKAEoASgBLAEwATwBSAFQAVABUAFQ="
print(origin)
decode = base64.b64decode(origin.encode("utf-8"))
print(decode)
print(len(decode)/4)
res = bytes2int(decode)
print(res)
print("================")

i=10
bi = i.to_bytes(32,'big')
print(bi)
bs = int.from_bytes(bi,'big')
print(bs)
print(len(bi))

res=[]
for x in range(0,len(decode),32):
	res.append(int.from_bytes(decode[x:x+32],'big'))
print(res)



# oxygen=(range(80,99,1))
# origin = int2bytes(oxygen)
# ori = b''.join(origin)
# originstr = ori.decode()
# print(originstr)

print("===================")

encodeStr = "AAAAAQAAACIAAAFZAAAFsAAAW30="
decode = base64.b64decode(encodeStr.encode())
print(type(decode))
print(decode)
print(len(decode))
decodeint = []
for i in range(0,len(decode),4):
	decodeint.append(int.from_bytes(decode[i:i+4],'big'))

print(decodeint)

