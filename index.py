#！/user/bin/env python
#! -*- coding=utf-8 -*-

arr = ['item','item23','item5']

arr[1]=12
print(arr)

t = (12,)
print(t)
print(t[0])
if len(t)==1:
	print('if established')
	print('asd')

print(len(t))

for item in arr:
	print("item:"+str(item))

print("=============end===============")

print("========for dict==========")
dd = {12:123,"asd":"asd"}

print("the name:"+str(dd[12]))
print(dd["asd"])

def getCoordinate(x,y=4):
	return "x:"+str(x),"y:"+str(y)
print(getCoordinate(12))
print(">>especial")
print(getCoordinate(12,12)[0])
def iter(i):
	if(i==1):
		return 1
	else:
		return i*iter(i-1)
print(iter(123))

print(arr[1:8])

l = range(12)
print(l[0:4])

for x,y in enumerate(arr):
	print (x,y)

itt = [i*i for i in range(1,5)]
for ii in itt:
	print(ii);

cloudStr = [m+n for m in ['n','x','y'] for n in ['r','q']]
print(cloudStr)


import os

for d in os.listdir('.'):
	print(d)

l = [x for x in range(20)]

print(l[6])

print("================================next======================")
def getCoor(x,y):
	return x ,y
print("x",getCoor(2,4)[0],getCoor(2,4)[1])

print(int('123'))
 

class sample(object):
	def __init__(self,name='python' ,source='cygwin'):
		self.__name = name
		self.source = source

ss = sample('cys')
print(ss.source)


