from tkinter import *

window = Tk()
window.title("Personal Bio Form")
window.geometry("450x450")
window.config(bg= "light yellow")

formFrame=Frame(window, bg="white", padx=50, pady=20)
formFrame.grid(row= 0, column=0, padx=30, pady=30)

titleLabel = Label(formFrame, text= "Personal Bio Form", bg= "light green", fg="black", width=40)
titleLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

nameLabel = Label(formFrame, text= "Name", bg= "light blue", fg= "black", width=10)
nameLabel.grid(row=1, column=0, padx=5, pady=5)

ageLabel = Label(formFrame, text="Age", bg="light blue", fg="black", width=10)
ageLabel.grid(row=2, column=0, padx=5, pady=5)

hobbyLabel = Label(formFrame, text="Hobby", bg="light blue", fg="black", width=10)
hobbyLabel.grid(row=3, column=0, padx=5, pady=5)

aboutLabel = Label(formFrame, text="About Me", bg="light blue", fg="black", width=10)
aboutLabel.grid(row=4, column=0, padx=5, pady=5)

nameEntry = Entry(formFrame, width=30)
nameEntry.grid(row=1, column=1, pady=5)
 
ageEntry = Entry(formFrame, width=30)
ageEntry.grid(row=2, column=1, pady=5)
 
hobbyEntry = Entry(formFrame, width=30)
hobbyEntry.grid(row=3, column=1, pady=5)
 
aboutText = Text(formFrame, width=23, height=5)
aboutText.grid(row=4, column=1, pady=5)

 
def show_bio():
    name = nameEntry.get()
    age = ageEntry.get()
    hobby = hobbyEntry.get()
    about = aboutText.get("1.0", END).strip()
    resultLabel.config(
        text="Hello, " + name + "!" " Age: " + age + "" " Hobby: " + hobby + "" " About: " + about
    ) 
submitButton = Button(formFrame, text="Show My Bio", bg="purple", fg="white", command=show_bio)
submitButton.grid(row=5, column=0, columnspan=2, pady=15)
 

resultLabel = Label(formFrame, text="Your bio will appear here.", bg="lightyellow", fg="black", width=35, height=5)
resultLabel.grid(row=6, column=0, columnspan=2, pady=10)
window.mainloop()
 

