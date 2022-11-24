#Api List
from tkinter import *
from tkinter import filedialog #File path
from pytube import YouTube
#import PySimpleGUI as sg
#from moviepy.editor import *
#sg.theme('Dark')

root = Tk('Video Downloader')
root.geometry ("640x360") #Window size
root.resizable(0, 0) #Makes the window resizeable
root.title('Video Downloader')

def downloadvideo():
    url = YouTube(str(link.get())) #Captures the youtube url
    video = url.streams.filter(res="1080p").first() #Captures the resolutions available
    video.download() #Method to download the video
    Label(root, text="Video Downloaded", font="arial 35", bg='green').place(relx=0.5, rely=0.5, anchor=CENTER) #Video Downloaded notification
    
def downloadaudio():
    url = YouTube(str(link.get()))
    audio = url.streams.filter(only_audio=True).first() #Captures only the audio
    audio.download() #Method to download the audio
   #Label(root, text="Video Downloaded", font="arial 35", bg='green').place(relx=0.5, rely=0.5, anchor=CENTER) #Audio Downloaded notification

def selectfilepath():
    path = filedialog.askdirectory().str(output_path=path)
    #video.download(output_path=path_label)

#Interface
Label(root, text="Download Your Video Here", font='san-serif 14 bold').pack()
link = StringVar()
Label(root, text="Paste your link here", font='san-serif 15 bold').place(relx=0.5, rely=0.4, anchor=CENTER)
link_enter = Entry(root, width=70, textvariable=link).place(relx=0.5, rely=0.5, anchor=CENTER) #Link form
Button(root, text='Download', font='san-serif 16 bold', bg='red3', padx=2, command=downloadaudio and downloadvideo).place(relx=0.3, rely=0.65, anchor=CENTER) #Button
Button(root, text='Choose Your File Path', font='san-serif 16 bold', bg='red3', padx=2, command=selectvideofilepath).place(relx=0.6, rely=0.65, anchor=CENTER)

root.mainloop() #Makes the main window loop, until the user do something