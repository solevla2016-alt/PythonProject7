def filter_aeroplanes(aeroplanes, countries):
    return [a for a in aeroplanes if a.country in countries]


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
