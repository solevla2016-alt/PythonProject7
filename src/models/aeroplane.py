class Aeroplane:
    """Класс самолета."""

    __slots__ = ("callsign", "country", "velocity", "altitude")

    def __init__(self, callsign: str, country: str, velocity: float, altitude: float):

        self.callsign = self.__validate_str(callsign)
        self.country = self.__validate_str(country)
        self.velocity = self.__validate_number(velocity)
        self.altitude = self.__validate_number(altitude)

    def __validate_str(self, value: str) -> str:

        if not value:
            return "Unknown"

        return value.strip()

    def __validate_number(self, value: float) -> float:

        if value is None:
            return 0

        return float(value)

    def __lt__(self, other):
        return self.altitude < other.altitude

    def __gt__(self, other):
        return self.altitude > other.altitude

    def __repr__(self):

        return f"{self.callsign} | {self.country} | {self.velocity} km/h | {self.altitude} m"

    @staticmethod
    def cast_to_object_list(data):
        """Преобразует данные API в список объектов Aeroplane."""

        planes = []

        for p in data:
            plane = Aeroplane(
                p[1] or "Unknown", p[2] or "Unknown", p[9] or 0, p[13] or 0
            )
            planes.append(plane)

        return planes
