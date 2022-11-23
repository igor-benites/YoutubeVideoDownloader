from tkinter import * #Graphical interface
from tkinter import filedialog #Used while asking the user for the path selection
from pytube import YouTube

root = Tk('Video Downloader')
root.geometry ("640x360") #Window size
root.resizable(0, 0) #Makes the window resizeable
root.title('Video Downloader')

#Interface
Label(root, text="Download Your Video Here", font='san-serif 14 bold').pack()
link = StringVar()
Label(root, text="Paste your link here", font='san-serif 15 bold').place(relx=0.5, rely=0.4, anchor=CENTER)
link_enter = Entry(root, width=70, textvariable=link).place(relx=0.5, rely=0.5, anchor=CENTER) #Link form
Button(root, text='Download', font='san-serif 16 bold', bg='red3', padx=2,command="download").place(relx=0.5, rely=0.65, anchor=CENTER) #Button

#Download Function
def download():
    url = YouTube(str(link.get()))#Captures the youtube url
    video = url.streams.first() #Captures the resolutions avaible
    video.download() #Method to download the video
    Label(root, text="Downloaded", font="arial 15").place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop() #Makes the main window loop, until the user do something

