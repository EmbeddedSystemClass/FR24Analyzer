from .helper import helper
from .store import store
import requests
import time
import json
from datetime import datetime


class FR24Analyzer(object):

    def __init__(self, configFile="config.yaml", logFile="log", logging=True):
        self._hlp = helper.Helper()
        self.configFile = configFile
        self.logging = logging

        if self.logging == True:  # Ugly but fast solution for #7 Make logging optional Issue
            #Set the log file and add titles to logfile
            self.logFile = logFile
            self._hlp.addTitleToLogFile(self.logFile)

        configParameters = self._hlp.readFromConfigFile(self.configFile)
        self.bounds = configParameters["bounds"]
        self.airportName = configParameters["airportName"]
        self.airportLat = configParameters["airportLat"]
        self.airportLon = configParameters["airportLon"]
        self.redis_ip = configParameters["redis_ip"]
        self.redis_port = configParameters["redis_port"]
        self.postgres_ip = configParameters["postgres_ip"]
        self.postgres_port = configParameters["postgres_port"]
        self._url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?"
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

    def __del__(self):
        del self._hlp

    def _readKeysFromJSONObject(self, jsonObject):
        flightData = dict()
        storeInstance = store.store(self.redis_ip, self.redis_port,
                                    self.postgres_ip, self.postgres_port)
        airportCoordinates = [self.airportLat, self.airportLon]
        if self.logging == True:
            f = open(self.logFile, 'a+')
        for key in jsonObject:
                if key not in ["version", "full_count", "stats"]:
                    value = jsonObject[key]
                    lat = value[1]
                    lon = value[2]
                    hdg = value[3]
                    alt = value[4]
                    spd = value[5]
                    flight = value[0]
                    _now = datetime.now()
                    _time = time.mktime(_now.timetuple())
                    distanceToAirport = str(self._hlp.calcDistanceFromAirport(
                        value[1], value[2], airportCoordinates[0], airportCoordinates[1]))
                    if self.logging == True:
                        f.write(str(flight) + "," + str(lat) + "," + str(lon) + "," + str(hdg) +
                                "," + str(alt) + "," + str(spd) + "," + str(_time) + "," + str(distanceToAirport) + "\n")

                    # Write to REDIS
                    flightData['lat'] = lat
                    flightData['lon'] = lon
                    flightData['hdg'] = hdg
                    flightData['alt'] = alt
                    flightData['spd'] = spd
                    flightData['distance'] = distanceToAirport
                    flightData['time'] = _time

                    #TODO: Add check to here if the same flight is exist on the REDIS
                    # do not add and check if the al value 0 than add it with an extension
                    storeInstance.writeToRedis(flight, flightData)
        if self.logging == True:
            f.close()

    def getLandingTimeToAirport(self):
        payload = {"bounds": str(self.bounds),
                       "faa": 1,
                       "satellite": 1,
                       "mlat": 1,
                       "flarm": 1,
                       "adsb": 1,
                       "gnd": 1,
                       "air": 1,
                       "vehicles": 1,
                       "estimated": 1,
                       "maxage": 14400,
                       "gliders": 1,
                       "stats": 1,
                       "to": str(self.airportName)}
        response = requests.get(
        self._url, headers=self._headers, params=payload)
        responseJSON = response.json()
        self._readKeysFromJSONObject(responseJSON)
