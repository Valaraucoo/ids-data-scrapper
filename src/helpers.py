from src.settings import *
import time
from datetime import date


def report_info(msg: str) -> None:
    print(
        f"{OKGREEN}[INFO]{ENDC} {OKBLUE}{str(date.today())} {time.strftime('%H:%M')}:" + \
        f"{ENDC} {BOLD}{msg}{ENDC}"
    )


def report_error(err: str, arg="") -> None:
    print(f"{FAIL}[ERROR] {str(date.today())} {time.strftime('%H:%M')}:{ENDC}{WARNING}{err} {args}{ENDC}")
