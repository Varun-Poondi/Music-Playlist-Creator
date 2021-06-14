import tkinter as tk
from tkinter import CENTER
import pathlib
from pytube import YouTube
from tkmacosx import Button
import tkinter.font as font

SOUND = 'sample_click.m4a'


class YoutubeDownloader:
    def __init__(self, root):
        # Create Labels
        buttonFont = font.Font(family='Helvetica', size=16)

        self.link_label = tk.Label(root, text='Video Downloader', font=buttonFont, bg='#EBDEF0', bd=3)
        self.link_label.place(y=15, relx=0.5, rely=0.0, anchor=CENTER)
        self.link_label = tk.Label(root, text='Download Link', bd=3, font=buttonFont, bg='#EBDEF0')
        self.link_label.place(x=20, y=50)
        self.link_label = tk.Label(root, text='Save File as', bd=3, font=buttonFont, bg='#EBDEF0')
        self.link_label.place(x=20, y=85)
        self.link_label = tk.Label(root, text='Save File Path', bd=3, font=buttonFont, bg='#EBDEF0')
        self.link_label.place(x=20, y=120)
        self.link_label = tk.Label(root, text='File extension', bd=3, font=buttonFont, bg='#EBDEF0')
        self.link_label.place(x=20, y=155)

        # Create Entry
        self.link_entry = tk.Entry(master=root, width=40, bg='pink', fg='black', borderwidth=3)
        self.link_entry.place(x=150, y=50)
        self.name_entry = tk.Entry(master=root, width=40, bg='pink', fg='black', borderwidth=3)
        self.name_entry.place(x=150, y=85)
        self.path_entry = tk.Entry(master=root, width=40, bg='pink', fg='black', borderwidth=3)
        self.path_entry.place(x=150, y=120)
        self.ext_entry = tk.Entry(master=root, width=40, bg='pink', fg='black', borderwidth=3)
        self.ext_entry.place(x=150, y=155)

        # Create Download Button
        self.download_button = Button(root, text='Download', font=buttonFont, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                                      activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D',
                                      command=lambda: self.__get_link(root))
        self.download_button.place(y=70, relx=0.79, rely=0.5, anchor=CENTER)

        return

    def __downloader(self, link, save_path='', save_name='', extension='mp4'):
        video = YouTube(link)
        video_stream = video.streams.filter(progressive=True, file_extension=extension).order_by(
            'resolution').desc().first()
        video_stream.download(output_path=save_path, filename=save_name)
        return

    # def error_label(self, window):
    #    label = Label(window, text='Must fill both link and path entries')

    # Test link: https://www.youtube.com/watch?v=EddzRp8E2Dc
    # Test path: /Users/varunpoondi/Desktop/mp4-Music

    def __get_link(self, root):
        directory = pathlib.Path(self.path_entry.get())
        hold = self.path_entry.get()
        if hold == '':
            directory = ''
        print('dir', directory)
        flag = True
        if directory != '' and directory.exists():
            print('exits')
        else:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, 'Invalid File Path! Please try again.')
            flag = False
        print('pass')

        if flag:
            link = self.link_entry.get()
            path = self.path_entry.get()
            name = self.name_entry.get()
            ext = self.ext_entry.get()
            self.__downloader(link, path, name, ext)