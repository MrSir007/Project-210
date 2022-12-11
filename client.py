import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound
import pygame
from pygame import mixer
import os
import time

SERVER = None
ip_address = "127.0.0.1"
port = 1050
buffer_size = 4096

song_counter = 0
listbox = None
song_selected = None
infoLabel = None

for file in os.listdir("shared_files") :
  filename = os.fsdecode(file)
  listbox.insert(song_counter, filename)
  song_counter = song_counter + 1


def playSong () :
  global song_selected
  song_selected = listbox.get(ANCHOR)

  pygame
  mixer.init()
  mixer.music.load('shared_files/' + song_selected)
  mixer.music.play()

  if (song_selected != "") :
    infoLabel.configure(text="Now Playing: " + song_selected)
  else :
    infoLabel.configure(text = "")

def stopSong () :
  global song_selected

  pygame
  mixer.init()
  mixer.music.load('shared_files/' + song_selected)
  mixer.music.pause()
  infoLabel.configure(text="")

def resumeSong () :
  global song_selected
  
  mixer.init()
  mixer.music.load('shared_files/' + song_selected)
  mixer.music.play()

def pauseSong () :
  global song_selected
  
  mixer.init()
  mixer.music.load('shared_files/' + song_selected)
  mixer.music.pause()

def musicWindow () :
  window = Tk()
  window.title("Music Window")
  window.geometry("300x300")
  window.configure(bg="LightSkyBlue")

  selectLabel = Label(
    window,
    text="Select Song",
    bg="LightSkyBlue",
    font=("Calibri", 8)
  )
  selectLabel.place(x=2, y=1)

  listBox = Listbox(
    window,
    height=10,
    width=39,
    activestyle="dotbox",
    bg="LightSkyBlue",
    borderwidth=2,
    font = ("Calibri", 10)
  )
  listBox.place(x=10, y=10)

  scrollbar1 = Scrollbar(listBox)
  scrollbar1.place(relheight=1, relx=1)
  scrollbar1.config(command = listBox.yview)

  playButton = Button(
    window,
    text="Play",
    width=10,
    bg="SkyBlue",
    font = ("Calibri", 10),
    command=playSong
  )
  playButton.place(x=30, y=200)

  stopButton = Button(
    window,
    text="Stop",
    bd=1,
    width=10,
    bg="SkyBlue",
    font = ("Calibri", 10),
    command=stopSong
  )
  stopButton.place(x=200, y=200)

  uploadButton = Button(
    window,
    text="Upload",
    bd=1,
    width=10,
    bg="SkyBlue",
    font = ("Calibri", 10)
  )
  uploadButton.place(x=30, y=250)
  
  downloadButton = Button(
    window,
    text="Download",
    bd=1,
    width=10,
    bg="SkyBlue",
    font = ("Calibri", 10)
  )
  downloadButton.place(x=200, y=250)

  stopButton = Button(
    window,
    text="Stop",
    bd=1,
    width=10,
    bg="skyblue",
    font = ("Calibri", 10),
    command=stopSong
  )
  stopButton.place(x=200, y=200)

  resumeButton = Button(
    window,
    text="Resume",
    width=10,
    bd=1,
    bg="skyblue",
    font = ("Calibri", 10),
    command=resumeSong
  )
  resumeButton.place(x=30, y=250)

  pauseButton = Button(
    window,
    text="Pause",
    width=10,
    bd=1,
    bg="skyblue",
    font = ("Calibri", 10),
    command=pauseSong
  )
  pauseButton.place(x=200, y=250)

  infoLabel = Label(
    window,
    text="",
    fg="blue",
    font=("Calibri", 8)
  )
  infoLabel.place(x=4, y=280)
  
  window.mainloop()


def setup () :
  global SERVER
  global ip_address
  global port

  SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  SERVER.connect((ip_address, port))

  musicWindow()

setup()