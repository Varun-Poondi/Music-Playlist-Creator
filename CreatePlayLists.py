from tkinter import *
from tkmacosx import Button
from PlayLists import PlayList
import tkinter.font as font
import Library as lb


class CreatePlayList(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.lib = lb.Library()
        self.current_playlist = []
        self.current_playlist_name = ""

        u_font = font.Font(family='Helvetica', size=16)

        home_label = Label(root, text='Playlist Creator', font=font.Font(family='Helvetica', size=20), bg='#EBDEF0',
                           bd=3)
        home_label.place(relx=0.5, rely=0.1, anchor=CENTER)

        n_label = Label(root, text='Playlist Name: ', font=u_font, bg='#EBDEF0', bd=3)
        n_label.place(x=20, y=50)

        self.search_label = Label(root, text='Song Name: ', font=u_font, bg='#EBDEF0', bd=3)
        self.search_label.place(x=20, y=85)

        self.n_entry = Entry(master=root, width=40, bg='pink', fg='black', borderwidth=3)
        self.n_entry.place(x=150, y=50)
        self.search_entry = Entry(master=root, width=40, bg='pink', fg='black', borderwidth=3)
        self.search_entry.place(x=150, y=85)

        self.add_button = Button(root, text='Add', font=u_font, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                                 activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', padx=5,
                                 command=self.__get_add)
        self.add_button.place(relx=0.88, rely=0.50, anchor=SE)

        self.add_button = Button(root, text='Submit', font=u_font, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                                 activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', padx=5,
                                 command=self.__get_create)
        self.add_button.place(relx=0.88, rely=0.965, anchor=SE)

    def __get_add(self):
        search_result = self.lib.find_tape(self.search_entry.get())
        if search_result is None:
            self.search_entry.delete(0, END)
            self.search_entry.insert(0, 'Song Was not found in you library.')
        else:
            print(search_result.title + " was found in your library")
            self.current_playlist.append(search_result)
        self.search_entry.delete(0, END)

    def __get_create(self):
        self.n_entry.delete(0, END)
        self.search_entry.delete(0, END)
        PlayList(self.n_entry.get(), self.current_playlist)
        self.n_entry.delete(0, END)
