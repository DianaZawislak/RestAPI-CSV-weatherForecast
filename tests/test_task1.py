"""Task 1"""
import os
from os.path import exists
import app


def test_task1():
    # pylint: disable=unused-argument, unused-import, duplicate-code, comparison-with-itself, singleton-comparison
    """Checks that the worldcities.csv file is in the right place."""
    assert exists(os.path.join(app.Config.BASE_DIR, "..", "data",
                               "../data/worldcities.csv")), "worldcities.csv not found"
