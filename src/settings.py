from dotenv import load_dotenv
import os

# GET ENVIROMENT VARIABLES
load_dotenv()

# WEATHER API settings / keys
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_REQUEST_LIMIT = 5
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather?q=Kraków&appid=" + WEATHER_API_KEY

# AZURE MAPS API settings / keys
AZURE_ACCESS_TOKEN = os.getenv("AZURE_ACCESS_TOKEN")
AZURE_SUBSCRIPTION_KEY = os.getenv("AZURE_SUBSCRIPTION_KEY")
AZURE_REQUEST_LIMIT = 10

# scrapping settings
LINE_NO = "139"
ROUTE_139_URL = 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839175'
STOP_BASE_URL = 'http://91.223.13.70/internetservice/services/passageInfo/stopPassages/stop?stop='
STOPS_URL = 'http://91.223.13.70/internetservice/geoserviceDispatcher/services/stopinfo/stops?left=-658000000&bottom=-324000000&right=648000000&top=324000000'

# script settings
DELAY_BETWEEN_STOPS = .5
DELAY_BETWEEN_LOOPS = 10

# colors definition
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'