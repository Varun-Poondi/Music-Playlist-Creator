import sqlite3
from tkinter import font
import ProjTools as pt
from tkinter import *
from tkmacosx import Button
import subprocess, sys

conn = sqlite3.connect('music_library.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS music (
            path text,
            title text,
            author text,
            name text
            )""")

def add_tape(tape):
    with conn:
        c.execute("INSERT INTO music VALUES (:path, :title, :author, :name)", {'path': tape.video_path, 'title': tape.video_title, 'author': tape.video_author, 'name': tape.video_name})


def get_music_by_author(author_name):
    c.execute("SELECT * FROM music WHERE author=:author", {'author': author_name})
    result = c.fetchall()
    if len(result) == 0:
        result = None
    else:
        result = result[1]

    return result

def get_music_by_name(name):
    c.execute("SELECT * FROM music WHERE name=?", (name,))
    result = c.fetchall()
    if len(result) == 0:
        result = None
    else:
        result = result[0][1]
    return result

def get_path_by_title(title):
    c.execute("SELECT * FROM music WHERE title=?", (title,))
    result = c.fetchall()
    if len(result) == 0:
        result = None
    else:
        result = result[0][0]
    return result

def update_music_path(tape, path):
    with conn:
        c.execute("""UPDATE music SET path = "path WHERE title = :title, author = :author, name = :name""", {'title': tape.video_title, 'author': tape.video_author, 'name': tape.video_name, 'path': path})

def update_music_title(tape, title):
    with conn:
        c.execute("""UPDATE music SET title = "title WHERE path = :path, author = :author, name = :name""", {'title': title, 'author': tape.video_author, 'name': tape.video_name, 'path': tape.video_path})

def remove_tape(tape):
    with conn:
        c.execute("DELETE from music WHERE author = :author AND name = :name", {'author': tape.video_author, 'name': tape.video_name})

def get_lib_info():
    cur = conn.cursor()
    for row in cur.execute("SELECT title FROM music"):
        print(row)



class LibraryFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.libRoot = root
        self.label = pt.create_Frame_label(root, 'Your Songs')

        self.l_scrollBar = Scrollbar(self.libRoot)
        self.l_scrollBar.place(relx=0.1, rely=0.35, anchor=CENTER)
        self.my_list = Listbox(self.libRoot, yscrollcommand=self.l_scrollBar.set, width=43)
        self.my_list.update_idletasks()
        self.my_list.place(relx=0.15, rely=0.20)
        self.l_scrollBar.config(command=self.my_list.yview)
        self.lib_scroll()

        u_font = font.Font(family='Helvetica', size=16)
        self.submit_button = Button(root, text='Refresh', font=u_font, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                                    activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', padx=5,
                                    command=self.__get_refresh)
        self.submit_button.place(relx=0.99, rely=0.965, anchor=SE)

        self.select_button = Button(root, text='Select', font=u_font, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                                    activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', padx=5,
                                    command=self.__get_selected)
        self.select_button.place(relx=0.99, rely=0.27, anchor=SE)



    def lib_scroll(self):
        self.my_list.delete(0, END)
        cur = conn.cursor()
        for x in cur.execute("SELECT title FROM music"):
            x = str(x)[2:-3]
            self.my_list.insert(END, str(self.my_list.size() + 1) + ". " + x)

    def __get_refresh(self):
        self.lib_scroll()

    def __get_selected(self):
        title = str(self.my_list.get(self.my_list.curselection()))
        title = title.lstrip('0123456789.- ')
        path = get_path_by_title(title)
        if path is None:
            print('Error, Path Error not found in Database')
        else:
            print("Now Playing .... " + title)
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, path])





