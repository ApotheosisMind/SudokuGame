from tkinter import *
import pygame
import numpy as np
import turtle
from random import randint, shuffle
from time import sleep


window = Tk()
window.resizable(0,0)
window.minsize(790,600)
window.maxsize(790,600)
window.iconbitmap("sudoku.ico")
window.title("SB Production: sudoku")
window.configure(bg="#ffffff")
window.attributes("-alpha",0.9825)



difficultylvl = "easy"






def gamestart():
    if (difficultylvl == "easy"):
        grid = np.zeros((9,9))
        print(grid)


























def difficultyselecteasy():
    global difficultylvl
    global easybtn
    global mediumbtn
    global hardbtn
    difficultylvl = "easy"
    easybtn.configure(bg="#3cca54")
    mediumbtn.configure(bg="#ff3236")
    hardbtn.configure(bg="#ff3236")

def difficultyselectmedium():
    global difficultylvl
    global easybtn
    global mediumbtn
    global hardbtn
    difficultylvl = "medium"
    mediumbtn.configure(bg="#3cca54")
    easybtn.configure(bg="#ff3236")
    hardbtn.configure(bg="#ff3236")



def difficultyselecthard():
    global difficultylvl
    global easybtn
    global mediumbtn
    global hardbtn
    difficultylvl = "hard"
    hardbtn.configure(bg="#3cca54")
    mediumbtn.configure(bg="#ff3236")
    easybtn.configure(bg="#ff3236")




def mainmenu():
    settingframe.grid_forget()
    empty.grid(padx=330, pady=100, row=0)
    startbtn.grid(padx=330, pady=10, row=1)
    settingbtn.grid(padx=330, pady=5, row=2)


def settingclick():
    global easybtn
    global mediumbtn
    global hardbtn
    settingframe.grid(row=1, padx=185, pady= 200)
    empty.grid_forget()
    startbtn.grid_forget()
    settingbtn.grid_forget()
    easybtn = Button(settingframe, text="Easy", fg="#ffffff", relief="solid", bg="#3cca54", activebackground="#cb2226",
                      activeforeground="#ffffff", padx=23, pady=4, bd=0, command=difficultyselecteasy,
                      font=("comic sans ms", "12", "normal"))

    mediumbtn = Button(settingframe, text="Medium", fg="#ffffff", relief="solid", bg="#ff3236", activebackground="#cb2226",
                     activeforeground="#ffffff", padx=13, pady=4, bd=0, command=difficultyselectmedium,
                     font=("comic sans ms", "12", "normal"))

    hardbtn = Button(settingframe, text="Hard", fg="#ffffff", relief="solid", bg="#ff3236", activebackground="#cb2226",
                     activeforeground="#ffffff", padx=23, pady=4, bd=0, command=difficultyselecthard,
                     font=("comic sans ms", "12", "normal"))

    backbtn = Button(settingframe, text="\u2b9c Back", fg="#ffffff", relief="solid", bg="#4885ef", activebackground="#1855bf",
                     activeforeground="#ffffff", padx=12, pady=4, bd=0, command= mainmenu,
                     font=("comic sans ms", "12", "normal"))


    easybtn.grid(pady=10, padx=80, row=1, column=1)
    mediumbtn.grid(pady=10, padx=80, row=2, column=1)
    hardbtn.grid(pady=10, padx=80, row=3, column=1)
    backbtn.grid(pady=10, row=4, column=0)








empty = Button(window, text="", fg="#ffffff", relief = "solid", bg="#ffffff", activebackground="#ffffff",
                  activeforeground="#ffffff", padx=10, pady=4, bd=0, state= "disabled",
                  font=("comic sans ms", "11", "bold"))


startbtn = Button(window, text="\u2b9e START", fg="#ffffff", relief = "solid", bg="#4885ef", activebackground="#0836af",
                  activeforeground="#ffffff", padx=24, pady=4, bd=0, command= gamestart,
                  font=("comic sans ms", "12", "normal"))

settingbtn = Button(window, text="\u2699 SETTING", fg="#ffffff", relief = "solid", bg="#4885ef", activebackground="#0836af",
                  activeforeground="#ffffff", padx=14, pady=4, bd=0, command=settingclick,
                  font=("comic sans ms", "12", "normal"))


settingframe = Frame(window, relief = "solid", bg="#ffffff", height=400, width=400)





empty.grid(padx=330, pady=100, row=0)
startbtn.grid(padx=330, pady=10, row=1)
settingbtn.grid(padx=330, pady=5, row=2)







window.mainloop()
