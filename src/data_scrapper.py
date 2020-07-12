import os
import requests
import time
from datetime import date
import uuid

from src.settings import *

BASE_PATH = os.getcwd()
PATH_TO_SAVE = os.path.join(BASE_PATH, "data",
                            f"data_{str(uuid.uuid4())[:10]}_{str(date.today())}_{time.strftime('%H_%M')}.csv")

STOPS_139 = [stop['number'] for stop in requests.get(ROUTE_139_URL).json()['stops']]
STOPS_139_COORDINATES = {stop['shortName']:{'latitude': stop['latitude']/3599998.007, 'longitude':stop['longitude']/3600022.131} for stop in requests.get(STOPS_URL).json()['stops'] if stop['shortName'] in STOPS_139}


def save_vehicles(vehicles_to_save: list, weather: object, flow_data: object, path: str) -> bool:
    if not vehicles_to_save:
        return True
    try:
        with open(path, 'a+') as file:
            if os.stat(path).st_size == 0:
                file.write("tripId;routeId;stop;patternText;direction;delay;time;date;weekday;weather;temp;currSpeed;currTravelTime\n")
            for vehicle in vehicles_to_save:
                file.write(
                    f"{vehicle.get('tripId', None)};{vehicle.get('routeId', None)};{vehicle.get('stop', None)};" + \
                    f"{vehicle.get('patternText', None)};{vehicle['direction']};{vehicle.get('actualRelativeTime', None)};" + \
                    f"{time.strftime('%H:%M')};{str(date.today())};{date.weekday(date.today())};" + \
                    f"{weather['weather'][0]['main']};{weather['main']['temp']};" + \
                    f"{flow_data.get('flowSegmentData').get('currentSpeed', None)};{flow_data.get('flowSegmentData').get('currentTravelTime', None)}'\n"
                )
    except Exception as e:
        print(e)
        return False
    return True


def get_flow_data(lat, lng, token=AZURE_ACCESS_TOKEN, subscription_key=AZURE_SUBSCRIPTION_KEY,unit="KMPH"):
    try:
        return requests.get(f"https://atlas.microsoft.com/traffic/flow/segment/json?subscription-key={subscription_key}&api-version=1.0&style=absolute&zoom=9&query={lat},{lng}&unit={unit}",
                       headers={"Authorization": f"Bearer {token}"}).json()
    except Exception as e:
        print(f"{FAIL}[ERROR]:{ENDC}{WARNING}{e}{ENDC}")
        time.sleep(10)
        return {}


def get_weather():
    return requests.get(WEATHER_API_URL).json()


def fetch_and_save_data(loops_delay=DELAY_BETWEEN_LOOPS, stops_delay=DELAY_BETWEEN_STOPS) -> None:
    OLD_HISTORY = set([])
    TO_SAVE = list()

    weather_counter = 0
    azure_api_counter = {stopId: 0 for stopId in STOPS_139}
    flow_data_for_stop = {stopId: None for stopId in STOPS_139}

    while True:
        if weather_counter % WEATHER_REQUEST_LIMIT == 0:
            weather = get_weather()
            print(
                f"{OKGREEN}[INFO]{ENDC} {OKBLUE}{str(date.today())} {time.strftime('%H:%M')}:" + \
                f"{ENDC} {BOLD}Getting current weather from {OKBLUE}openweathermap.org{ENDC}{ENDC}"
            )
            weather_counter = 0

        for current_stop in STOPS_139:
            stop_url = STOP_BASE_URL + current_stop
            try:
                trips_on_stop = [trip for trip in requests.get(stop_url).json()['old'] if trip['patternText'] == "139"]
            except Exception as e:
                print(f"{FAIL}[ERROR]:{ENDC}{WARNING}{e}{ENDC}")
                time.sleep(10)
                continue

            for trip in trips_on_stop:
                if (trip['tripId'], trip['routeId'], current_stop) not in OLD_HISTORY:

                    if azure_api_counter[current_stop] % AZURE_REQUEST_LIMIT == 0:
                        print(
                            f"{OKGREEN}[INFO]{ENDC} {OKBLUE}{str(date.today())} {time.strftime('%H:%M')}:" + \
                            f"{ENDC} {BOLD}Getting flow info for stop no. {current_stop} from {OKBLUE}https://docs.microsoft.com/en-us/rest/api/maps/traffic/gettrafficflowsegment{ENDC}{ENDC}"
                        )
                        flow_data_for_stop[current_stop] = get_flow_data(lat=STOPS_139_COORDINATES[current_stop]['latitude'],
                                                  lng=STOPS_139_COORDINATES[current_stop]['longitude'])
                        azure_api_counter[current_stop] = 0
                    azure_api_counter[current_stop] += 1

                    OLD_HISTORY.add((trip['tripId'], trip['routeId'], current_stop))
                    trip['stop'] = current_stop
                    TO_SAVE.append(trip)

            if save_vehicles(TO_SAVE, weather, flow_data_for_stop[current_stop], PATH_TO_SAVE):
                if len(TO_SAVE) > 0:
                    print(
                        f"{OKGREEN}[INFO]{ENDC} {OKBLUE}{str(date.today())} {time.strftime('%H:%M')}:{ENDC} successfully saved" + \
                        f"{len(TO_SAVE)} records to {HEADER}{PATH_TO_SAVE}{ENDC} at stop no. {current_stop}."
                    )
                else:
                    print(
                        f"{OKGREEN}[INFO]{ENDC} {OKBLUE}{str(date.today())} {time.strftime('%H:%M')}:" + \
                        f"{ENDC} There is no new vehicles to save at stop no. {current_stop}."
                    )
            else:
                print(
                    f"{FAIL}[ERROR]{ENDC} {WARNING}{str(date.today())} {time.strftime('%H:%M')}:" + \
                    f"{ENDC} {HEADER}something went wrong.{ENDC}"
                )
            TO_SAVE = []
            time.sleep(stops_delay)
        weather_counter += 1
        print(
            f"{OKGREEN}[INFO]{ENDC} {OKBLUE}{str(date.today())} {time.strftime('%H:%M')}:" + \
            f"{ENDC} {BOLD}sleeping for {loops_delay} seconds.{ENDC}"
        )
        time.sleep(loops_delay)
