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
    start.write("fetch_and_save_data()")

print(f"{OKGREEN}[INFO]{ENDC}: {BOLD}Created directory {WARNING}data{ENDC}.{ENDC}")
os.mkdir("data")


print(f"{OKGREEN}[INFO]{ENDC}: {WARNING}Now you can run {BOLD}start.py{ENDC}")