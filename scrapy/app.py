import requests
import json
import multitasking
from statistics import mean
import pandas as pd

requests_ = requests.Session()

stations = requests_.get("http://api.gios.gov.pl/pjp-api/rest/station/findAll")
stations = json.loads(stations.content)

is_first = True


@multitasking.task
def save(station, sensor, values):
    global is_first
    book = {}
    book["geg_lat"] = station.get("gegrLat")
    book["geg_lon"] = station.get("gegrLon")
    book["district_name"] = station.get("city").get("commune").get("districtName")
    book["province_name"] = station.get("city").get("commune").get("provinceName")
    book["param_name"] = sensor.get("param").get("paramName")
    book["param_formula"] = sensor.get("param").get("paramFormula")
    book["values"] = values.get("values")

    columns = None
    if is_first:
        columns = list(book.keys())
        is_first = False

    df = pd.DataFrame([list(book.values())])

    df.to_csv("file.csv", mode="a", header=columns, encoding="utf-8")


def get_sensors(station, sensors):
    for sensor in sensors:
        sensorid = sensor.get("id")
        values = requests_.get(
            f"http://api.gios.gov.pl/pjp-api/rest/data/getData/{sensorid}"
        )
        values = json.loads(values.content)
        save(station, sensor, values)


def main():
    for station in stations:
        stationid = station.get("id")
        sensors = requests_.get(
            f"http://api.gios.gov.pl/pjp-api/rest/station/sensors/{stationid}"
        )
        sensors = json.loads(sensors.content)
        get_sensors(station, sensors)


main()

