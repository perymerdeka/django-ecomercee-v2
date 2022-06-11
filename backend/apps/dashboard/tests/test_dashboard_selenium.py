import pytest

@pytest.mark.fixtures
def test_adminpage(live_server, chrome_browser_instance):
    driver = chrome_browser_instance
    url: str = f"{live_server.url}/admin/login"
    driver.get(url)
