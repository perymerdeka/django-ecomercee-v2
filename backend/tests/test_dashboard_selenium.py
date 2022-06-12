import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from django.test import TestCase
from django.urls import reverse

from . import DRIVER_PATH


class TestAdminPage(TestCase):
    def setUp(self) -> None:
        try:
            os.mkdir(f"{DRIVER_PATH}/temp")
        except FileExistsError:
            pass

        path = f"{DRIVER_PATH}/temp"
        options = Options()
        options.headless = False

        self.driver = webdriver.Chrome(
            ChromeDriverManager(path=path).install(), chrome_options=options
        )
        yield self.driver
        return super().setUp()

    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()
    
    def test_adminpage(self):
        url: str = "admin/login"
        self.driver.get(url)
        source = self.driver.page_source
        assert source == "test"