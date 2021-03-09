import requests
from errors import *
from data_cleaning import *
from constants import *


def __get_movies(title):
    """
    Private function that returns the list of movies containing the input search in their title.
    :param title: input search obtain from the command line, inserted by the user.
    :return: API response in dict format.
    """
    params = {
        's': title,
        'type': 'movie'
    }

    response = requests.get(API_URL + API_KEY, params=params).json()
    return response


def __get_series(title):
    """
    Private function that returns the list of series containing the input search in their title.
    :param title: input search obtain from the command line, inserted by the user.
    :return: API response in dict format.
    """
    params = {
        's': title,
        'type': 'series'
    }

    response = requests.get(API_URL + API_KEY, params=params).json()
    return response


def __get_title_info(movie_id):
    """
    Private function used to obtain the complete information about a movie o series.
    :param movie_id: IMDb ID of the movie or series related with the input search.
    :return: dictionary with all the information about a movie or series.
    """
    params = {
        'i': movie_id,
    }

    response = requests.get(API_URL + API_KEY, params=params).json()

    clean_response = get_clean_response(response)

    return clean_response


def get_data(inp):
    """
    Function used to obtain information from OMDb API about the input search.
    :param inp: input search introduced by the user.
    :return: all movies and series related with the input search, in dict format.
    """
    movies = __get_movies(inp)
    series = __get_series(inp)

    exist_title(movies, series)
    is_response_larger_than_max_results(movies, series)

    search_dict = {}

    if movies['Response'] != 'False':
        for movie in movies['Search']:
            search_dict.update({'movie': __get_title_info(movie['imdbID'])})

    if series['Response'] != 'False':
        for show in series['Search']:
            search_dict.update({'series': __get_title_info(show['imdbID'])})

    return search_dict
