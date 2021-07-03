import SongDB as s_db
import ProjTools as pt


class Playlist:
    def __init__(self, current_playlist, playlist_name, date):
        self.playlist_name = playlist_name
        self.playlist_creation_date = date
        self.paths = ''
        self.string_info = '\nPlaylist Name: ' + self.playlist_name + '\n' + \
                           'Creation Date: ' + self.playlist_creation_date + '\n' + 'Attributes: ' + '\n'

        for i in current_playlist:
            self.string = pt.listToString(s_db.get_tape_info(str(i)))
            self.paths += str(i) + ','
            self.string_info += '-> ' + self.string + '\n'

        self.paths = self.paths.strip(',')

    def __str__(self):
        return self.string_info
