#! /usr/bin/env python3
# _*_encoding=utf-8_*_

from urllib import request

with request.urlopen("http://imagination.ga/api/tasklist") as f:
	data = f.read();
	print(f.status,f.reason)