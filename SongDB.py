import sqlite3

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
