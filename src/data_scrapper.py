import os
import requests
import time
from datetime import date
import uuid

from src.settings import *
from src.helpers import report_error, report_info, fetch_error_handler
from src.firebase_push_data import firebase_push_data

@fetch_error_handler
def get_flow_data(lat, lng, token=AZURE_ACCESS_TOKEN, subscription_key=AZURE_SUBSCRIPTION_KEY,unit="KMPH") -> object:
    return requests.get(f"https://atlas.microsoft.com/traffic/flow/segment/json?subscription-key={subscription_key}&api-version=1.0&style=absolute&zoom=9&query={lat},{lng}&unit={unit}",
                       headers={"Authorization": f"Bearer {token}"}).json()

@fetch_error_handler
def get_weather() -> object:
    return requests.get(WEATHER_API_URL).json()


def fetch_and_save_data(line_no=LINE_NO, loops_delay=DELAY_BETWEEN_LOOPS, stops_delay=DELAY_BETWEEN_STOPS) -> None:
    LINE_NO = line_no
    try:
        ROUTE_LINE_URL = STOPS[LINE_NO]
    except KeyError as e:
        report_error(e, f"There is no bus line number {line_no}")
        raise KeyError()


    STOPS_LINE = [stop['number'] for stop in requests.get(ROUTE_LINE_URL).json()['stops']]
    STOPS_LINE_COORDINATES = {stop['shortName']:{'latitude': stop['latitude']/3599998.007, 'longitude':stop['longitude']/3600022.131} for stop in requests.get(STOPS_URL).json()['stops'] if stop['shortName'] in STOPS_LINE}

    OLD_HISTORY = set([])
    TO_SAVE = list()

    weather_counter = 0
    azure_api_counter = {stopId: 0 for stopId in STOPS_LINE}
    flow_data_for_stop = {stopId: None for stopId in STOPS_LINE}

    while True:
        if weather_counter % WEATHER_REQUEST_LIMIT == 0:
            weather = get_weather()
            report_info(f"Getting current weather from {OKBLUE}openweathermap.org{ENDC}")
            weather_counter = 0

        for current_stop in STOPS_LINE:
            stop_url = STOP_BASE_URL + current_stop
            try:
                trips_on_stop = [trip for trip in requests.get(stop_url).json()['old'] if trip['patternText'] == LINE_NO]
            except Exception as e:
                report_error(e)
                time.sleep(10)
                continue

            for trip in trips_on_stop:
                if (trip['tripId'], trip['routeId'], current_stop) not in OLD_HISTORY:

                    if azure_api_counter[current_stop] % AZURE_REQUEST_LIMIT == 0:
                        report_info(f"Getting flow info for stop no. {current_stop} from {OKBLUE}https://docs.microsoft.com/en-us/rest/api/maps/traffic/gettrafficflowsegment{ENDC}")
                        flow_data_for_stop[current_stop] = get_flow_data(
                                                lat=STOPS_LINE_COORDINATES[current_stop]['latitude'],
                                                lng=STOPS_LINE_COORDINATES[current_stop]['longitude']
                                                )
                        azure_api_counter[current_stop] = 0
                    azure_api_counter[current_stop] += 1

                    OLD_HISTORY.add((trip['tripId'], trip['routeId'], current_stop))
                    trip['stop'] = current_stop
                    TO_SAVE.append(trip)

            if firebase_push_data(TO_SAVE, weather, flow_data_for_stop[current_stop], FIREBASE_BASE_DOC + '-' + LINE_NO):
                if len(TO_SAVE) > 0:
                    report_info(f"saved {len(TO_SAVE)} records to {HEADER}Firebase/{FIREBASE_BASE_DOC + '-' + LINE_NO}{ENDC} at stop no. {current_stop}.")
                else:
                    report_info(f"There is no new vehicles to save at stop no. {current_stop}.")
            else:
                report_error(f"{HEADER}something went wrong.{ENDC}")
            TO_SAVE = []
            time.sleep(stops_delay)
        weather_counter += 1
        report_info("sleeping for {loops_delay} seconds.")
        time.sleep(loops_delay)
