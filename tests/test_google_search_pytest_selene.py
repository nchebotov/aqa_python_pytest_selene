
from selene import be, have
from selene.support.shared import browser


def test_my_github_s(url, browser_size_s):
    browser.open("/ncr")
    browser.element('[name="q"]').should(be.blank).type('pytest').press_enter()
    browser.element('[id="search"]').should(have.text('helps you write better programs — pytest documentation'))


def test_my_github_m(url, browser_size_m):
    browser.open("/ncr")
    browser.element('[name="q"]').should(be.blank).type('pytest').press_enter()
    browser.element('[id="search"]').should(have.text('helps you write better programs — pytest documentation'))