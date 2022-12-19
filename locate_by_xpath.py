from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# this import is used to find element by name, xpath, id, ecc...
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:\\Users\\carlo\\git\\LinkedIN\\python-automating-testing\\page_test.html")
login_form_absolute = driver.find_element(By.XPATH, "/html/body/form[1]")
login_form_relative = driver.find_element(By.XPATH, "//form[1]")
login_form_id = driver.find_element(By.XPATH, "//form[@id='loginForm']")
print("My login form is: ")
print(login_form_absolute)
print(login_form_relative)
print(login_form_id)
driver.close()