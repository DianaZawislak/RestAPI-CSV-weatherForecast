 """Task 3"""
import pytest

import app


@pytest.mark.parametrize("city, city_confirmation", [
    ("London", "London"),
    ("Jakarta", "Jakarta"),
])
def test_task3(load_env, city, city_confirmation):
    # pylint: disable=unused-argument, unused-import, duplicate-code, comparison-with-itself, singleton-comparison
    """Tests that the weather api gets a valid response for the city you are requesting"""
    assert app.get_city_forecast_response(city) == city_confirmation
