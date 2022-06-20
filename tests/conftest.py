"""This is for test helper fixtures and configuration as needed"""
import time

import pytest
from dotenv import load_dotenv

import app


@pytest.fixture
def run_program():
    """This runs the program for the test"""
    app.main()


@pytest.fixture
def setup_logs():
    """This runs the program for the test"""
    app.setup_logs()


@pytest.fixture
def load_env():
    """This Loads the .env file you need this to use the API key in requests"""
    load_dotenv()


@pytest.fixture
def sleep():
    """This Loads the .env file you need this to use the API key in requests"""
    time.sleep(1)
