import os
import sys

from src.helpers import report_error, report_info
from src.firebase_push_data import firebase_push_record


if len(sys.argv) < 2:
    report_info("Please enter a path(s) to file(s) or directory to load:")
    paths = input().split(" ")
else:
    paths = sys.argv[1:]


for path in paths:
    if os.path.isdir(path):
        for file_path in os.listdir(path):
            with open(os.path.join(path, file_path), "r") as file:
                for record in file.readlines()[1:]:
                    if firebase_push_record(record):
                        report_info(f"Successfully pushed record from {os.path.join(path, file_path)}.")
                    else:
                        report_error("Unfortunetly something gone wrong.")
    else:
        with open(path, "r") as file:
            for record in file.readlines()[1:]:
                if firebase_push_record(record):
                    report_info(f"Successfully pushed record from {path}.")
                else:
                    report_error("Unfortunetly something gone wrong.")
