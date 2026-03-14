def filter_aeroplanes(aeroplanes, countries):
    """Фильтр самолетов по стране регистрации."""

    if not countries:
        return aeroplanes

    filtered = []

    for plane in aeroplanes:
        if plane.country in countries:
            filtered.append(plane)

    return filtered


def get_top_aeroplanes(aeroplanes, n):

    sorted_planes = sorted(aeroplanes, reverse=True)

    return sorted_planes[:n]


def print_aeroplanes(aeroplanes):
    for plane in aeroplanes:
        print(
            f"Позывной: {plane.callsign} | "
            f"Страна: {plane.country} | "
            f"Скорость: {plane.velocity} | "
            f"Высота: {plane.altitude}"
        )
