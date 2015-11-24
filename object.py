#！/user/bin/env python
# *_coding=utf-8_*

print("======================start===============")
class Question(object):
	__slots__=('name','ext','id','value','verify','title','age','set_age')
	def __init__(self,name='default',value='value'):
		self.name = name
		self.value = value
	def display(self):
		print(self.name,self.value)

class NormalQa(Question):
	def display(self):
		print("normal"+str(self.value))

class RadioQa(Question):
	__slots__=('verify')
	def display(self):
		print("radio"+str(self.name))

radio = RadioQa()
normal = NormalQa()

radio.display()
normal.display()
print("=============defined a decorate method============")
def log(func):
	def warp(*arg):
		print("call %s" % func.__name__)
		return func(*arg)
	return warp

@log
def logname(info):
	print("current",info)

logname('ii')

print("====================getattr==============")
print(getattr(radio,'name'))

def set_age(self,age):
	self.age = age
	print(self.age)

radio.title = 'dynamic bind medthod'
print(radio.title)
normal.title ='bind normal'
print(normal.title)

print('==============import types========')
from types import MethodType
radio.set_age = MethodType(set_age,radio)
radio.set_age(123)
Question.set_age = MethodType(set_age,Question)
normal.set_age("bind all instance for set age medthod")
print("===========test for slots==============")
print(radio.age)
radio.id =0x1001
print(radio.id)
radio.ext = 'ext,should not be bind'
print(radio.ext)




