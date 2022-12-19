from selenium import webdriver

# this import is used to find element by name, xpath, id, ecc...
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
#driver.get("file:///C:\\Users\\carlo\\git\\LinkedIN\\python-automating-testing\\page_test.html")
driver.get("http://selenium.dev")

element_id = driver.find_element(By.ID, "selenium-logo")
print(element_id) 

element_name = driver.find_element(By.NAME, "submit")
print(element_name)

heading_xpath = driver.find_element(By.XPATH, "//section[@class='hero homegape']/h1[1]")
print(heading_xpath)

element_classname = driver.find_element(By.CLASS_NAME, "selenium-backers")
print(element_classname)

driver.close()