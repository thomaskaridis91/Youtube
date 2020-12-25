from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name) > 1):
        locationError.config(text="Please choose folder",fg="purple")

    else:
        locationError.config(text=Folder_Name,fg="green")


#Download video
def DownloadVideo():
    choice = yChoices.get()
    url = yEntry.get()

    if(len(url)>1):
        yError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif (choice == choices[2]):
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif(choice == choices[3]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            yError.config(text="Paste correct link",fg="red")

    #Download function
    select.download(Folder_Name)
    yError.config(text="Download is completed")

root = Tk()
root.title("YT Downloader")
root.geometry("700x600")  #set window
root.columnconfigure(0, weight=1) #set all in center

#Youtube link label
ylabel = Label(root,text="Enter the url of the video", font = ("jost", 15))
ylabel.grid()

#Entry box
yEntryVar = StringVar()
yEntry = Entry(root, width = 70, textvariable= yEntryVar)
yEntry.grid()

#Error
yError = Label(root, text = "Error", fg= "red", font =("jost",10))
yError.grid()

#Save file
saveLabel = Label(root, text = "Save video file", font = ("jost", 15, "bold"))
saveLabel.grid()

#Button save file
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose path",command=openLocation)
saveEntry.grid()

#Error msg location
locationError = Label(root,text="Error of the path",fg="red",font=("jost",10))
locationError.grid()

#Download quality
yQuality = Label(root,text="Select quality",font=("jost",15))
yQuality.grid()

#Combo box
choices = ("1080p","720p","480p","Only Audio")
yChoices = ttk.Combobox(root,values=choices)
yChoices.grid()

#Download button
downloadbtn = Button(root,text="Download",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

#Developer label
developerlabel = Label(root,text="Thomas",font=("jost",15))
developerlabel.grid()

root.mainloop()