from pytube import *
import datetime


class Tape:
    def __init__(self, link, path):
        def __seconds_to_minutes(seconds):
            return str(datetime.timedelta(seconds=seconds))

        self.video = YouTube(link)  # get video
        self.thumbnail = self.video.thumbnail_url  # get jpg
        self.artist = self.video.author
        self.title = self.video.title
        self.duration_seconds = self.video.length
        self.duration_format = __seconds_to_minutes(self.video.length)
        self.publish_date = self.video.publish_date
        self.video_path = path

