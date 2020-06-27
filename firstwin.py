from tkinter import *


def dome(txt):
    print("hello")
    print(txt)


rootwin = Tk()
alabel = Label(rootwin, text="helo mutha, dont press button 1")
alabel.pack()

button2 = Button(rootwin, text="button 2", command = lambda: dome('fine'))
button2.pack()

frame = Frame(rootwin, bg="blue")
frame.pack(expand=True, fill=BOTH)
button1 = Button(frame, text="button 1", command=dome)
button1.pack()


dome('startin')
rootwin.mainloop()
