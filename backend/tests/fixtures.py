import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from . import DRIVER_PATH

# chrome fixture
@pytest.fixture(scope="module")
def chrome_browser_instance():
    """
    provide a selenium webdriver
    """
    try:
        os.mkdir(f"{DRIVER_PATH}/temp")
    except FileExistsError:
        pass
    
    driver_path = f"{DRIVER_PATH}/temp"
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(executable_path=ChromeDriverManager(path=driver_path).install(),chrome_options=options)
    yield driver
    driver.close()
    

