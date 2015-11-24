#! /user/bin/env python3
# -*-encoding=utf-8-*-

from tkinter import *
import tkinter.messagebox as messagebox
class CusApplication(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
        self.alertButton = Button(self,text='input',command=self.display)
        self.alertButton.pack()
        self.inputEntry = Entry(self)
        self.inputEntry.pack()

    def display(self):
        print('print',self.inputEntry.get())
        messagebox.showinfo('title',self.inputEntry.get() if self.inputEntry.get() else 'default')

cus = CusApplication()
cus.master.title('gpu')
cus.mainloop()

