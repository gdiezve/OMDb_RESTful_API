from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from constants import *


def get_clean_input(inp):
    """
    Function that cleans the input to use it as key in our cache.
    :param inp: input search introduced by the user.
    :return: the cleaned input in string format.
    """
    stop_words_en = stopwords.words('english')
    stop_words_es = stopwords.words('spanish')

    inp_tokens = word_tokenize(inp)

    inp_clean = [w for w in inp_tokens if w not in stop_words_en]
    inp_clean = [w for w in inp_clean if w not in stop_words_es]
    inp_clean = ''.join(inp_clean)

    return inp_clean


def get_clean_response(response):
    """
    Function that cleans the API response in order to obtain the desired fields specified in MOVIE_DATA and SERIES
    data constants.
    :param response: API response in dict format.
    :return: cleaned response from the API.
    """
    clean_response = {}

    if response['Type'] == 'movie':
        for item in response:
            if item in MOVIE_DATA:
                clean_response.update({item: response[item]})
    elif response['Type'] == 'series':
        for item in response:
            if item in SERIES_DATA:
                clean_response.update({item: response[item]})

    return clean_response
