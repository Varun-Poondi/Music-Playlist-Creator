import sqlite3

conn = sqlite3.connect('playlist_library.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS playlist (
            title text,
            songs text,
            name text
            )""")

def add_playlist(playlist):
    with conn:
        c.execute("INSERT INTO music VALUES (:path, :title, :author, :name)", {'path': tape.video_path, 'title': tape.video_title, 'author': tape.video_author, 'name': tape.video_name})

