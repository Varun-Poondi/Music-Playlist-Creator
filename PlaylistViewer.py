from tkinter import *
import tkinter.font as font
from tkmacosx import Button, CircleButton
from PIL import ImageTk, Image
import pygame


class PlaylistViewer:
    def __init__(self, mp3_paths, text, title):
        # root creation
        self.new_root = Toplevel()
        self.new_root.configure(bg='#EBDEF0')
        self.new_root.title('Playlist Viewer')
        self.new_root.maxsize(400, 550)
        self.new_root.minsize(400, 550)
        pygame.mixer.init()

        # stuff
        u_font = font.Font(family='Helvetica', size=16)
        self.text = text
        self.songs = mp3_paths
        self.playlist_status = True
        self.base_state = False
        self.song_load = False
        self.song_index = 0

        # default image
        image1 = Image.open("proj_images/default.png")
        image1 = image1.resize((300, 300))
        test = ImageTk.PhotoImage(image1)
        label1 = Label(master=self.new_root, image=test)
        label1.image = test
        label1.place(relx=0.5, rely=0.35, anchor=CENTER)

        # button images
        back_image = Image.open("proj_images/back.png")
        back_image = back_image.resize((400, 250))
        back_image = ImageTk.PhotoImage(back_image)

        front_image = Image.open("proj_images/front.png")
        front_image = front_image.resize((400, 200))
        front_image = ImageTk.PhotoImage(front_image)

        state_image = Image.open("proj_images/pause.png")
        state_image = state_image.resize((400, 200))
        self.base_image = ImageTk.PhotoImage(state_image)

        self.info_button = Button(self.new_root, text=title, font=u_font, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                                  activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', padx=5,
                                  command=self.__get_info)

        self.play_button = CircleButton(self.new_root, image=self.base_image, borderwidth=0, bg='#A3E4D7', fg='#5F4B8B',
                                        borderless=1, activebackground=('#AE0E36', '#D32E5E'),
                                        activeforeground='#E69A8D', radius=20)
        self.back_button = CircleButton(self.new_root, image=back_image, borderwidth=0, bg='#A3E4D7', fg='#5F4B8B',
                                        borderless=1, radius=20)
        self.front_button = CircleButton(self.new_root, image=front_image, borderwidth=0, bg='#A3E4D7', fg='#5F4B8B',
                                         borderless=1, radius=20)

        self.info_button.place(relx=0.5, rely=0.035, anchor=CENTER)
        self.play_button.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.back_button.place(relx=0.15, rely=0.7, anchor=CENTER)
        self.front_button.place(relx=0.845, rely=0.7, anchor=CENTER)

        self.play_button.config(command=lambda: self.__play(self.songs[self.song_index]))
        self.front_button.config(command=self.__next)
        self.back_button.config(command=self.__previous)

        self.new_root.mainloop()

    def __get_info(self):
        info_root = Toplevel()
        info_root.title('Playlist Description')
        info_root.configure(bg='#EBDEF0')
        info_root.maxsize(500, 250)
        info_root.minsize(500, 250)
        scroll = Scrollbar(info_root)
        scroll.place(relx=0.08, rely=0.05, heigh=203)
        playlist_info = Text(info_root, relief=SUNKEN, width=50, wrap=WORD, height=15, yscrollcommand=scroll.set)
        playlist_info.bind("<Key>", lambda e: "break")
        playlist_info.insert(INSERT, self.text)
        playlist_info.place(relx=0.5, rely=0.45, anchor=CENTER)
        scroll.config(command=playlist_info.yview)

    def __play(self, song):
        if not self.song_load:
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)
            self.song_load = True

        if not self.base_state:
            state_image = Image.open("proj_images/play.png")
            self.base_state = True
            pygame.mixer.music.unpause()

        else:
            state_image = Image.open("proj_images/pause.png")
            self.base_state = False
            pygame.mixer.music.pause()

        state_image = state_image.resize((425, 200))
        state_image = ImageTk.PhotoImage(state_image)
        self.play_button.configure(image=state_image)

    def __next(self):
        if self.song_index < len(self.songs)-1:
            self.song_index += 1
            self.song_load = False
            self.base_state = False
            self.__play(self.songs[self.song_index])
        else:
            print('This is the last song on the playlist!')

    def __previous(self):
        if self.song_index > 0:
            self.song_index -= 1
            self.song_load = False
            self.base_state = False
            self.__play(self.songs[self.song_index])
        else:
            print('You are at the beginning of the playlist!')
