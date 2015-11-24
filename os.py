#! /user/bin/env python3
# -*-encoding=utf-8-*-

print("=============os==================")
import os
print("os name:",os.name)
print("os variable:",os.environ)
print("os path",os.environ.get('PATH'))

print("============json=============")
import json
class Real(dict):
	def __init__(self,name='default',value='default'):
		self['name']= name
		self['value'] = value
	def display(self):
		pass

class ListImpl(list):
	pass
real = Real('show name')
listImpl = ListImpl(map(lambda x: x*x,[1,2,3,5,6,7,4,3]))
print(json.dumps(real))
print(json.dumps(listImpl))

