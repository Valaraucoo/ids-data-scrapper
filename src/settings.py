from dotenv import load_dotenv
import os

# API KEYS
load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# scrapping settings
LINE_NO = "139"
ROUTE_139_URL = 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839175'
STOP_BASE_URL = 'http://91.223.13.70/internetservice/services/passageInfo/stopPassages/stop?stop='

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