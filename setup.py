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
    start.write("from src.data_scrapper import fetch_and_save_data\n")
    start.write("from src.settings import *\n")
    start.write("import sys\n")
    start.write("if len(sys.argv) == 2:\n")
    start.write('   print(f"{OKGREEN}[INFO]{ENDC}: {BOLD}DELAY_BETWEEN_LOOPS={sys.argv[1]}, DELAY_BETWEEN_STOPS={DELAY_BETWEEN_STOPS}{ENDC}") \n')
    start.write("   fetch_and_save_data(loops_delay=float(sys.argv[1]))\n")
    start.write("elif len(sys.argv) == 3:\n")
    start.write('   print(f"{OKGREEN}[INFO]{ENDC}: {BOLD}DELAY_BETWEEN_LOOPS={sys.argv[1]}, DELAY_BETWEEN_STOPS={sys.argv[2]}{ENDC}")\n')
    start.write("   fetch_and_save_data(loops_delay=float(sys.argv[1]), stops_delay=float(sys.argv[2]))\n")
    start.write("else:\n")
    start.write("   print(f'{OKGREEN}[INFO]{ENDC}: {BOLD}DELAY_BETWEEN_LOOPS={DELAY_BETWEEN_LOOPS}, DELAY_BETWEEN_STOPS={DELAY_BETWEEN_STOPS}{ENDC}')\n")
    start.write("   fetch_and_save_data()")

if not os.path.exists("data"):
    print(f"{OKGREEN}[INFO]{ENDC}: {BOLD}Created directory {WARNING}data{ENDC}.{ENDC}")
    os.mkdir("data")
else:
    print(f"{OKGREEN}[INFO]{ENDC}: {BOLD}Directory {WARNING}data{ENDC} already exists.{ENDC}")

if not os.path.exists("src/.env"):
    print(f"{OKGREEN}[INFO]{ENDC}: {BOLD}Created {WARNING}src/.env{ENDC} file. You can get {WARNING}WEATHER_API_KEY{ENDC} here: {OKBLUE}https://openweathermap.org/{ENDC}")
    with open("src/.env", "w") as env:
        env.write("WEATHER_API_KEY=<YOUR API KEY>")
else:
    print(f"{OKGREEN}[INFO]{ENDC}: {BOLD}File {WARNING}src/.env{ENDC} already exists.{ENDC}")
print(f"{OKGREEN}[INFO]{ENDC}: {WARNING}Make sure that your API KEYS are fine, after that run {BOLD}start.py{ENDC}: {OKBLUE}python3 start.py{ENDC}.")
