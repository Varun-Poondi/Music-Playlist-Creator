from tkinter import *
import tkinter.font as font

class PlayList:
    def __init__(self, playlist_name, playlist):
        self.playlist = playlist
        print(playlist_name)
        for tabs in self.playlist:
            print(tabs.title)
        return


class PlayListFrame(Frame, PlayList):
    def __init__(self, root):
        Frame.__init__(self, root)

        home_label = Label(root, text='My PlayLists', font=font.Font(family='Helvetica', size=20), bg='#EBDEF0', bd=3)
        home_label.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.scrollbar = Scrollbar(root)
        self.scrollbar.place(relx=0.1, rely=0.35, anchor=CENTER)

        self.my_list = Listbox(root, yscrollcommand=self.scrollbar.set)
        for line in range(100):
            self.my_list.insert(END, "This is line number " + str(line))

        self.my_list.place(relx=0.15, rely=0.20)
        self.scrollbar.config(command=self.my_list.yview)

        return
