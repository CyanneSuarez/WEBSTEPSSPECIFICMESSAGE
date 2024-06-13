# features/steps/web_steps.py

from behave import then
from selenium import webdriver

# Initialize the WebDriver
driver = webdriver.Chrome()

@then('I should see the message "{message}"')
def step_impl(context, message):
    assert message in driver.page_source, f"Expected message '{message}' not found in page source"
