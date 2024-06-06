from tkinter import *
from PIL import ImageTk, Image
import os  # files k andaar navigate kr ssakte hein


def rotate_image():
    global counter
    img_label.config(image=img_array[counter % len(img_array)])
    counter = counter + 1


counter = 1

root = Tk()

root.title("WALLPAPER VIEWER")
root.geometry("300x400")
root.configure(background="blue")
files = os.listdir("./res")
print(files)

img_array = []
for file in files:

    img = Image.open(os.path.join("./res", file))
    resizedimg = img.resize((200, 300))
    img_array.append(ImageTk.PhotoImage(resizedimg))
img_label = Label(root, image=img_array[0])
img_label.pack(pady=(15, 10))

next_btn = Button(
    root, text="Next", bg="white", fg="black", width=28, height=2, command=rotate_image
)
next_btn.pack()

root.mainloop()
