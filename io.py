#! /user/bin/env python 
#! *--coding=utf-8--*

print("==========start======")
f = open('object.py','r',encoding='utf-8')
try:
	print(f.read())
finally:
	if(f):
		f.close()

print("=============end=============")
f = open('index.txt','w',encoding='utf-8')
f.write('写入python')
f.close()


with open('index.txt','w',encoding='utf-8') as f:
	f.write('写入 aaa')

print("==========read======")
f = open('index.txt','r',encoding='utf-8')
try:
	print(f.read())
finally:
	if(f):
		f.close()
