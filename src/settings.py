from dotenv import load_dotenv
import os

# GET ENVIROMENT VARIABLES
load_dotenv()

# WEATHER API settings / keys
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_REQUEST_LIMIT = 5
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather?q=Kraków&appid=' + WEATHER_API_KEY

# AZURE MAPS API settings / keys
AZURE_ACCESS_TOKEN = os.getenv("AZURE_ACCESS_TOKEN")
AZURE_SUBSCRIPTION_KEY = os.getenv("AZURE_SUBSCRIPTION_KEY")
AZURE_REQUEST_LIMIT = 3

# Firebase setup
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")
FIREBASE_AUTH_DOMAIN = "ids-store.firebaseapp.com"
FIREBASE_DATABASE_URL = "https://ids-store.firebaseio.com"
FIREBASE_PROJECT_ID = "ids-store"
FIREBASE_STORAGE_BUCKET = "ids-store.appspot.com"


# Default line number
LINE_NO = "139"

STOP_BASE_URL = 'http://91.223.13.70/internetservice/services/passageInfo/stopPassages/stop?stop='
STOPS_URL = 'http://91.223.13.70/internetservice/geoserviceDispatcher/services/stopinfo/stops?left=-658000000&bottom=-324000000&right=648000000&top=324000000'

# scrapping settings
DELAY_BETWEEN_STOPS = 1.2
DELAY_BETWEEN_LOOPS = 20

# colors definition
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

STOPS = {
 '100': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838593',
 '101': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838594',
 '102': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838595',
 '103': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838596',
 '105': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838597',
 '189': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838598',
 '107': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838599',
 '109': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838600',
 '110': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838601',
 '742': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838602',
 '112': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838603',
 '113': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838604',
 '324': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838605',
 '117': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838606',
 '120': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838607',
 '122': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838608',
 '123': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838609',
 '124': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838610',
 '125': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838611',
 '127': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838612',
 '128': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838613',
 '129': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838614',
 '130': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838615',
 '131': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838616',
 '133': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838617',
 '106': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838618',
 '136': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838619',
 '578': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838620',
 '208': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838659',
 '209': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838660',
 '210': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838661',
 '211': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838662',
 '212': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838663',
 '213': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838664',
 '214': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838665',
 '215': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838666',
 '217': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838667',
 '218': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838668',
 '220': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838669',
 '221': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838670',
 '222': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838671',
 '223': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838672',
 '224': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838673',
 '225': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838674',
 '227': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838676',
 '229': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838677',
 '230': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838678',
 '232': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838679',
 '233': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838680',
 '235': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838681',
 '237': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838682',
 '238': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838683',
 '239': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838684',
 '240': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838685',
 '242': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838686',
 '243': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838687',
 '244': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838688',
 '245': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838689',
 '247': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838690',
 '248': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838691',
 '249': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838692',
 '250': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838693',
 '252': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838694',
 '253': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838695',
 '255': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838696',
 '257': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838697',
 '258': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838698',
 '259': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838699',
 '260': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838700',
 '263': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838701',
 '265': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838702',
 '267': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838703',
 '268': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838704',
 '269': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838705',
 '270': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838706',
 '273': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838707',
 '275': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838708',
 '277': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838709',
 '278': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838710',
 '280': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838711',
 '283': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838712',
 '285': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838713',
 '287': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838714',
 '297': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838716',
 '301': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838717',
 '304': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838718',
 '405': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838720',
 '422': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838721',
 '424': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838722',
 '451': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838724',
 '501': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838726',
 '502': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838727',
 '503': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838728',
 '572': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838730',
 '601': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838731',
 '605': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838732',
 '608': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838733',
 '610': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838734',
 '637': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838736',
 '642': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838737',
 '662': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838739',
 '664': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838740',
 '669': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838741',
 '902': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838743',
 '904': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838745',
 '271': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838749',
 '192': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838761',
 '160': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838788',
 '116': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838789',
 '469': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838791',
 '484': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838793',
 '537': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838873',
 '704': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305838941',
 '264': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839099',
 '219': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839105',
 '274': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839167',
 '114': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839171',
 '134': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839172',
 '137': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839173',
 '138': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839174',
 '139': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839175',
 '141': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839176',
 '142': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839177',
 '143': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839178',
 '144': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839179',
 '149': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839180',
 '151': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839181',
 '152': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839182',
 '154': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839183',
 '158': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839184',
 '159': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839185',
 '162': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839186',
 '163': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839187',
 '164': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839188',
 '168': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839190',
 '169': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839191',
 '171': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839192',
 '172': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839193',
 '173': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839194',
 '174': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839195',
 '175': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839196',
 '178': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839197',
 '179': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839198',
 '181': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839199',
 '182': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839200',
 '183': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839201',
 '184': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839202',
 '193': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839203',
 '194': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839204',
 '201': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839205',
 '202': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839206',
 '203': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839207',
 '204': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839208',
 '207': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839209',
 '478': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839211',
 '111': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839252',
 '161': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839253',
 '722': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839258',
 '743': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839334',
 '234': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839366',
 '140': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839374',
 '352': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839375',
 '427': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839376',
 '773': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839399',
 '714': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839408',
 '176': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839438',
 '228': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839456',
 '135': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839464',
 '254': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839465',
 '156': 'http://91.223.13.70/internetservice/services/routeInfo/routeStops?routeId=8095257447305839504',
 }