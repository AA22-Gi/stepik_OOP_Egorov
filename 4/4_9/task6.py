"""
В этой задаче мы создадим аналог плейлиста, для этого понадобится реализовать два класса Song и Playlist

Класс Song должен содержать:
    1)  метод __init__, который сохраняет в экземпляре два атрибута title и artist: название песни и исполнитель

Класс Playlist должен содержать:
    1)  метод __init__. , который создает в экземпляре атрибут songs. Изначально должен быть пустым списком;

    2)  метод __getitem__ , который возвращает песню из атрибута songs по индексу

    3)  метод __setitem__ , который добавляет песню в атрибут songs по указанному индексу.
        При этом нужно сдвинуть уже имеющиеся песни вправо,
        у которых индекс был до момента вставки равен или больше переданного

    4)  метод add_song, который добавляет песню в конец плейлиста
"""


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


class Playlist:
    def __init__(self):
        self.songs = []

    def __getitem__(self, item: int):
        if 0 <= item < len(self.songs):
            return self.songs[item]
        else:
            raise IndexError(f"Индекс {item} находится за пределами вектора")

    def __setitem__(self, key, value):
        self.songs.insert(key, value)

    def add_song(self, song: Song):
        if isinstance(song, Song):
            self.songs.append(song)


if __name__ == '__main__':
    playlist = Playlist()
    assert len(playlist.songs) == 0
    assert isinstance(playlist, Playlist)
    playlist.add_song(Song("Paradise", "Coldplay"))
    assert playlist[0].title == 'Paradise'
    assert playlist[0].artist == 'Coldplay'
    assert len(playlist.songs) == 1

    playlist[0] = Song("Resistance", "Muse")
    assert playlist[0].title == 'Resistance'
    assert playlist[0].artist == 'Muse'
    assert playlist[1].title == 'Paradise'
    assert playlist[1].artist == 'Coldplay'

    playlist[1] = Song("Helena", "My Chemical Romance")
    assert playlist[1].title == 'Helena'
    assert playlist[1].artist == 'My Chemical Romance'

    assert playlist[2].title == 'Paradise'
    assert playlist[2].artist == 'Coldplay'
    print('Good')
