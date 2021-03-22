import requests
import json
from statistics import mean
import pandas as pd

stations = requests.get("http://api.gios.gov.pl/pjp-api/rest/station/findAll")

stations = json.loads(stations.content)


def get_sensors(sensors):
    for sensor in sensors:
        sensorid = sensor.get("id")
        values = requests.get(
            f"http://api.gios.gov.pl/pjp-api/rest/data/getData/{sensorid}"
        )
        values = json.loads(values.content)
        # print(
        #     values.get("key"),
        #     mean(
        #         [
        #             data.get("value")
        #             for data in values.get("values")[:24]
        #             if data.get("value")
        #         ]
        #     ),
        # )


def main():
    for station in stations:
        stationid = station.get("id")
        sensors = requests.get(
            f"http://api.gios.gov.pl/pjp-api/rest/station/sensors/{stationid}"
        )
        sensors = json.loads(sensors.content)
        get_sensors(sensors)


main()
