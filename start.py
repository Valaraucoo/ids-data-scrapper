from src.data_scrapper import fetch_and_save_data
from src.settings import *
import sys
if len(sys.argv) == 2:
   print(f"{OKGREEN}[INFO]{ENDC}: {BOLD}LINE_NO={sys.argv[1]} DELAY_BETWEEN_LOOPS={DELAY_BETWEEN_LOOPS}, DELAY_BETWEEN_STOPS={DELAY_BETWEEN_STOPS}{ENDC}") 
   fetch_and_save_data(line_no=sys.argv[1])
elif len(sys.argv) == 3:
   print(f"{OKGREEN}[INFO]{ENDC}: {BOLD}LINE_NO={sys.argv[1]} DELAY_BETWEEN_LOOPS={sys.argv[2]}, DELAY_BETWEEN_STOPS={DELAY_BETWEEN_STOPS}{ENDC}")
   fetch_and_save_data(line_no=sys.argv[1],loops_delay=float(sys.argv[2]))
elif len(sys.argv) == 4:
   print(f"{OKGREEN}[INFO]{ENDC}: {BOLD}LINE_NO={sys.argv[1]} DELAY_BETWEEN_LOOPS={sys.argv[2]}, DELAY_BETWEEN_STOPS={sys.argv[3]}{ENDC}")
   fetch_and_save_data(line_no=sys.argv[1],loops_delay=float(sys.argv[2]), stops_delay=float(sys.argv[3]))
else:
   print(f'{OKGREEN}[INFO]{ENDC}: {BOLD}DELAY_BETWEEN_LOOPS={DELAY_BETWEEN_LOOPS}, DELAY_BETWEEN_STOPS={DELAY_BETWEEN_STOPS}{ENDC}')
   fetch_and_save_data()