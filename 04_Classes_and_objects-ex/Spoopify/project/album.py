from typing import Tuple
from typing import List
from project.song import Song


class Album:
    def __init__(self, name: str, *songs: Tuple[str]):
        self.name = name
        self.published: bool = False
        self.songs: List[Song] = list(songs)

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add{song.name}. It is a single"
        if self.published:
            return "Cannot add songs. Album already published"
        if song in self.songs:
            return "Song is already in the album"

        self.songs.append(song)

        return f"Song {song.name} has been added to the album {self.name}"

    def remove_song(self, song_name: str) -> str:
        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        if self.published:
            return "Cannot remove songs. Album is published."

        self.songs.remove(song)

        return f"Removed song {song.name} from album {self.name}."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self):
        songs = '\n'.join([f"== {s.get_info()}" for s in self.songs])

        return f"Album {self.name}\n" + \
            f"{songs}"
