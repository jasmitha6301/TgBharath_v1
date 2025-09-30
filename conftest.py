import time
from playwright.sync_api import sync_playwright, Page
import configparser
import pytest
import os

# Pytest hook to capture screenshot on test failure
import pytest
import os

import yaml

from pages.home_page import HomePage

import pytest
import os



@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
       with open("config/config.yaml") as f:
        config=yaml.safe_load(f)
       browser_name = config.get("browser", "chromium")
       browser = getattr(p, browser_name).launch()
       time.sleep(10)
       yield browser
       browser.close()

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def assert_text_present():
    def _assert_text_present(page, text, timeout=5000):
        locator = page.locator(f"text={text}")
        try:       
            locator.wait_for(state="visible",timeout=timeout)
            assert locator.is_visible(), f"Text '{text}' not found on the page"
        except Exception as e:
            screenshots_dir = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshots_dir, f"assert_fail_{text.replace(' ', '_')}.png")
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path} due to assertion failure")
            raise
    return _assert_text_present

@pytest.fixture
def login_as():
    def _login_as(page, login_page, userName, password, base_url):
        login_page.login(userName, password, base_url)
    return _login_as

       

      
  
@pytest.fixture(scope="function")         
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    with open("config/config.yaml") as f:
        config=yaml.safe_load(f)
    base_url = config.get("baseUrl", "https://tgbharath.com/admin-login")
    page.goto(base_url)
    time.sleep(10)
    yield page
    page.close()
    
     
@pytest.fixture(scope="session")
def config():
   with open("config/config.yaml") as f:
      return yaml.safe_load(f)
   

