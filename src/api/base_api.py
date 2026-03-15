from abc import ABC, abstractmethod

import requests


class BaseAPI(ABC):
    """Абстрактный класс для работы с API."""

    @abstractmethod
    def _connect(self, url: str) -> requests.Response:
        """Подключение к API."""
        pass

    @abstractmethod
    def get_aeroplanes(self, country: str) -> list:
        """Получение самолетов."""
        pass
