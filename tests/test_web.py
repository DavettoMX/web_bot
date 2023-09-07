# Import dependencies
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

# Enter the URL
url = "https://www.mozilla.org"  # Mozilla webpage
title = "Internet for people"

@pytest.fixture
def webFix():
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        element = wait(driver, 10).until(EC.title_contains(title))  # Wait 10 secs for an element to load
    except Exception as e:
        print(e)
    yield driver

    driver.quit()


def test_account_form(webFix):
    webFix.find_element_by_link_text("Get a Firefox Account").click()

    try:
        element = wait(webFix, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'email tooltip-below'))
        )

    except Exception as e:
        print(e)

    text_input = webFix.find_element_by_tag_name('input')
    text_input.send_keys('selenium@fakemail.com')
    webFix.find_elements_by_id('submit-btn').click()
    prefill_email = 'none'
    
    try:
        prefill_email = wait(webFix, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'prefill_email'))
        )
    except Exception as e:
        print(e)

    assert 'selenium@fakemail.com' in prefill_email.text