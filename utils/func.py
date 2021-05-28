from __future__ import unicode_literals
from youtubesearchpython import VideosSearch
from datetime import datetime
from dotenv import load_dotenv
from .Exceptions import *
from pathlib import Path
import threading
import youtube_dl
import platform
import glob
import os

def is_date_actual(dataBaseDatetime: datetime) -> bool:
    """
    Функция для проверки времяни.
    """
    return dataBaseDatetime == datetime.now()

def organizer(query: str) -> list:
    """
    Функция подготавливает данные из таблицы.
    """
    data = []
    for row in query.dicts():
        strDict = {}
        for key in row:
            strDict[key] = str(row[key])
        data.append(strDict)
    return data

def check_atr_lenght(data: dict, count: int) -> DictTooManyAtrs:
    """
    Функция проверяет колличество поданных аргументов.
    """
    if (len(data.keys()) != count):
        raise DictTooManyAtrs()

def is_first_launch() -> bool:
    """
    Функция проверяет есть ли база данных.\n
    Если ее нет то создает .env файл.

    """
    try:
        f = open("database.sqlite")
    except IOError:
        f = open(".env", "w")
        f.write("CLIENT_ID=\nCLIENT_SECRET=")
        f.close()
        return True
    finally:
        f.close()
        return False

def get_spotify_tokens() -> dict:
    """
    Функция берет токены из .env файла.
    """
    load_dotenv()
    spotify_tokens = {}
    spotify_tokens['id'] = os.getenv('CLIENT_ID')
    spotify_tokens['secret'] = os.getenv('CLIENT_SECRET')
    return spotify_tokens

def get_songs(sp: dict) -> list:
    """
    Возвращает название песни и артиста.
    """
    tracks_list = []

    for track in sp['tracks']['items']:
        tr_name = track['track']['name']
        tr_artist_name = track['track']['artists'][0]['name']
        tracks_list.append(f'{tr_name} {tr_artist_name}')
    
    return tracks_list

def get_playlist_data(sp: dict) -> list:
    """
    Возвращает обложку описание и тд.
    """
    return {
        "title": sp['name'],
        "description": sp["description"],
        "id": sp["id"],
        "cover": sp["images"][0]["url"]
    }

def get_songs_paths() -> list:
    """
    Функция вернет массив с песнями, а точнее пути к ним.
    """
    return glob.glob(get_music_path() + "/*.mp3")

def get_music_path() -> str:
    """
    Функция вернет путь к папке с музыкой.
    """
    home_dir = str(Path.home())
    return home_dir + '/SpotifyAlarm'

def title_to_url(playlist: str) -> list:
    """
    Функция переводит название песен в url для youtube.
    """
    y_playlist = []
    for song in playlist.split(','):
        y_playlist.append(VideosSearch(song, limit = 1))
    return y_playlist

def download_music(playlist: list) -> bool:
    """
    Функция скачивает музыку .
    """
    try:
        Path(get_music_path()).mkdir(parents=True, exist_ok=True)
    except FileExistsError:
        files = glob.glob(get_music_path())
        for f in files:
            os.remove(f)

    ydl_opts = {
        'outtmpl': str(get_music_path()) + '/' + '%(id)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download(playlist)
        except youtube_dl.utils.DownloadError:
            #TODO Разобраться с этой проблемой! Вроде все равно файл скачивается...
            pass

def start_thread(func, daemon: bool, *func_args) -> None:
    """
    Функция запускает отдельный поток с функцией.
    """
    x = threading.Thread(target=func, args=(func_args), daemon=daemon)
    x.start()

def inspect_request(db_wrapper, mp) -> bool:
    """
    Проверяет не нужно ли включить будильник.
    """
    while True:
        for row in db_wrapper.select_all().dicts():
            if is_date_actual(row["alarm_time"]) == True:
                if row["downloaded"] != True:
                    download_music(title_to_url(row["playlist"]))
                    db_wrapper.update_by_id(
                        row["id"],
                        downloaded=1
                    )
                if row["downloaded"] == 1 and row["is_worked"] == 0:
                    db_wrapper.update_by_id(
                        row["id"],
                        is_worked=1
                    )
                    start_thread(mp.play, False, get_songs_paths())
