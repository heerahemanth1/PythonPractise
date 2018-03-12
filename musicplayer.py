#!/usr/bin/env python
from tkinter import *

class MusicPlayer(Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.Quit = Button(self, text = 'Exit',command = self.quit)
		self.list = 
		self.Quit.pack(side='bottom')

root = Tk()
mplayer = MusicPlayer(master = root)
mm = mplayer.master
mm.title("Music Player")
mm.minsize(600, 400)

mplayer.mainloop()