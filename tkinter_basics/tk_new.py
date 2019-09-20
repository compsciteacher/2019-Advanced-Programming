#HCD 2019
#new_button v.1
from tkinter import *
COLOR1='blue'
COLOR2='red'

def b1_click(*args):
    print(COLOR1)
def b2_click(*args):
    print(COLOR2)
def set_huge(*args):
    root.geometry('1000x1000')
root = Tk()
root.title("The colored buttons window!")
root.geometry('200x200')
mainframe = Frame(root,width=100,height=100)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.anchor(CENTER)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


b1=Button(mainframe, text="BLUE", command=b1_click,bg=COLOR1).grid(column=0, row=0, sticky=(N,W,E,S))
b2=Button(mainframe, text="RED", command=b2_click,bg=COLOR2).grid(column=0, row=1, sticky=(N,W,E,S))
huge=Button(mainframe, text="huge", command=set_huge,bg='white').grid(column=0, row=2, sticky=(N,W,E,S))


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', b1_click)

root.mainloop()


