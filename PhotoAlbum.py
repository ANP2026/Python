from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("My Photo Album")
window.geometry("400x420")

title = Label(window, text= "My Photo Album", bg= "purple", fg="white", padx=10, pady=10, width=40)
imageFile = Image.open("coding.png")
imageFile = imageFile.resize((300, 180))
photo = ImageTk.PhotoImage(imageFile)
pic = Label(window, image=photo)
pic.pack(pady=5)

def show_message():
    messagebox.showinfo("Great, you clicked the photo!")
msg_btn = Button(window, text="Click to View", bg= "blue", fg="white", command=show_message)
msg_btn.pack(pady=5)
def show_details():
    top = Toplevel()
    top.title("Photo Details")
    top.geometry("200x120")
    info = Label(top, text="Taken on: July 14, 2026")
    info.pack(pady=10)
    place = Label(top, text="Location: My Garden")
    place.pack()
    top.mainloop()
details_button = Button(window, text="See details", bg="green", fg="white", command=show_details)
details_button.pack(pady=10)
window.mainloop()