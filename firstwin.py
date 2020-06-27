from tkinter import *


def dome(txt):
    print("hello")
    print(txt)


rootwin = Tk()
alabel = Label(rootwin, text="helo mutha, dont press button 1")
alabel.pack()
button1 = Button(rootwin, text="button 1", command=dome)
button2 = Button(rootwin, text="button 2", command = lambda: dome('fine'))
button1.pack()
button2.pack()
dome('startin')
rootwin.mainloop()
