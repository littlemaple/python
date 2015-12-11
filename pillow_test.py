#! /user/bin/env python3
# -*-UTF-8-*-

print("======")
from PIL import Image
im = Image.open("image.png")
print(im.format,im.size,im.mode)


from datetime import datetime
print(datetime.now())

date = datetime(2015, 12,20)
print(date)
print(date.timestamp())
t = date.timestamp()
print(datetime.fromtimestamp(t))


from collections import namedtuple
Point  = namedtuple("point",['x','y'])

p = Point(2,3)
print(type(p))

p  =Point('2',2)
print(p.x)

import re

origin=r'12iir@11.com'
res = re.match(r'[a-zA-Z0-9]+@.[0-9a-zA-Z]+',origin)
if res:
	print("match success")
else:
	print("match fail")

import hashlib

md5 = hashlib.md5()
md5.update("this is".encode("utf-8"))
print(md5.hexdigest())
print(md5.digest())
