from selenium import webdriver

def get_browser(browser_name):
    if browser_name.lower() == "chrome":
        return webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        return webdriver.Firefox()
    else:
        raise ValueError(f"Browser {browser_name} is not supported.")
