from unittest.mock import patch
from src.api.aeroplanes_api import AeroplanesAPI


@patch("requests.get")
def test_get_country_bbox(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {"boundingbox": ["1", "2", "3", "4"]}
    ]

    api = AeroplanesAPI()

    bbox = api.get_country_bbox("Spain")

    assert bbox == (1.0, 2.0, 3.0, 4.0)


@patch("requests.get")
def test_get_aeroplanes(mock_get):

    def side_effect(*args, **kwargs):

        class MockResponse:
            status_code = 200

            def json(self):
                if "search" in args[0]:
                    return [{"boundingbox": ["1", "2", "3", "4"]}]
                return {"states": [["id", "CALL1", "USA", None, None, None, None, None, None, 250, None, None, None, 10000]]}

        return MockResponse()

    mock_get.side_effect = side_effect

    api = AeroplanesAPI()

    planes = api.get_aeroplanes("Spain")

    assert len(planes) == 1