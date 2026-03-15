from typing import List, Tuple

import requests

from src.api.base_api import BaseAPI


class AeroplanesAPI(BaseAPI):

    __NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
    __OPENSKY_URL = "https://opensky-network.org/api/states/all"

    def _connect(self, url: str) -> requests.Response:
        response = requests.get(url)

        if response.status_code != 200:
            raise ConnectionError("Ошибка подключения к API")

        return response

    def get_country_bbox(self, country: str) -> Tuple[float, float, float, float]:

        params = {"q": country, "format": "json"}
        headers = {"User-Agent": "aeroplanes_project"}

        response = requests.get(self.__NOMINATIM_URL, params=params, headers=headers)

        data: list = response.json()

        if not data:
            raise ValueError("Страна не найдена")

        bbox = data[0]["boundingbox"]

        south: float = float(bbox[0])
        north: float = float(bbox[1])
        west: float = float(bbox[2])
        east: float = float(bbox[3])

        return south, north, west, east

    def get_aeroplanes(self, country: str) -> List[list]:
        """Получение самолетов в воздушном пространстве страны."""

        south, north, west, east = self.get_country_bbox(country)

        params = {
            "lamin": south,
            "lomin": west,
            "lamax": north,
            "lomax": east,
        }

        response = requests.get(self.__OPENSKY_URL, params=params)

        if response.status_code != 200:
            return []

        data: dict = response.json()

        states: List[list] | None = data.get("states")

        if not states:
            return []

        planes: List[list] = []

        for s in states:
            try:
                if s[1]:
                    planes.append(s)
            except IndexError:
                raise ValueError("Некорректные данные API")

        return planes[:100]
