import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyWorker():
    """
    Класс обертка вокруг spotipy.
    """

    def __init__(self, tokens: dict) -> None:
        """
        Входной атрибут словарь с токенами.
        """

        self.sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=tokens['id'],
                client_secret=tokens['secret']
            )
        )

    def find_playlist_by_id(self, id: str):
        """
        Находит плей-лист по id.\n
        Пример: '0XBa7XqP9FaBXNaZSAGmP8'
        """
        return self.sp.playlist(id)
