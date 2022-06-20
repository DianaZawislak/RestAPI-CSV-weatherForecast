"""Task 4"""
import pytest


@pytest.mark.parametrize("city, city_confirmation", [
    ("Jakarta", "Jakarta"),
    ("London", "London"),
])
def test_task4(load_env, city, city_confirmation):
    # pylint: disable=unused-argument, unused-import, duplicate-code, comparison-with-itself, singleton-comparison
    """See task 4 in the readme"""
    assert True
