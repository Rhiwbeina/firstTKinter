from tkinter import *


def dome():
    print("hellllo")


rootwin = Tk()
alabel = Label(rootwin, text="helo mutha")
alabel.pack()
button1 = Button(rootwin, text="yo button 1", command=dome)

button1.pack()
dome()
rootwin.mainloop()
