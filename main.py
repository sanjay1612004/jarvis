import tkinter as tk
import cv2
from PIL import Image, ImageTk

# Create a class for the video player
class VideoPlayer:
    def __init__(self, root, video_source, width, height):
        self.root = root
        self.video_source = video_source
        self.width = width
        self.height = height
        
        # Set the tkinter window size and center it
        self.root.geometry(f"{self.width}x{self.height}+{int((root.winfo_screenwidth() - self.width) / 2)}+{int((root.winfo_screenheight() - self.height) / 2)}")
        
        # Create a canvas to display video frames
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        # Open the video source using OpenCV
        self.vid = cv2.VideoCapture(self.video_source)

        # Start the video update loop
        self.update_video()

        # Create a button and place it on top of the canvas
        #self.add_button = tk.Button(self.root, text="Add", bg="#4CAF50", fg="white", command=self.on_button_click)
        self.canvas.create_window(self.width // 2, self.height - 30)#, window=self.add_button)  # Center button at the bottom

        
        # self.info_label = tk.Label(root, text="Waiting for video...", fg="white", bg="black", font=("Helvetica", 14))
        # self.info_label.pack()

    def update_video(self):
        ret, frame = self.vid.read()
        if ret:
            frame = cv2.resize(frame, (self.width, self.height))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img_tk = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
            self.canvas.image = img_tk
            self.root.after(10, self.update_video)
        else:
            self.vid.release()
            print("First video finished.")
            self.play_next_video("siri.mp4")
            
    def play_next_video(self, next_video_path):
        self.vid = cv2.VideoCapture(next_video_path)
        if not self.vid.isOpened():
            print(f"Error: Cannot open {next_video_path}")
            return
        self.update_video()
        import threading
        threading.Thread(target=self.on_button_click).start()
    
    # def update_label(self, text):
    #     """Update the info label text"""
    #     self.info_label.config(text=text)

        
    def on_button_click(self):
        import Sppech
        from Sppech import listen
        import speech_recognition as sr
        import pyttsx3 
        import pywhatkit
        import wikipedia
        import datetime
        import time
        import os
        import openai
        import google.generativeai as genai
        import pyautogui   
        from plyer import notification
        import requests
        from bs4 import BeautifulSoup    
        import speedtest     
        print("Running Sppech.commands()")

        # text = listen()  # Get the recognized text from speech
        # if text:
        #     self.update_label(f"You said: {text}")
        # else:
        #     self.update_label("No speech detected.")

        Sppech.commands()  # <-- This is your function call

   
        import threading

        def run_commands():
            import Sppech
            import speech_recognition as sr
            import pyttsx3 
            import pywhatkit
            import wikipedia
            import datetime
            import time
            import os
            import openai
            import google.generativeai as genai
            import pyautogui   
            from plyer import notification
            import requests
            from bs4 import BeautifulSoup    
            import speedtest     
            print("Running Sppech.commands()")
            Sppech.commands()  # <- Won't freeze the GUI now

        threading.Thread(target=run_commands).start()

# Create the main tkinter window
root = tk.Tk()
root.title("Jarvis")
root.configure(bg="black")
# Set window size
window_width = 640
window_height = 580

# Path to video
video_path = "loadvideo.mp4"

# Launch VideoPlayer
player = VideoPlayer(root, video_path, window_width, window_height)

# Start the tkinter event loop
root.mainloop()
