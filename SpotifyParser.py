from bs4 import BeautifulSoup
import requests

#--------------------#
# SpotifyParser 
# started 22.07.2020
# author mar4elkin
#--------------------#

#todo добавить больше проверок и поставть слипы


class SpotifyParser(object):
    
    def __init__(self, playListId ):
        self.playListId = 'https://open.spotify.com/playlist/'+ playListId
        self.page = requests.get(self.playListId)
    
    def statusCode(self):
        return int(self.page.status_code)
    
    def getSongs(self):
        if self.statusCode() == 200:
            
            soup = BeautifulSoup(self.page.text, "html.parser")
            songsTitles = soup.findAll('span', class_='track-name')
            songsArtist = soup.findAll('span', class_='artists-albums')

            songs = []

            for j in range(0, len(songsTitles)):
                songs.append(songsTitles[j].text)

            for i in range(0, len(songsArtist)):
                songs[i] = songs[i] + " - " + songsArtist[i].text.split("•")[0].strip()

            return songs

        else:
            return 'Spotify banned our ip :('
    
    

    
