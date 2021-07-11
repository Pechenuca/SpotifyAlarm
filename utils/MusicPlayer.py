from pygame import mixer
import pygame


class MusicPlayer:
    """
    Класс для работы с pygame.\n
    В частности mixer.
    """

    def __init__(self) -> None:
        """
        Передается массив с песнями, а точнее путь к ним.
        """
        pygame.init()
        self.mixer = mixer
        self.mixer.init()

    def stop(self) -> None:
        """
        Останавливает воспроизведение песен.
        """
        self.mixer.music.stop()

    def play(self, songs: list) -> None:
        """
        Запускает плейлист.
        """

        self.mixer.music.load(songs.pop())
        self.mixer.music.queue(songs.pop())
        self.mixer.music.set_endevent(pygame.USEREVENT)
        self.mixer.music.play()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    if len(songs) > 0:
                        self.mixer.music.queue(songs.pop())
                    if len(songs) == 0:
                        self.stop()
