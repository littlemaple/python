#！ /user/bin/env python
#! *--coding=utf-8--*

print("===============start============")

def calParams(*args,**kw):
		print(args,kw)

calParams(123)
calParams('asd',name='nn')
calParams('asd',name='nn',pa='qwe')



def log(func):
	def warpper(*args,**kw):
		print("call name %s() %d()" % (func.__name__,0x1001))
		return func(*args,**kw)
	return warpper

@log
def getStatistic(*value,**kw):
	print(value,kw)


getStatistic(12,name1="123",params="12333")


def logs(desc):
	def decorate(func):
		def war(*arg,**kk):
			print("%s() call %s" % (desc,func.__name__))
			return func(*arg,*kk)
		return decorate
	return log

@logs('name')
def getSpec(*v,**kk):
	print("this is mesa")

@logs('name')
getSpec()
@logs('name')
getSpec("asd")

getSpec("asd",name='q1')
