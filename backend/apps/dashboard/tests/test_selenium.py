import time
from bs4 import BeautifulSoup
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_create_superuser(create_admin_user):
    assert create_admin_user.is_superuser is True
    assert create_admin_user.is_staff is True
    assert create_admin_user.is_active is True
    assert create_admin_user.email == "dev@dev.id"
    assert create_admin_user.username == "dev"


@pytest.mark.selenium
def test_dashboard_admin_login(
    live_server, chrome_browser_instance, db_fixture_setup
):

    browser = chrome_browser_instance

    browser.get(("%s%s" % (live_server.url, "/admin/login/")))

    user_name = browser.find_element(By.NAME, "username")
    user_password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input')

    user_name.send_keys("dev")
    user_password.send_keys("dev")
    submit.send_keys(Keys.RETURN)

    # parse the page title
    soup = BeautifulSoup(browser.page_source, "html.parser")
    site_title = soup.find("div", attrs={'id': "content"}).find("h1").text

    assert "Site administration" == site_title