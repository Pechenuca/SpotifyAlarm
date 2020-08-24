from proxy_requests import ProxyRequests, ProxyRequestsBasicAuth
from bs4 import BeautifulSoup
import requests

#--------------------#
# SpotifyParser 
# started 22.07.2020
# author mar4elkin
#--------------------#

#todo добавить больше проверок и поставть слипы


class SpotifyParser(object):
    """
    Класс для работы со spotify.
    На вход принимает конец ссылки на плейлист 
    """
    
    def __init__(self, playListId ):
        self.playListId = 'https://open.spotify.com/playlist/'+ playListId
        self.page = requests.get(self.playListId)

    
    def statusCode(self):
        """
        Производит проверку подключения к сайту
        """
        return int(self.page.status_code)

    def getSongs(self):
        """
        Парсинг страницы с альбомом
        """
        if self.statusCode() == 200:
            
            soup = BeautifulSoup(self.page.text, "html.parser")
            songsTitles = soup.findAll('span', class_='track-name')
            songsArtist = soup.findAll('span', class_='artists-albums')

            songs = []

            for j in range(0, len(songsTitles)):
                songs.append(songsTitles[j].text)

            for i in range(0, len(songsArtist)):
                songs[i] = songs[i] + " - " + songsArtist[i].text.split("•")[0].strip()

            return (songs, 1)

        else:
            return ('status code: ' + str(self.statusCode()) + ' url: ' + self.playListId, 0)