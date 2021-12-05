from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get('http://www/.amazon.com')

driver.find_element(CSS_SELECTOR, "a-icon a-icon-logo")
driver.find_element(CSS_SELECTOR, "ap_register_form")
driver.find_element(CSS_SELECTOR, "ap_customer_name")
driver.find_element(CSS_SELECTOR, "email")
driver.find_element(CSS_SELECTOR, "ap_email")
driver.find_element(CSS_SELECTOR, "password")
driver.find_element(CSS_SELECTOR, "ap_password_check")
driver.find_element(CSS_SELECTOR, "auth-continue-announce")
driver.find_element(CSS_SELECTOR, "ap_register_notification_Conditions of Use")
driver.find_element(CSS_SELECTOR, "ap_register_notification_privacy_notice")
driver.find_element(CSS_SELECTOR, "ap_register_form")





Amazon cancel order

Given user is on Amazon.com page
When user clicks on search button
And search for cancel order
Then verifies order is cancelled

from selenium import webdriver
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(contex):
    contex.driver.get('https://www.amazon.com/')


@when('click on cart button')
def click_cart button(contex):
    contex.driver.find_element(By.ID, 'nav-cart-icon nav-sprite').send_keys


then('Verify cart is empty')
def click_cart_icon(contex):
    contex.driver.find_element (By.ID, 'div.a-row.sc-your-amazon-cart-is-empty').click









