import sqlite3
import ProjTools as pt
from tkinter import *

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


def get_music_by_author(author):
    c.execute("SELECT * FROM music WHERE author=:author", {'author': author})
    result = c.fetchall()
    if len(result) == 0:
        result = None
    else:
        result = result[1]

    return result

def get_music_by_name(name):
    c.execute("SELECT * FROM music WHERE name=:name", {'name': name})
    result = c.fetchall()
    if len(result) == 0:
        result = None
    else:
        result = result[1]
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

def lib_scroll(root):
    cur = conn.cursor()
    l_scrollBar = Scrollbar(root)
    l_scrollBar.place(relx=0.1, rely=0.35, anchor=CENTER)

    my_list = Listbox(root, yscrollcommand=l_scrollBar.set, width=50)
    for x in cur.execute("SELECT title FROM music"):
        x = str(x)[2:-3]
        my_list.insert(END, x)

    my_list.place(relx=0.15, rely=0.20)
    l_scrollBar.config(command=my_list.yview)


class LibraryFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.label = pt.create_Frame_label(root, 'Your Songs')
        lib_scroll(root)


