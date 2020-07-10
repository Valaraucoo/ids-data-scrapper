import os
import requests
import time
from datetime import date
import uuid

from src.settings import *


STOPS_139 = [stop['number'] for stop in requests.get(ROUTE_139_URL).json()['stops']]
BASE_PATH = os.getcwd()
PATH_TO_SAVE = os.path.join(BASE_PATH, "data", f"bus_data{str(uuid.uuid4())[:10]}_{str(date.today())}_{time.strftime('%H:%M')}.csv")


def save_vehicles(vehicles_to_save: list, path: str) -> bool:
    if not vehicles_to_save: 
        return True
    try:
        with open(path, 'a+') as file:
            if os.stat(path).st_size == 0:
                file.write("tripId;routeId;stop;patternText;direction;delay;time;date;weekday\n")
            for vehicle in vehicles_to_save:
                file.write(f"{vehicle.get('tripId', None)};{vehicle.get('routeId',None)};{vehicle.get('stop',None)};{vehicle.get('patternText',None)};{vehicle['direction']};{vehicle.get('actualRelativeTime',None)};{time.strftime('%H:%M')};{str(date.today())};{date.weekday(date.today())}\n")
    except Exception as e:
        print(e)
        return False
    return True


def fetch_and_save_data(loops_delay=DELAY_BETWEEN_LOOPS, stops_delay=DELAY_BETWEEN_STOPS) -> None:
    OLD_HISTORY = set([])
    TO_SAVE = list()
    while True:
        for current_stop in STOPS_139:
            stop_url = STOP_BASE_URL + current_stop
            trips_on_stop = [trip for trip in requests.get(stop_url).json()['old'] if trip['patternText']=="139"]

            for trip in trips_on_stop:
                if (trip['tripId'],trip['routeId'], current_stop) not in OLD_HISTORY:
                    OLD_HISTORY.add((trip['tripId'],trip['routeId'], current_stop))
                    trip['stop'] = current_stop
                    TO_SAVE.append(trip)

            if save_vehicles(TO_SAVE, PATH_TO_SAVE):
                if len(TO_SAVE) > 0:
                    print(f"{OKGREEN}[INFO]{ENDC} {OKBLUE}{str(date.today())} {time.strftime('%H:%M')}:{ENDC} successfully saved {len(TO_SAVE)} records to {HEADER}{PATH_TO_SAVE}{ENDC} at stop no. {current_stop}.")
                else:
                    print(f"{OKGREEN}[INFO]{ENDC} {OKBLUE}{str(date.today())} {time.strftime('%H:%M')}:{ENDC} There is no new vehicles to save at stop no. {current_stop}.")
            else:
                print(f"{FAIL}[ERROR]{ENDC} {WARNING}{str(date.today())} {time.strftime('%H:%M')}:{ENDC} {HEADER}something went wrong.{ENDC}")
            TO_SAVE = []
            time.sleep(stops_delay)
        print(f"{OKGREEN}[INFO]{ENDC} {OKBLUE}{str(date.today())} {time.strftime('%H:%M')}:{ENDC} {BOLD}sleeping for {loops_delay} seconds.{ENDC}")
        time.sleep(loops_delay)

