import os
import pip
from src.settings import *


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


print(f"{OKGREEN}[INFO]{ENDC}: {WARNING}Now you can run {BOLD}start.py{ENDC}")