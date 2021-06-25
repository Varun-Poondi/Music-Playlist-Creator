from tkinter import *
import ProjTools as pt


global_playlist = []

class PlayList:
    def __init__(self, name, array):
        print(name)
        self.playlist_name = name
        self.playlist_array = array
        for i in range(len(self.playlist_array)):
            print(str(i+1) + ':', self.playlist_array[i].__str__())
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


