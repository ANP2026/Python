from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Photo Album")
window.geometry("600x600")
window.configure(bg="light gray")

title = Label(window, text="Photo Album", bg="light blue", fg="black", padx=5, pady=5, width=20)
title.pack(pady=5)

photo = Image.open("trampoline.jpg")
photo = photo.resize((500, 400))
pic = ImageTk.PhotoImage(photo)
picture = Label(window, image=pic)
picture.pack(pady=0)

def react():
    messagebox.showinfo("Reaction", "That was fun!")
def details():
    messagebox.showinfo("Details", "Photo Tooken on July 15, 2026")
btn1=Button(window, text="Reaction", bg="light blue", fg="black", command=react)
btn2=Button(window, text="Details", bg="light blue", fg="black", command=details)
btn1.pack(pady=5)
btn2.pack(pady=5)

window.mainloop()