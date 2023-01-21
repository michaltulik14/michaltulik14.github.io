from pytube import YouTube
import customtkinter
import moviepy.editor
from tkinter import * 
from customtkinter import *



def download_video():
    if len(entry1.get()) == 0:
        output_result.configure(text="Enter URL link",text_color="red") #Display error when trying to process empty link
    
    link = entry1.get()
    try:
        youtubeObject = YouTube(link)
    except:
        output_result.configure(text="Invalid URL link",text_color="red") #Display error when link is invalid
    
    
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        output_result.configure(text="Failed")  
    output_result.configure(text="Completed successfuly",text_color="green")       

#Converting video to audio 

def browse():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Video files",
                                                        "*.mp4"),
                                                       ("All files",
                                                        "*.*")))

    try:
        content = moviepy.editor.VideoFileClip(filename)
    except:
        output2_result.configure(text="Invalid video format",text_color="red") 

    audio=content.audio

    out_str = str(filename)+".mp3"    #declaring name of the output file
    
    audio.write_audiofile(out_str)

    output2_result.configure(text="Completed successfuly",text_color="green") 




#Creating a GUI


customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("600x600")
root.configure(bg="blue")

root.title("YouConvert")

#Enter link - Label
label1=customtkinter.CTkLabel(root, text="Enter YouTube video URL",font=('',20))
label1.pack(pady=20,padx=10)

#Entry Box
entry1=customtkinter.CTkEntry(root)
entry1.pack(pady=20,padx=10)

#Download button
button=customtkinter.CTkButton(root,command=download_video, text="Download")
button.pack(pady=20,padx=10,ipady=5)

#Display the status of the operation
output_result=customtkinter.CTkLabel(root,text="",font=('Helvetica bold',20))
output_result.pack(pady=20,padx=10)

#Extracting Audio from Video - Label
label2=customtkinter.CTkLabel(root, text="Extract Audio from a Video",font=('',20))
label2.pack(pady=50,padx=10)

#Browse and process button
browse=customtkinter.CTkButton(root,command=browse, text="Browse")
browse.pack(pady=20,padx=10,ipady=5)

#Display the result of the operation
output2_result=customtkinter.CTkLabel(root,text="",font=('Helvetica bold',20))
output2_result.pack(pady=20,padx=10)

root.mainloop()

