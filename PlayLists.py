from tkinter import *
from tkmacosx import Button
import tkinter.font as font


class PlayLists(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        buttonFont = font.Font(family='Helvetica', size=16)
        self.my_playlists = Label(self, text='My Playlists', font=buttonFont, bg='#EBDEF0', bd=3)
        self.my_playlists.place(relx=0.2, rely=0.1, anchor=CENTER)

        # Travel Button
        self.cp_button = Button(self, text='Create PlayList', font=buttonFont, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                                activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D')
        self.cp_button.place(relx=0.75, rely=0.965, anchor=SW)

        return
