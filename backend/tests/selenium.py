import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# chrome fixture
@pytest.fixture(scope="module")
def chrome_browser_instance():
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
    yield driver
    driver.close()
    

