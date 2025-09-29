import time
from playwright.sync_api import sync_playwright, Page
import configparser
import pytest
import yaml

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
       with open("config/config.yaml") as f:
        config=yaml.safe_load(f)
       browser_name = config.get("browser", "chromium")
       browser = getattr(p, browser_name).launch(headless=False)
       time.sleep(10)
       yield browser
       browser.close()

@pytest.fixture
def home_page(page):
    return HomePage(page)


       

      
  
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