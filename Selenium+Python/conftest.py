import pytest
from selenium import webdriver

# Add a command-line option for selecting the browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")

# Create a fixture to initialize the browser based on the command-line option
@pytest.fixture(scope="function")
def get_driver(request):
    browser = request.config.getoption("--browser")
    
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")
    
    driver.maximize_window()
    yield driver
    driver.quit()
