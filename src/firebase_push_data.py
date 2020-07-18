from src.settings import db
from src.helpers import report_error
from datetime import date
import time


def firebase_push_data(vehicles: list, weather: object, flow_data: object, doc="bus-data") -> bool:
    if not vehicles:
        return True

    for vehicle in vehicles:
        data = {
            "tripId":           vehicle.get("tripId"),
            "routeId":          vehicle.get("routeId"),
            "stop":             vehicle.get("stop"),
            "patternText":      vehicle.get("patternText"),
            "direction":        vehicle['direction'],
            "delay":            vehicle.get("actualRelativeTime"),
            "time":             time.strftime('%H:%M'),
            "date":             str(date.today()),
            "weekday":          date.weekday(date.today()),
            "weather":          weather['weather'][0]['main'],
            "temp":             weather['main']['temp'],
            "currSpeed":        flow_data.get("flowSegmentData").get("currentSpeed"),
            "currTravelTime":   flow_data.get("flowSegmentData").get("currentTravelTime")
        }
        try:
            db.child(doc).push(data)
        except Exception as err:
            report_error(err)
            return False
    return True
