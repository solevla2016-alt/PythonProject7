import json
from pathlib import Path

from .base_storage import BaseStorage


class JSONSaver(BaseStorage):

    def __init__(self, filename="data/aeroplanes.json"):

        self.__filename = Path(filename)

        if not self.__filename.exists():
            self.__filename.write_text("[]")

    def add_aeroplane(self, aeroplane):

        try:
            data = json.loads(self.__filename.read_text())
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        plane_dict = {
            "callsign": aeroplane.callsign,
            "country": aeroplane.country,
            "velocity": aeroplane.velocity,
            "altitude": aeroplane.altitude,
        }

        if plane_dict not in data:
            data.append(plane_dict)

        self.__filename.write_text(json.dumps(data, indent=4))

    def get_aeroplanes(self):

        return json.loads(self.__filename.read_text())

    def delete_aeroplane(self, aeroplane):

        data = json.loads(self.__filename.read_text())

        data = [p for p in data if p["callsign"] != aeroplane.callsign]

        self.__filename.write_text(json.dumps(data, indent=4))
