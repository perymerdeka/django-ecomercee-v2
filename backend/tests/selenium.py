import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path


@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    path = Path(__file__).parent.parent

    try:
        os.mkdir(f"{path}/tests/temp")
    except FileExistsError:
        pass

    """
    Provide a selenium webdriver instance
    """
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(
        ChromeDriverManager(path=os.path.join(path, "tests/temp")).install(),
        options=options,
    )
    yield browser
    browser.close()
