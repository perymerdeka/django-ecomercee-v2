import pytest

@pytest.mark.selenium
def test_adminpage(live_server, chrome_browser_instance):
    driver = chrome_browser_instance
    url: str = f"{live_server.url}/admin/login"
    driver.get(url)
    source = driver.page_source
    title = source.title
    assert title == "test"


def test_login_admin():
    pass