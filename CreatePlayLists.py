import os
from tkinter import *
from tkinter import filedialog
from tkmacosx import Button, CircleButton
import tkinter.font as font
import datetime as dt
import SongDB as s_db
import PlaylistDB as p_db
import Tapes as tp
import Playlists as pl
import ProjTools as pt
import numpy as np


class CreatePlayList(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.current_playlist = []
        self.current_playlist_name = ""

        u_font = font.Font(family='Helvetica', size=16)
        self.or_label = Label(root, text='Please enter in the song name or search path.',
                              font=font.Font(family='Helvetica', size=16), bg='#EBDEF0', fg='red', bd=10).place(
            relx=0.515, rely=0.35, anchor=CENTER)

        self.home_label = pt.create_Frame_label(root, 'PlayList Creator')
        self.name_label = Label(root, text='Playlist Name: ', font=u_font, bg='#EBDEF0', bd=3)
        self.name_label.place(x=20, y=50)
        self.search_label = Label(root, text='Song Name: ', font=u_font, bg='#EBDEF0', bd=3)
        self.search_label.place(x=20, y=130)
        self.find_song_path_label = Label(root, text='Enter Path: ', font=u_font, bg='#EBDEF0', bd=3)
        self.find_song_path_label.place(x=20, y=160)

        self.name_entry = Entry(master=root, width=40, bg='pink', fg='black', borderwidth=3)
        self.name_entry.place(x=150, y=50)
        self.search_entry = Entry(master=root, width=40, bg='pink', fg='black', borderwidth=3)
        self.search_entry.place(x=150, y=130)
        self.find_song_path_entry = Entry(master=root, width=40, bg='pink', fg='black', borderwidth=3)
        self.find_song_path_entry.place(x=150, y=160)
        self.find_song_path_entry.insert(0, '/User/username/..../song_name')

        self.add_button = Button(root, text='Add', font=u_font, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                                 activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', padx=5,
                                 command=self.__get_add)
        self.add_button.place(relx=0.88, rely=0.80, anchor=SE)
        self.submit_button = Button(root, text='Submit', font=u_font, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                                    activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', padx=5,
                                    command=self.__get_create)
        self.submit_button.place(relx=0.88, rely=0.965, anchor=SE)

        self.clear_button = CircleButton(root, text='CE', font=font.Font(family='Helvetica', size=12), bg='#A3E4D7',
                                         fg='#5F4B8B', borderless=1,
                                         activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', radius=20,
                                         command=self.__get_clear)
        self.clear_button.place(relx=0.98, rely=0.40, anchor=SE)

        load_button = Button(root, text='Search Path', font=u_font, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                             activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', padx=5,
                             command=self.__get_load)

        load_button.place(relx=0.016, rely=0.74)

    # /Users/varunpoondi/Desktop/mp4-Music/Playboi Carti- 9 AM in Calabasas remix(prod by Adrian).mp4

    def __get_load(self):
        self.find_song_path_entry.delete(0, END)
        self.music_file = filedialog.askopenfilename()
        self.find_song_path_entry.insert(0, self.music_file)

    def __get_add(self):
        self.current_playlist_name = self.name_entry.get()
        if self.search_entry.get() != '':
            search_result = s_db.get_music_by_name(self.search_entry.get())
            if search_result is None:
                self.search_entry.delete(0, END)
                self.search_entry.insert(0, 'Song Was not found in you library.')
            else:
                music_path = s_db.get_path_by_title(search_result)
                print("Song was found in your library")
                self.current_playlist.append(music_path)
                self.search_entry.delete(0, END)
        else:
            flag = pt.file_checker(self.find_song_path_entry)
            if not flag:
                self.find_song_path_entry.delete(0, END)
                self.find_song_path_entry.insert(0, 'Invalid File Path! Please try again.')
            else:
                path = self.find_song_path_entry.get()
                arr = path.split('/')
                song_title = arr[-1]
                parse = song_title.split('-')
                author = parse[0]
                song = parse[-1]
                song = str(song)[:-4]

                author = pt.format_vars(author)
                song = pt.format_vars(song)

                tape = tp.Tape(path, author, song)
                s_db.add_tape(tape)
                self.current_playlist.append(tape.video_path)
                print('song added')
                s_db.get_lib_info()

    def __get_create(self):
        if p_db.get_playlist_by_title(self.current_playlist_name) is None:
            my_array = np.array(self.current_playlist)
            date = dt.date.today()
            current_date = str(date.month) + "-" + str(date.day) + "-" + str(date.year)
            playlist = pl.Playlist(my_array, self.current_playlist_name, current_date)
            p_db.add_playlist(playlist)
            print(playlist.__str__())
            self.name_entry.delete(0, END)
        else:
            self.name_entry.delete(0, END)
            self.name_entry.insert(0, 'Playlist title already exists! Please choose a unique name.')

        self.search_entry.delete(0, END)
        self.find_song_path_entry.delete(0, END)

    def __get_clear(self):
        self.find_song_path_entry.delete(0, END)
        self.search_entry.delete(0, END)
