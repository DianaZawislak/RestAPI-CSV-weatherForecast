"""Task 5"""
import pytest

import app


@pytest.mark.parametrize("city, lat, lng", [
    ("Tokyo", 35.6839, 139.7744),
    ("Warsaw",  52.2300, 21.0111),
])
def test_task5(load_env, city, lng, lat):
    """See task 5 in the readme"""
    # pylint: disable=unused-argument, unused-import, duplicate-code, comparison-with-itself, singleton-comparison
    lng_lat = app.get_city_lng_lat(city)
    assert lng_lat[0] == lng
    assert lng_lat[1] == lat
