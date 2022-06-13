import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

from . import DRIVER_PATH


class TestAdminPage(StaticLiveServerTestCase):
    def setUp(self) -> None:
        try:
            os.mkdir(f"{DRIVER_PATH}/tests/temp")
        except FileExistsError:
            pass

        path = f"{DRIVER_PATH}/tests/temp"
        options = Options()
        options.headless = False

        self.driver = webdriver.Chrome(
            ChromeDriverManager(path=path).install(), options=options
        )

    def tearDown(self) -> None:
        self.driver.close()
    
    @pytest.mark.fixtures
    def test_adminpage(self):
        url: str = self.live_server_url + reverse("admin:login")
        self.driver.get(url)
        source = self.driver.page_source