class Playlist:
    def __init__(self, current_playlist, playlist_name, date):
        self.playlist_name = playlist_name
        self.playlist = current_playlist
        self.playlist_creation_date = date

    def __str__(self):
        string_info = '\nPlaylist Name: ' + self.playlist_name + '\n' + \
                      'Creation Date: ' + self.playlist_creation_date + '\n' + 'Attributes: ' + '\n'


        for i in self.playlist:
            string_info += str(i.title) + '\n'

        return string_info
