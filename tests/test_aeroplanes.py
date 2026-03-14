import pytest
from src.models.aeroplane import Aeroplane


def test_create_aeroplane():
    plane = Aeroplane("A1", "USA", 250, 10000)

    assert plane.callsign == "A1"
    assert plane.country == "USA"
    assert plane.velocity == 250
    assert plane.altitude == 10000


def test_validation_none_values():
    plane = Aeroplane(None, None, None, None)

    assert plane.callsign == "Unknown"
    assert plane.country == "Unknown"
    assert plane.velocity == 0
    assert plane.altitude == 0


def test_compare_altitude():
    p1 = Aeroplane("A1", "USA", 200, 10000)
    p2 = Aeroplane("A2", "USA", 200, 20000)

    assert p2 > p1
    assert p1 < p2


def test_cast_to_object_list():
    data = [
        ["id", "CALL1", "USA", None, None, None, None, None, None, 250, None, None, None, 10000],
        ["id", "CALL2", "Germany", None, None, None, None, None, None, 300, None, None, None, 12000],
    ]

    planes = Aeroplane.cast_to_object_list(data)

    assert len(planes) == 2
    assert isinstance(planes[0], Aeroplane)