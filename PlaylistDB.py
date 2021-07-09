import sqlite3
import ProjTools as pt
import numpy as np

conn = sqlite3.connect('playlist_library.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS playlist (
            title text,
            date text,
            info text, 
            paths text
            )""")


def add_playlist(playlist):
    with conn:
        c.execute("INSERT INTO playlist VALUES (:title, :date, :info, :paths)",
                  {'title': playlist.playlist_name,
                   'date': playlist.playlist_creation_date,
                   'info': playlist.string_info,
                   'paths': playlist.paths})


def get_playlist_by_title(title):
    c.execute("Select * FROM playlist WHERE title=?", (title,))
    return pt.db_validator(c.fetchall(), 0, 0)


def get_info_by_title(title):
    c.execute("Select info FROM playlist WHERE title=?", (title,))
    return pt.db_validator(c.fetchall(), 0, 0)


def get_paths_by_title(title):
    c.execute("Select paths FROM playlist WHERE title=?", (title,))
    s = pt.db_validator(c.fetchall(), 0, 0)
    arr = np.array(s.split(','))
    return arr
