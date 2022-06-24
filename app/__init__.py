"""This is the app demonstrates logging configuration and unit testing"""

import http.client
import json
import logging
import logging.config
import logging.config
import os
import pandas as pd
from dotenv import load_dotenv
from ratelimiter import RateLimiter
import locale


class Config(object):
    """This provides configuration information"""
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
    LOG_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'logs'))


@RateLimiter(max_calls=1, period=1)
def weather_forecast_api(city, days=2):
    """This makes a request to hotels on rapid api and saves the request to the hotels_api_response logger"""
    # This creates an HTTP connection to make a request
    """Makes the request to the weather forecast API"""
    conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': str(os.getenv('RAPID_API_KEY')),  # gets the rapid API key from the .env file
        'X-RapidAPI-Host': "weatherapi-com.p.rapidapi.com"
    }
    try:
        # this makes the actual request.
        conn.request("GET", '/forecast.json?q=' + str(city) + '&days=' + str(days), headers=headers)
    except Exception as e:
        app_log = logging.getLogger("errors")
        app_log.error(e, exc_info=True)
    # this gets the response data
    res = conn.getresponse()
    # this reads the response data and returns it as a python object

    data = res.read()

    return data.decode("utf-8")


def get_city_from_user():
    """Returns the city the user inputs"""
    # Gets the city from the user
    return input("What City do you want to know about? ")


def get_city_population(city):
    """searches the worldcities.csv file for the city information and returns it"""
    city_info = get_city_info(city)
    return int(city_info.population.to_string(index=False))


def get_city_current_condition(city):
    """searches the weather api to get the current condition of the city"""
    api_response = json.loads(weather_forecast_api(city))
    api_logging(api_response)
    return str(api_response["current"]["condition"]["text"])


def get_city_forecast_response(city):
    """searches the weather api to get the current condition of the city"""
    api_response = json.loads(weather_forecast_api(city))
    print(api_response)
    return str(api_response["location"]["name"])

def get_city_lng_lat(city):
    """searches csv for city info and returns it"""
    city_info = get_city_info(city)
    lng = float(city_info.lng.to.string(index=False))
    lat = float(city_info.lat.to.string(index=False))
    lng_lat = (lng, lat)
    return lng_lat

def setup():
    """Setup functions to run when app starts"""
    load_dotenv()
    setup_logs()
    locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'
    os.system('cls')


def print_banner():
    """Prints the banner title"""
    print("\t**********************************************")
    print("\t***  Welcome to City Information Service   ***")
    print("\t**********************************************")


def main():
    """This is the main function that is run"""
    setup()
    print_banner()
    # Gets the city from the console input
    city = get_city_from_user()
    # gets the population of the city the user input
    population = get_city_population(city)
    # gets the current conditions of the city
    condition_text = get_city_current_condition(city)
    # Prints out the information
    print(f"The Population of {city} is {population:n} and the weather is {condition_text}")


def api_logging(message):
    """Logs the message to the api response log file"""
    log = logging.getLogger("api_response")
    log.info(message)


def get_city_info(city, rows=419):
    """Queries the wordcities.csv file """
    df = pd.read_csv(os.path.join(Config.BASE_DIR, '..', 'data', '../data/worldcities.csv'), nrows=rows)
    return df.query('city_ascii == @city')


def setup_logs():
    # set the name of the apps log folder to logs
    logdir = Config.LOG_DIR
    # make a directory if it doesn't exist
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    # this loads the log configuration
    logging.config.dictConfig(LOGGING_CONFIG)


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'just_message': {
            'format': '%(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file.handler.errors': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(Config.LOG_DIR, 'errors.log'),
            'maxBytes': 10000000,
            'encoding': 'utf-8',
            'backupCount': 5,
        },
        'file.handler.api_response': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(Config.LOG_DIR, 'api_response.json'),
            'encoding': 'utf-8',
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.default_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(Config.LOG_DIR, 'root_logger_default.log'),
            'maxBytes': 10000000,
            'encoding': 'utf-8',
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default', 'file.handler.default_file'],
            'level': 'DEBUG',
            'propagate': False
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default', 'file.handler.default_file'],
            'level': 'DEBUG',
            'propagate': False
        },
        'api_response': {
            'handlers': ['file.handler.api_response'],
            'level': 'INFO',
            'propagate': False
        },
        'errors': {  # if __name__ == '__main__'
            'handlers': ['default', 'file.handler.errors'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

if __name__ == '__main__':
    """This causes the app to run"""
    main()
