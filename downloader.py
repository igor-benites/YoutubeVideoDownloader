#Api List
from tkinter import *
from tkinter import filedialog #File path
from pytube import YouTube
from moviepy.editor import *

root = Tk('Video Downloader')
root.geometry ("640x360") #Window size
root.resizable(height = None, width = None) #Makes the window resizeable
root.title('Video Downloader')

def selectfilepath():
    filedialog.askdirectory()

def downloadimage():
    url = YouTube(str(link.get())) #Captures the youtube url
    video = url.streams.filter(res='1080p').first() #Captures the resolutions available
    video.download() #Method to download the video
    Label(root, text="Video Downloaded", font="arial 35", bg='green').place(relx=0.5, rely=0.5, anchor=CENTER) #Video Downloaded notification

def downloadaudio():
    url = YouTube(str(link.get())) 
    audio = url.streams.filter(only_audio=True).first() #Captures only the audio
    audio.download() #Method to download the video

def downloadvideo(): 
    CompositeAudioClip([downloadaudio, downloadimage])

#Interface
Label(root, text="Download Your Video Here", font='san-serif 14 bold').pack()
link = StringVar()
Label(root, text="Paste your link here", font='san-serif 15 bold').place(relx=0.5, rely=0.4, anchor=CENTER)
link_enter = Entry(root, width=70, textvariable=link).place(relx=0.5, rely=0.5, anchor=CENTER) #Link form
Button(root, text='Download', font='san-serif 16 bold', bg='red3', padx=2, command=downloadvideo).place(relx=0.3, rely=0.65, anchor=CENTER)
Button(root, text='Choose Your File Path', font='san-serif 16 bold', bg='red3', padx=2, command=selectfilepath).place(relx=0.6, rely=0.65, anchor=CENTER)

root.mainloop() #Makes the main window loop, until the user do something