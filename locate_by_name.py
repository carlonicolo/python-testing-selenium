from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# this import is used to find element by name, xpath, id, ecc...
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:\\Users\\carlo\\git\\LinkedIN\\python-automating-testing\\page_test.html")
username = driver.find_element(By.NAME, "username")
print("My input element is: ")
print(username)
driver.close()