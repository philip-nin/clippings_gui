import pytest
import os

@pytest.fixture(scope="function", autouse=True)
def driver_unittest(request, driver):
    request.cls.driver = driver


@pytest.fixture(autouse=True)
def selenium(selenium):
    try:
        selenium.set_window_size(1920, 1080)
    except:
        selenium.maximize_window()
    return selenium


def pytest_logger_stdoutloggers(item):
    return ['verbose']
