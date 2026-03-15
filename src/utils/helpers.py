from typing import List

from src.models.aeroplane import Aeroplane


def filter_aeroplanes(aeroplanes: List[Aeroplane], countries: List[str]) -> List[Aeroplane]:
    """Фильтрация самолетов по стране регистрации."""
    if not countries:
        return aeroplanes

    return [plane for plane in aeroplanes if plane.country in countries]


def get_top_aeroplanes(aeroplanes: List[Aeroplane], top_n: int) -> List[Aeroplane]:
    """Получение топ N самолетов по высоте."""
    sorted_planes = sorted(aeroplanes, key=lambda x: x.altitude, reverse=True)
    return sorted_planes[:top_n]


def print_aeroplanes(aeroplanes: List[Aeroplane]) -> None:
    """Вывод самолетов в консоль."""
    for plane in aeroplanes:
        print(
            f"Позывной: {plane.callsign} | "
            f"Страна: {plane.country} | "
            f"Скорость: {plane.velocity} | "
            f"Высота: {plane.altitude}"
        )
