from SpotifyParser import SpotifyParser 
from MusicDownloader import MusicDownloader
#from Connector import Connector

#get playlist
sp = SpotifyParser('5VFBiAtuHsUK7FFxYkKJ9u')
spotifySongsArray = sp.getSongs()


# #donload songs
for i in range(0, len(spotifySongsArray)):
    md = MusicDownloader(spotifySongsArray[i])
    toDownload = md.findVideo()
    print(toDownload)
    md.dnSong(toDownload)

