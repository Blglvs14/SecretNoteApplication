from tkinter import *
import os, sys
from PIL import ImageTk, Image



my_window = Tk()
my_window.minsize(400, 600)
my_window.title("Secret Notes")

f = open("text.txt", "a")

title = []
note = []
key = []

img = ImageTk.PhotoImage(Image.open("indir.png"))
panel = Label(my_window, image=img)
panel.pack(side="top", fill="both", expand="yes")

#image = ImageTk.PhotoImage(Image.open("indir.png"))
#test = ImageTk.PhotoImage(image)
#label = tkinter.Label(image=test)
#label.image = test

label1 = Label(text="Enter your title", font=('Arial',10,'bold'))
label1.pack()

entry1 = Entry()
entry1.pack()

label2 = Label(text="Enter your secret", font=('Arial',10,'bold'))
label2.pack()

text = Text(width=30 , height=15)
text.pack()

label3 = Label(pady=5,text="Enter master key", font=('Arial',10,'bold'))
label3.pack()

entry2 = Entry()
entry2.pack()

def encFunc():
    if entry1.get() == "" or entry2.get() == "" or text.get(1.0, END) == "":
        label4.config(text="Enter all gaps!", pady=5, bg="red", fg="white")
    else:
        secret = str(text.get(1.0, END))
        encoded = secret.encode()

        title.append(entry1.get())
        note.append(text.get(1.0, END))
        key.append(entry2.get())
        f.write(f"{entry1.get()}\n")
        f.write(f"{str(encoded)}\n")

        entry1.delete(0, END)
        text.delete(1.0, END)
        entry2.delete(0, END)

        print(key)

        '''for i in range(5):
            title.append(entry1.get())
            note.append(encoded)
            key.append(entry2.get())'''

def decFunc():
    if entry2.get() == "" or text.get(1.0, END) == "":
        label4.config(text="Enter your encrypted note or key!", bg="yellow")
    else:
        try:
            for n in range(5):
                if entry2.get() == key[n]:
                    result = bytes(text.get(1.0, END))
                    result.decode(entry2.get(), text.get("1.0", END))

                    entry1.delete(0, END)
                    text.delete(1.0, END)
                    entry2.delete(0, END)
                    text.insert("1.0", result)
                    break
                else:
                    label4.config(text="Enter true key!", bg="yellow")
        except:
            label4.config(text="Please enter encrypted text!")

button1 = Button(text="Save & Encrypt", command=encFunc)
button1.pack()

button2 = Button(text="Decrypt", command=decFunc)
button2.pack()

label4 = Label()
label4.pack()

my_window.mainloop()