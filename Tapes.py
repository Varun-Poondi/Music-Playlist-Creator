class Tape:
    def __init__(self, path, author, name):
        # What defines a tape
        # All tapes are formatted in a particular way. Author - Title
        self.video_path = path
        self.video_title = author + '-' + name
        self.video_author = author
        self.video_name = name

    def change_name(self, name):
        self.video_name = name
        self.video_title = self.video_author + "-" + self.video_name

    def change_author(self, author):
        self.video_author = author
        self.video_title = self.video_author + "-" + self.video_name

    def change_path(self, path):
        self.video_path = path
