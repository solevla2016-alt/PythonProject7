from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """Абстрактный класс для работы с API."""

    @abstractmethod
    def _connect(self, url: str):
        """Подключение к API."""
        pass

    @abstractmethod
    def get_aeroplanes(self, country: str):
        """Получение самолетов."""
        pass
