import requests

from .base_api import BaseAPI


class AeroplanesAPI(BaseAPI):

    __NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
    __OPENSKY_URL = "https://opensky-network.org/api/states/all"

    def _connect(self, url: str):
        response = requests.get(url)

        if response.status_code != 200:
            raise ConnectionError("Ошибка подключения к API")

        return response

    def get_country_bbox(self, country: str):

        params = {"q": country, "format": "json"}

        headers = {"User-Agent": "aeroplanes_project"}

        response = requests.get(self.__NOMINATIM_URL, params=params, headers=headers)

        data = response.json()

        if not data:
            raise ValueError("Страна не найдена")

        bbox = data[0]["boundingbox"]

        south = float(bbox[0])
        north = float(bbox[1])
        west = float(bbox[2])
        east = float(bbox[3])

        return south, north, west, east

    def get_aeroplanes(self, country: str) -> list:
        """Получение самолетов в воздушном пространстве страны."""

        south, north, west, east = self.get_country_bbox(country)

        url = (
            f"https://opensky-network.org/api/states/all?"
            f"lamin={south}&lomin={west}&lamax={north}&lomax={east}"
        )

        response = requests.get(url)

        if response.status_code != 200:
            return []

        data = response.json()

        states = data.get("states")

        if not states:
            return []

        # фильтруем пустые записи
        planes = [s for s in states if s[1]]

        return planes[:100]
