from tkinter import *
from tkinter import font
import Library as lib
import ProjTools as pt
import numpy as np

global_playlist = []

class PlayList:
    def __init__(self, playlist_name, playlist_array):
        print(playlist_name)

        for i in range(len(playlist_array)):
            print(str(i+1) + ':', playlist_array[i].__str__())
        return


class PlayListFrame(Frame, PlayList):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.pL = pt.create_Frame_label(root, 'Your Playlists')
        self.p_scrollBar = Scrollbar(root)
        self.p_scrollBar.place(relx=0.1, rely=0.35, anchor=CENTER)

        self.my_list = Listbox(root, yscrollcommand=self.p_scrollBar.set)
        self.my_list.insert(END, global_playlist)

        self.my_list.place(relx=0.15, rely=0.20)
        self.p_scrollBar.config(command=self.my_list.yview)



        return


