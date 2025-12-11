import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup():
    """
    Setup: Initialize Chrome WebDriver using webdriver-manager.
    Teardown: Quit browser after test completes.
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_homepage_loads(setup):
    """
    Test: Verify homepage loads.
    Expected: Page title contains 'Dave' or 'DaveAI'.
    """
    setup.get("https://www.iamdave.ai")
    assert "Dave" in setup.title or "DaveAI" in setup.title


def test_logo_displayed(setup):
    """
    Test: Verify that the website logo/image is visible.
    Purpose: Ensures that UI elements load correctly.
    """
    setup.get("https://www.iamdave.ai")
    time.sleep(2)
    logo = setup.find_element(By.TAG_NAME, "img")
    assert logo.is_displayed()


def test_navigation(setup):
    """
    Test: Verify navigation works.
    Action: Click first link on page.
    Expected: URL should change from the homepage.
    """
    setup.get("https://www.iamdave.ai")
    time.sleep(2)
    links = setup.find_elements(By.TAG_NAME, "a")
    assert len(links) > 0  # Ensure at least one link exists
    links[0].click()
    time.sleep(2)
    assert setup.current_url != "https://www.iamdave.ai"


def test_input_field(setup):
    """
    Test: Check presence of input fields on homepage.
    Purpose: Ensures page supports user interaction.
    """
    setup.get("https://www.iamdave.ai")
    time.sleep(2)
    inputs = setup.find_elements(By.TAG_NAME, "input")
    assert len(inputs) > 0
