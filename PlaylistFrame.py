from tkinter import *
from tkinter import font
from tkmacosx import Button
import ProjTools as pt
import PlaylistDB as p_db
import PlaylistViewer as viewer


class PlayListFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.pL = pt.create_Frame_label(root, 'Your Playlists')
        self.libRoot = root

        self.l_scrollBar = Scrollbar(self.libRoot)
        self.l_scrollBar.place(relx=0.1, rely=0.35, anchor=CENTER)
        self.my_list = Listbox(self.libRoot, yscrollcommand=self.l_scrollBar.set, width=43)
        self.my_list.update_idletasks()
        self.my_list.place(relx=0.15, rely=0.20)
        self.l_scrollBar.config(command=self.my_list.yview)
        self.lib_scroll()

        u_font = font.Font(family='Helvetica', size=16)
        self.refresh_button = Button(root, text='Refresh', font=u_font, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                                     activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', padx=5,
                                     command=self.__get_refresh)
        self.refresh_button.place(relx=0.99, rely=0.965, anchor=SE)

        self.select_button = Button(root, text='Select', font=u_font, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                                    activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', padx=5,
                                    command=self.__get_playlist_viewer)
        self.select_button.place(relx=0.99, rely=0.27, anchor=SE)

        self.delete_button = Button(root, text='Delete', font=u_font, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                                    activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', padx=5,
                                    command=self.__delete)
        self.delete_button.place(relx=0.99, rely=0.37, anchor=SE)

    def lib_scroll(self):
        self.my_list.delete(0, END)
        cur = p_db.conn.cursor()
        for x in cur.execute("SELECT title FROM playlist"):
            x = str(x)[2:-3]
            self.my_list.insert(END, str(self.my_list.size() + 1) + ". " + x)

    def __get_refresh(self):
        self.lib_scroll()

    def __get_playlist_viewer(self):
        title = str(self.my_list.get(self.my_list.curselection())).lstrip('0123456789.- ')
        mp3_paths = p_db.get_paths_by_title(title)
        text = p_db.get_info_by_title(title)
        viewer.PlaylistViewer(mp3_paths, text, title)

    def __delete(self):
        title = str(self.my_list.get(self.my_list.curselection())).lstrip('0123456789.- ')
        p_db.remove_playlist(title)
        title = self.my_list.curselection()
        self.my_list.delete(title)
