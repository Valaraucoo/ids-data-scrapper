from src.settings import db, FIREBASE_BASE_DOC
from src.helpers import report_error
from datetime import date
import time

from typing import List, Dict


def firebase_push_data(vehicles: List[Dict], weather: object, flow_data: Dict, doc=FIREBASE_BASE_DOC) -> bool:
    if not vehicles:
        return True

    for vehicle in vehicles:
        data = {
            "tripId":           vehicle.get("tripId"),
            "routeId":          vehicle.get("routeId"),
            "stop":             vehicle.get("stop"),
            "patternText":      vehicle.get("patternText"),
            "direction":        vehicle.get("direction"),
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


def firebase_push_record(record: Dict, doc=FIREBASE_BASE_DOC) -> bool:
    record = record.strip().split(";")
    if len(record) != 13:
        for _ in range(13 - len(record)):
            record.append(None)
    data = {
        "tripId":           record[0],
        "routeId":          record[1],
        "stop":             record[2],
        "patternText":      record[3],
        "direction":        record[4],
        "delay":            record[5],
        "time":             record[6],
        "date":             record[7],
        "weekday":          record[8],
        "weather":          record[9],
        "temp":             record[10],
        "currSpeed":        record[11],
        "currTravelTime":   record[12]
    }
    doc = doc + "-" + data["patternText"]
    try:
        db.child(doc).push(data)
    except Exception as err:
        report_error(err)
        return False
    return True