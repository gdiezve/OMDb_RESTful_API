import constants
import sys


def exist_title(movies, series):
    """
    Function that throws an error when a movie o series doesn't exist in OMDb API.
    :param movies: movies that contain in the title the input search.
    :param series: series that contain in the title the input search.
    """
    if (movies['Response'] == 'False') & (series['Response'] == 'False'):
        sys.exit('Error: Title not found!')


def is_response_larger_than_max_results(movies, series):
    """
    Function that throws an error when the API response results are higher than 10.
    :param movies: movies that contain in the title the input search.
    :param series: series that contain in the title the input search.
    """
    if movies['Response'] == 'False':
        mov_res = 0
    else:
        mov_res = int(movies['totalResults'])

    if series['Response'] == 'False':
        ser_res = 0
    else:
        ser_res = int(series['totalResults'])

    if (mov_res > constants.MAX_RESULTS) | (ser_res > constants.MAX_RESULTS) | (
            mov_res + ser_res > constants.MAX_RESULTS):
        sys.exit('Error: the amount of results is higher than 10 and can not be displayed.')
