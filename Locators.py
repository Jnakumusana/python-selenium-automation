from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://www/.amazon.com')

driver.find_element(By.XPATH, "//*@id="nav-linl-flyout-ya-signin")a/span[2]')
driver.find_element(By.XPATH, "//*@id="ap_email"]')

driver.find_element(By.XPATH, "//*[@id="continue"])
driver.find_element(By.XPATH, "//*@id="ap_password"]')
driver.find_element(By.XPATH, "//*@id="_signInSubmit"]')
driver.find_element(By.XPATH, "//*[@id="auth-fpp-link-bottom"]
driver.find_element(By.XPATH, "//*[@id="legalTextRow"]/a[2]

driver.find_element(By.XPATH, "// *[@id="authportal-main-section"]
driver.find_element(By.XPATH, "//*[@id="createAccountSubmit"]



driver.get('https://www.amazon.com/gp/help/customer/display.html ')
search = driver.find_element(By_ID, 'helpsearch')
search.send_keys('cancel_order', keys.ENTER)
assert "No results found." not in driver.page_source
driver.close()




