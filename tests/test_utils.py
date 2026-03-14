from src.models.aeroplane import Aeroplane
from src.utils.helpers import (
    filter_aeroplanes,
    get_top_aeroplanes,
)


def test_filter_planes():

    planes = [
        Aeroplane("A1", "USA", 200, 10000),
        Aeroplane("A2", "Germany", 200, 15000),
    ]

    result = filter_aeroplanes(planes, ["USA"])

    assert len(result) == 1
    assert result[0].country == "USA"


def test_get_top_planes():

    planes = [
        Aeroplane("A1", "USA", 200, 10000),
        Aeroplane("A2", "USA", 200, 20000),
        Aeroplane("A3", "USA", 200, 15000),
    ]

    top = get_top_aeroplanes(planes, 2)

    assert len(top) == 2
    assert top[0].altitude == 20000