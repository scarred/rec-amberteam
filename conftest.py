import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from utils.config_reader import ConfigReader

@pytest.fixture(scope="session")
def driver():
    config_reader = ConfigReader()
    browser = config_reader.get_browser()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.use_chromium = True
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Invalid browser specified in config.ini: {browser}")

    yield driver

    driver.quit()