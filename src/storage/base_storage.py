from abc import ABC, abstractmethod


class BaseStorage(ABC):

    @abstractmethod
    def add_aeroplane(self, aeroplane):
        pass

    @abstractmethod
    def get_aeroplanes(self):
        pass

    @abstractmethod
    def delete_aeroplane(self, aeroplane):
        pass
