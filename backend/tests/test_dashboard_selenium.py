import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.contrib.auth.models import User

from . import DRIVER_PATH


class TestAdminPage(StaticLiveServerTestCase):
    def setUp(self) -> None:
        try:
            os.mkdir(f"{DRIVER_PATH}/tests/temp")
        except FileExistsError:
            pass

        path = f"{DRIVER_PATH}/tests/temp"
        options = Options()
        options.headless = True

        self.driver = webdriver.Chrome(
            ChromeDriverManager(path=path).install(), options=options
        )

    def tearDown(self) -> None:
        self.driver.close()

    def test_create_new_user(self):
        admin = User.objects.create_superuser('dev', 'dev@dev.id', 'dev')
        self.client.login(username=admin.username, password=admin.password)
        # cookie = self.client.cookies['sessionid']
        self.driver.get(self.live_server_url + '/admin/')  # selenium will set cookie domain based on current page domain
        # self.driver.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.driver.refresh() # need to update page for logged in user
        self.driver.get(self.live_server_url + '/admin/')

    def test_adminpage(self):
        url: str = self.live_server_url + reverse("admin:login")
        self.driver.get(url)
        source = self.driver.page_source
        
        username = self.driver.find_element(By.NAME, 'username')
        passwd = self.driver.find_element(By.NAME, 'password')
        submit = self.driver.find_element(By.XPATH, '//input[@value="Log in"]')

        # bypass login
        username.send_keys("dev")
        passwd.send_keys("dev")
        submit.send_keys(Keys.ENTER)
        
        soup = BeautifulSoup(source, 'html.parser')
        title = soup.find("title").text.strip()
        assert title == "Log in | Django site admin"
        