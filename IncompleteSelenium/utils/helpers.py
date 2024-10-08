import pytest

@pytest.fixture(scope="function")
def get_driver(request):
    from utils.browser_setup import get_browser
    browser = request.config.getoption("--browser")
    driver = get_browser(browser)
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
