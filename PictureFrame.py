import os
import tkinter as tk
from PIL import Image, ImageTk
import random

# Set the DISPLAY environment variable to the local display
os.environ["DISPLAY"] = ":0.0"

class ImageLoop:
    def __init__(self, imageList):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.config(cursor ="none", background="black")
        self.imageList = imageList
        self.currentImg = random.choice(self.imageList)
        self.img = Image.open(self.currentImg)
        self.displayImg = ImageTk.PhotoImage(self.img)
        print("initialized")

    def start_loop(self):
        self.imgLabel = tk.Label(self.root, image=self.displayImg, borderwidth=0)
        self.imgLabel.pack()
        print("start loop called")

        while True:
            self.currentImage = ImageTk.PhotoImage(Image.open(random.choice(self.imageList)))
            self.imgLabel.configure(image=self.currentImage)
            print("While Loop Running")
            self.root.update()
            self.root.after(30000)

        self.mainloop()

def build_image_list():
    imgList=[]
    path = "images"
    for file in os.listdir(path):
        if file.lower().endswith('.jpg'):
            imgList.append('images/'+file)
    return(imgList)

imgList = build_image_list()

pictureLoop = ImageLoop(imgList)
pictureLoop.start_loop()
