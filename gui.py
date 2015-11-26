#coding=utf-8
#！ /user/bin/env python3

import tkinter as tk
import tkinter.messagebox as messagebox


class Application(tk.Frame):
	def __init__(self,master):
		tk.Frame.__init__(self,master)
		master.minsize(width=666, height=666)
		master.maxsize(width=666, height=666)
		master.title("messagebox")
		self.pack(expand=1)
		self.createWidget()

	def createWidget(self):
		self.tv_show = tk.Entry(self)
		self.tv_show.pack(side='top')
		self.tv_sub = tk.Button(self,text='submit',fg='blue',bg='grey',command=self.display)
		self.tv_sub.pack(side ='left')
		self.QUIT = tk.Button(self,text='quit',fg='red',command=root.quit)
		self.QUIT.pack(side='bottom',pady=20)
	def display(self):
		messagebox.showinfo('title','message')

root = tk.Tk()
app = Application(master=root)
app.mainloop()
