
import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def url():
    return "https://google.com"


@pytest.fixture(scope="function")
def browser_size_s():
    browser.config.window_width = 1280
    browser.config.window_height = 800


@pytest.fixture(scope="function")
def browser_size_m():
    browser.config.window_width = 1440
    browser.config.window_height = 900
