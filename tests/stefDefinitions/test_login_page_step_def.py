from pytest_bdd import when, then, given, scenarios, parsers
from pages import login_page
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
    login_page.in_login(userName, password, base_url)

@then("I login to home page")
def login_action(page):
    login_page_instance = LoginPage(page)
    login_page_instance.login()

@pytest.fixture
def home_page(page):
    return HomePage(page)

@then(parsers.parse("I am in ${web_page} page with content ${content}"))
def page_validation(page,assert_text_present,content):
     for s in content.split(","):
        assert_text_present(page,s)

