from typing import List
from project.album import Album

class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return

        self.albums.append(album)

        return


    def remove_album(self, album_name):
        try:
            album = next(filter(lambda a: a.name == album_name, self.albums))
        except StopIteration:
            return

        if album.published:
            return

        self.albums.remove(album)

        return f"Album {album_name} has been removed"

    def details(self):
        pass