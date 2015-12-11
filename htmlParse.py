﻿#! /usr/bin/env python3
# _*_coding=utf-8_*_


from html.parser import HTMLParser
from html.entities import name2codepoint

print("====================")

class HtmlParse(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print('<%s>' % tag)
	def handle_endtag(self, tag):
		print('</%s>' % tag)
	def handle_startendtag(self, tag, attrs):
		print('<%s/>' % tag)
	def handle_data(self, data):
		print(data)
	def handle_comment(self, data):
		print('<!--', data, '-->')
	def handle_entityref(self, name):
		print('&%s;' % name)
	def handle_charref(self, name):
		print('&#%s;' % name)

parser = HtmlParse()
parser.feed("<html><body><img href='http://imagination.ga'</body></html>")


# from html.parser import HTMLParser
# from html.entities import name2codepoint

# class MyHTMLParser(HTMLParser):

#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)

#     def handle_endtag(self, tag):
#         print('</%s>' % tag)

#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)

#     def handle_data(self, data):
#         print(data)

#     def handle_comment(self, data):
#         print('<!--', data, '-->')

#     def handle_entityref(self, name):
#         print('&%s;' % name)

#     def handle_charref(self, name):
#         print('&#%s;' % name)

# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')