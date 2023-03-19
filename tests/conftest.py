
import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session", autouse=True)
def url():
    browser.config.timeout = 3.0
    browser.config.base_url = "https://google.com"

    yield

    browser.quit()


@pytest.fixture(scope="function")
def browser_size_s():
    browser.config.window_width = 1280
    browser.config.window_height = 800


@pytest.fixture(scope="function")
def browser_size_m():
    browser.config.window_width = 1440
    browser.config.window_height = 900
