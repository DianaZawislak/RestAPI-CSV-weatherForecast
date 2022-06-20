"""Task 2"""
import pytest

import app


@pytest.mark.parametrize("city, population", [
    ("Tokyo", 39105000),
    ("Jakarta", 35362000),
])
def test_task2(city, population):
    # pylint: disable=unused-argument, unused-import, duplicate-code, comparison-with-itself, singleton-comparison
    """Tests that the get city population function gets the population of the city inputted """
    assert app.get_city_population(city) == int(population)
