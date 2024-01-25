from tkinter import * # import tkinter library
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import os

Win = Tk() # Create a window
Win.title("FriendsList") # Give a name to the window
Win.geometry("700x500") # set the window size
Win.configure(background = "Yellow2")
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', background = 'lightblue', foreground = 'blue', width = 15, borderwidth=4, focusthickness=3, focuscolor='yellow')
style.map('TButton', background=[('active','red')])
path = "friends/"
pics = []
picON = False

def quit():
    answer = messagebox.askquestion("Confirm","Are you sure you wantto quit?")
    if answer == "yes":
        Win.destroy()
    else:
        messagebox.showinfo("Information","Keep Going!")
for file in os.listdir("friends/"):
    print(file)
def show():
    i = 0
    for file in os.listdir(path):
        print(file)
        pics.append(file)
        print(pics)
        file = os.path.join(path,file)
        print(file)
        for img in file:
            image = Image.open(img)
            print("path&filename: ", img)
            print("image: " + str(image))
            resizedImage = image.resize((105, 90), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(resizedImage)
            print(photo)
            imgLabel = Label(Win, image=photo)
            imgLabel.grid(row=1, column=1 + i, sticky=NE)
            imgLabel.image = photo
            i = i + 1



imgButton = ttk.Button(Win, text = "Show Friends", command= show)
imgButton.grid(row=0, column=1, sticky=NE)
imgButton = ttk.Button(Win, text = "Clear All", command= show)
imgButton.grid(row=0, column=2, sticky=NE)
imgButton = ttk.Button(Win, text = "Delete a Friend", command= show)
imgButton.grid(row=0, column=3, sticky=NE)
imgButton = ttk.Button(Win, text = "Add New Friend", command= show)
imgButton.grid(row=0, column=4, sticky=NE)
QuitButton = ttk.Button(Win, text= "Quit", command= Win.destroy)
QuitButton.grid(row = 0, column = 5, sticky= E)

Win.mainloop()
