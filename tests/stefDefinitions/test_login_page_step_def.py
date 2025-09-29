from pytest_bdd import when, then, given, scenarios, parsers
from pages.login_page import LoginPage
from pages.home_page import HomePage
import pytest

scenarios("../features")

@when(parsers.parse("I am in login page with ${userRole} with userName ${userName} and password as ${password}"))
def step_enter_credentials(page, config, userRole, userName, password):
    login_page = LoginPage(page)
    if userRole == "AdminUser":
        base_url = config["baseUrlAdmin"]
    elif userRole == "NormalUser":
        base_url = config["baseUrlUser"]
    else:
        base_url = config.get("baseUrl", "https://tgbharath.com/admin-login")
    login_page.login(userName, password, base_url)

@pytest.fixture
def home_page(page):
    return HomePage(page)

@then(parsers.parse("I am in ${web_page} page"))
def page_validation(home_page, web_page):
    if web_page == "home":
        assert "Select Complaint Type"==home_page.get_content_txt()

