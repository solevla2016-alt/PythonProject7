from src.storage.json_saver import JSONSaver
from src.models.aeroplane import Aeroplane


def test_add_aeroplane(tmp_path):

    file = tmp_path / "planes.json"

    saver = JSONSaver(file)

    plane = Aeroplane("A1", "USA", 200, 10000)

    saver.add_aeroplane(plane)

    data = saver.get_aeroplanes()

    assert len(data) == 1
    assert data[0].callsign == "A1"


def test_no_duplicates(tmp_path):

    file = tmp_path / "planes.json"

    saver = JSONSaver(file)

    plane = Aeroplane("A1", "USA", 200, 10000)

    saver.add_aeroplane(plane)
    saver.add_aeroplane(plane)

    data = saver.get_aeroplanes()

    assert len(data) == 1


def test_delete_plane(tmp_path):

    file = tmp_path / "planes.json"

    saver = JSONSaver(file)

    plane = Aeroplane("A1", "USA", 200, 10000)

    saver.add_aeroplane(plane)

    saver.delete_aeroplane(plane)

    data = saver.get_aeroplanes()

    assert data == []