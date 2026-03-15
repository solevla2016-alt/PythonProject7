from abc import ABC, abstractmethod
from typing import List

from src.models.aeroplane import Aeroplane


class BaseStorage(ABC):

    @abstractmethod
    def add_aeroplane(self, aeroplane: Aeroplane) -> None:
        pass

    @abstractmethod
    def get_aeroplanes(self) -> List[Aeroplane]:
        pass

    @abstractmethod
    def delete_aeroplane(self, aeroplane: Aeroplane) -> None:
        pass
