import os
import pip

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])


with open('requirements.txt', 'r+') as file:
    print(f"{OKGREEN}[INFO]{ENDC}: {WARNING}Installing required packages.{ENDC}")
    for package in file:
        print(f"{OKGREEN}[INFO]{ENDC}: {BOLD}Installing required {WARNING}{package}{ENDC}.{ENDC}")
        import_or_install(package)


with open("start.py", 'w') as start:
    print(f"{OKGREEN}[INFO]{ENDC}: {BOLD}Creating {WARNING}start.py{ENDC}")
    start.write("""
import argparse 

from src.data_scrapper import fetch_and_save_data
from src.settings import *
from src.helpers import report_info

if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument("line_number", 
                        help="Bus line number, it must be one value from the specified list.", 
                        type=str)
   parser.add_argument("-l", "--loops", 
                        help="Delay between execution of the query loop.", 
                        type=float)
   parser.add_argument("-s", "--stops", 
                        help="Delay execution of the query between each stop per specified line_number.",
                        type=float)

   args = parser.parse_args()

   loops_delay = args.loops if args.loops else DELAY_BETWEEN_LOOPS
   stops_delay = args.stops if args.stops else DELAY_BETWEEN_STOPS

   report_info(f"Line number: {args.line_number}, loops delay: {loops_delay}, stops delay: {stops_delay}.")
   fetch_and_save_data(line_no=args.line_number, loops_delay=loops_delay, stops_delay=stops_delay)""")

if not os.path.exists("src/.env"):
    print(f"{OKGREEN}[INFO]{ENDC}: {BOLD}Created {WARNING}src/.env{ENDC} file. You can get {WARNING}WEATHER_API_KEY{ENDC} here: {OKBLUE}https://openweathermap.org/{ENDC}")
    with open("src/.env", "w") as env:
        env.write("WEATHER_API_KEY=<YOUR API KEY>\n")
        env.write("AZURE_ACCESS_TOKEN=<ACCESS TOKEN>\n")
        env.write("AZURE_SUBSCRIPTION_KEY=<SUBSCRIPTION KEY>\n")
        env.write("FIREBASE_API_KEY=<API KEY>\n")
else:
    print(f"{OKGREEN}[INFO]{ENDC}: {BOLD}File {WARNING}src/.env{ENDC} already exists.{ENDC}")
print(f"{OKGREEN}[INFO]{ENDC}: {WARNING}Make sure that your API KEYS are fine, after that run {BOLD}start.py{ENDC}: {OKBLUE}python3 start.py{ENDC}.")
