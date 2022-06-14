"""
Program: musicplayerGUI.py
Author: Jessica 6/13/2022

GUI-based version of the music player app.
**MUST install pygame package by running: pip install pygame
"""

from breezypythongui import EasyFrame
from pygame import mixer
from tkinter import PhotoImage
from tkinter.font import Font
#other imports

class MusicPlayerGUI(EasyFrame):
	# definiton of the __init__() method which is our class constructor
	def __init__(self):
		# call the EasyFrame version of __init__
		EasyFrame.__init__(self, title = "Music Player GUI", background="black", resizeable = False)
		myFont = Font(family="Impact",size = 28)
		self.addLabel(title="Music Player", row = 0, column = 0, columnspan = 3, background = "black", foreground="orange", sticky="NSEW",font = myFont)
		# Create a label variable for the image label
		self.imageLabel = self.addLabel(text = "", row = 1, column = 0, columnspan = 3,sticky= "NSEW")
		# Load the image into the imageLabel object
		self.image = PhotoImage(file = "music_player.png")
		self.imageLabel["image"] = self.image
		# Label and button to lpad the music file
		self.addLabel(text="Enter file name to load", row=2,column=0, background="black", foreground="orange",sticky="NE")
		self.musicFile = self.addTextField(text="", row=2, column =1)
		self.addButton(text = "Load", row = 2, column = 2, command= self.loadFile)
		# 3 buttons for the music player functions
		self.playButton = self.addButton(text = "Play", row=3, column=0, state="disabled", command=self.playMusic)
		self.pauseButton = self.addButton(text= "Pause", row=3, column=1, state="disabled", command=self.pauseMusic)
		self.resumeButton = self.addButton(text = "Resume", row=3,column=2, state="disabled", command=self.resumeMusic)

	# Event handling methods for the command beutton
	def loadFile(self):
		#initialize the pygame mixer
		mixer.init()
		songFile = self.musicFile.getText()
		mixer.music.load(songFile)
		self.playButton["state"] = "normal"

	def playMusic(self):
		# Play previously loaded music file
		mixer.music.play()
		self.pauseButton["state"] = "normal"

	def pauseMusic(self):
		# pause the current song
		mixer.music.pause()
		self.pauseButton["state"] = "disabled"
		self.resumeButton["state"] = "normal"

	def resumeMusic(self):
		#resume tje current song
		mixer.music.unpause()
		self.pauseButton["state"]="normal"
		self.resumeButton["state"]="disabled"
# definition of the main method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	MusicPlayerGUI().mainloop()

#global call to the main() method
main()