import sqlite3
import ProjTools as pt

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
        c.execute("INSERT INTO music VALUES (:path, :title, :author, :name)",
                  {'path': tape.video_path,
                   'title': tape.video_title,
                   'author': tape.video_author,
                   'name': tape.video_name})


def get_music_by_author(author_name):
    c.execute("SELECT * FROM music WHERE author=:author", {'author': author_name})
    return pt.db_validator(c.fetchall(), 1, 0)


def get_music_by_name(name):
    c.execute("SELECT * FROM music WHERE name=?", (name,))
    return pt.db_validator(c.fetchall(), 0, 1)


def get_path_by_title(title):
    c.execute("SELECT path FROM music WHERE title=?", (title,))
    return pt.db_validator(c.fetchall(), 0, 0)


def update_music_path(title, path):
    with conn:
        c.execute("""UPDATE music SET path = "path WHERE title = :title""", {'title': title, 'path': path})


def update_music_title(tape, title):
    with conn:
        c.execute("""UPDATE music SET title = "title WHERE path = :path, author = :author, name = :name""",
                  {'title': title, 'author': tape.video_author, 'name': tape.video_name, 'path': tape.video_path})


def remove_tape(title):
    with conn:
        c.execute("DELETE from music WHERE title = :title", {'title': title})


def get_tape_info(path):
    c.execute("Select * FROM music WHERE path=?", (path,))
    result = c.fetchall()
    path_name = result[0][0]
    author = result[0][2]
    name = result[0][3]

    result = 'Video Info: ' + \
             '\n\tAuthor: ' + author + \
             '\n\tName: ' + name + \
             '\n\tPath: ' + path_name + '\n'

    return result


def get_lib_info():
    cur = conn.cursor()
    for row in cur.execute("SELECT title FROM music"):
        print(row)
