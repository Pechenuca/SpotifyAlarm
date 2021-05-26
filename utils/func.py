from datetime import datetime
from dotenv import load_dotenv
from .Exceptions import *
import threading
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

def start_thread(func: function, daemon: bool) -> None:
    """
    Функция запускает отдельный поток с функцией.
    """
    x = threading.Thread(target=func, args=(), daemon=daemon)
    x.start()

def inspect_request(db_wrapper, mp) -> bool:
    """
    Проверяет не нужно ли включить будильник.
    """
    #TODO нужно вставить ее куданибуть 
    while True:
        for row in db_wrapper.select_all().dicts():
            if is_date_actual(row["alarm_time"]) == True:
                start_thread(mp.play, daemon=False)

