import json

import requests


def top_rated():
    req = requests.get(
        "https://api.themoviedb.org/3/movie/top_rated?api_key=d10554b639e8af1d820f7ec858bc7a02&language=ru-US&page=1")
    response = req.json()
    s = ""
    for i in response['results']:
        s += i['title'] + "\n" + "Оригинальная озвучка  : " + i['original_language'] + "\n" + "Рейтинг: " + str(
            i['vote_average'])
        s += "\n"
        s += "\n"
    return s


def now_playing():
    req = requests.get(
        "https://api.themoviedb.org/3/movie/now_playing?api_key=d10554b639e8af1d820f7ec858bc7a02&language=en-US&page=1")
    response = req.json()
    s = ""
    for i in response['results']:
        s += i['title'] + "\n" + "Оригинальная озвучка  : " + i['original_language'] + "\n" + "Рейтинг: " + str(
            i['vote_average'])
        s += "\n"
        s += "\n"
    return s


def popular_actors():
    req = requests.get(
        "https://api.themoviedb.org/3/person/popular?api_key=d10554b639e8af1d820f7ec858bc7a02&language=en-US&page=1")
    response = req.json()
    s = ""
    for i in response['results']:
        s += i['name'] + "\n" + "Популярность : " + str(i['popularity']) + "\n" + "Гендер: " + str(
            i['gender'])
        s += "\n"
        s += "\n"
    return s
