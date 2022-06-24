"""Task 4"""
import pytest
import app


@pytest.mark.parametrize("city, city_confirmation", [
    ("Jakarta", "Jakarta"),
    ("London", "London"),
])
def test_task4(load_env, city, city_confirmation):
    """Test if current condition was returned"""
    # pylint: disable=unused-argument, unused-import, duplicate-code, comparison-with-itself, singleton-comparison
    forecast_current_condition = app.get_city_current_condition(city)
    assert isinstance(forecast_current_condition, str)
