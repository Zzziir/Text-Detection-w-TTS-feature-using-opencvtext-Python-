from pytesseract import pytesseract
from time import sleep
import pyttsx3
import cv2
import tkinter as tk
from tkinter import *
import numpy as np
from PIL import Image, ImageTk

#note: run venv/Scripts/activate to terminal to activate virtual environment before running app.py

#Function to read the webcam, and return the text 
def tesseract():
    image = Image.fromarray(img1)
    image.save('test1.jpg')
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = "test1.jpg"
    pytesseract.tesseract_cmd = path_to_tesseract
    textread = pytesseract.image_to_string(Image.open(image_path))
    print(textread[:-1])
    readTextLabel['text'] = textread
    #text-to-speech feature
    text_speech.say(textread)
    text_speech.runAndWait()
    return textread

# object_detector = cv2.createBackgroundSubtractorMOG2()
text_speech = pyttsx3.init()

#Main Root
root = tk.Tk()
root.title('AI Project')
# root.eval('tk::PlaceWindow . center')
root.geometry("480x853")
root.configure(bg="#4a81ff")

#Function to display the camera in Capture Frame
def show_camera_in_capture_frame():
    while True:
        #To check AI webcam
        # mask = object_detector.apply(Image) 
        # cv2.imshow("Mask", mask)
        img = camera.read()[1]
        global img1
        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(img1))
        L1['image'] = img
        root.update()

#Function to Show Splash Screen
def show_splash_screen():
    splash_screen_frame.pack(fill='both', expand=1)
    splash_screen_frame.after(3000, move_to_home_frame)

#Function to Navigate to Capture Frame
def move_to_capture_frame():
    home_frame.forget()
    capture_frame.pack(fill='both', expand=1)
    show_camera_in_capture_frame()

#Function to navigate to home frame
def move_to_home_frame():
    splash_screen_frame.forget()
    capture_frame.forget()
    home_frame.pack(fill='both', expand=1)

#Function to close all windows
def close():
    root.destroy()

#Function to Increase Brightness of webcam
def increase_brightness():
    bright = bright + 5
    camera.set(cv2.CAP_PROP_BRIGHTNESS, (bright))

#Function to decrease Brightness of webcam
def decrease_brightness():
    bright = bright - 5
    if bright < 0:
        bright = 0
    camera.set(cv2.CAP_PROP_BRIGHTNESS, (bright))

#Function to Increase focus of webcam
def increase_focus():
    focus = focus + 5
    camera.set(cv2.CAP_PROP_FOCUS, (focus))

#Function to decrease focus of webcam
def decrease_focus():
    focus = focus - 5
    if focus < 0:
        focus = 0
    camera.set(cv2.CAP_PROP_FOCUS, (focus))

#Initialize Frames
splash_screen_frame = tk.Frame(root)
capture_frame = tk.Frame(root, bg="#4a81ff")
home_frame = tk.Frame(root, bg="#4a81ff")

#Splash Screen Frame Properties
logo = ImageTk.PhotoImage(Image.open("iRead-tts logo.png"))
logo1 = Label(splash_screen_frame, image=logo)
logo1.place(relx=0.5, rely=0.5, anchor=CENTER)

#Home Frame Properties
logoHome = ImageTk.PhotoImage(Image.open("iRead-tts logo2.jpg"))
logoHome2 = Label(home_frame, image=logoHome, bg="#4a81ff")
logoHome2.place(relx=0.5, rely=0.25, anchor=CENTER)
logout_icon = PhotoImage(file=r"C:\Users\Lance\Desktop\TextDetection\signout1.png")
logout_icon_image = logout_icon.subsample(1,1)
logoutButton = tk.Button(home_frame, image = logout_icon_image, bg="#4a81ff", command=close)
logoutButton.config(height=25, width=25)
h1 = tk.Label(home_frame, text="Welcome to iRead-tts", font=("century gothic", 20, "bold"), bg="#4a81ff", fg="black")
h2 = tk.Label(home_frame, text="iRead-tts is a text detection AI software with", 
            font=("century gothic", 12, "bold"), 
            bg="#4a81ff", 
            fg="black").place(relx=0.5, rely= 0.45, anchor=CENTER)
h3 = tk.Label(home_frame, text="Text to Speech feature", 
            font=("century gothic", 12, "bold"), 
            bg="#4a81ff", 
            fg="black").place(relx=0.5, rely= 0.48, anchor=CENTER)
ProceedButton = tk.Button(home_frame,text="Proceed to Camera", font=("century gothic", 15, "bold"), bg="#4a81ff", fg="black", command=move_to_capture_frame)
logoutButton.grid(column=0,row=0)
h1.place(relx=0.5, rely= 0.4, anchor=CENTER)
ProceedButton.place(relx=0.5, rely=0.6, anchor=CENTER)

#Capture Frame Properties
l1 = tk.Label(capture_frame, text="Camera", font=("century gothic", 26, "bold"), bg="#4a81ff", fg="black").pack()
f1 = LabelFrame(capture_frame, bg="blue")
f1.pack()
L1 = Label(f1, bg="blue")
L1.pack()
camera = cv2.VideoCapture(0)
    #Camera Settings
bright = 128
focus = 0
camera.set(cv2.CAP_PROP_BRIGHTNESS,(bright))
camera.set(cv2.CAP_PROP_FOCUS, (focus))
readTextLabel = Label(capture_frame, text="[Text will appear here]", font=("century gothic", 14, "bold"), bg="#4a81ff", fg="black")
readTextLabel.pack()
ReadButton = tk.Button(capture_frame,text="Read", font=("century gothic", 15, "bold"), bg="#4a81ff", fg="black", command=tesseract).place(x=210, y=750)
Back = tk.Button(capture_frame,text="Back to Home", font=("century gothic", 15, "bold"), bg="#4a81ff", fg="black", command=move_to_home_frame).place(x=165, y=800)

#Buttons for Brightness and Focus modifications
#ps: these features may only work on webcams/cameras who contains these features
increase_brightness = PhotoImage(file=r"C:\Users\Lance\Desktop\TextDetection\increase_brightness_icon.png")
increase_brightness_image = increase_brightness.subsample(1,1)
increase_brightness_button = tk.Button(capture_frame, image = increase_brightness_image, bg="#4a81ff", command=increase_brightness)
increase_brightness_button.config(height=25, width=25)
increase_brightness_button.place(x=30, y=750)

decrease_brightness = PhotoImage(file=r"C:\Users\Lance\Desktop\TextDetection\decrease_brightness_icon.png")
decrease_brightness_image = decrease_brightness.subsample(1,1)
decrease_brightness_button = tk.Button(capture_frame, image = decrease_brightness_image, bg="#4a81ff", command=decrease_brightness)
decrease_brightness_button.config(height=25, width=25)
decrease_brightness_button.place(x=30, y=800)

increase_focus = PhotoImage(file=r"C:\Users\Lance\Desktop\TextDetection\increase_focus_icon.png")
increase_focus_image = increase_focus.subsample(1,1)
increase_focus_button = tk.Button(capture_frame, image = increase_focus_image, bg="#4a81ff", command=increase_focus)
increase_focus_button.config(height=25, width=25)
increase_focus_button.place(x=420, y=750)

decrease_focus = PhotoImage(file=r"C:\Users\Lance\Desktop\TextDetection\decrease_focus_icon.png")
decrease_focus_image = decrease_focus.subsample(1,1)
decrease_focus_button = tk.Button(capture_frame, image = decrease_focus_image, bg="#4a81ff", command=decrease_focus)
decrease_focus_button.config(height=25, width=25)
decrease_focus_button.place(x=420, y=800)

#main
show_splash_screen() #display splash screen then start with home frame
root.mainloop()