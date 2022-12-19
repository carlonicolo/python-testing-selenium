from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("file:///C:\\Users\\carlo\\git\\LinkedIN\\python-automating-testing\\page_test.html")
login_form = driver.find_element("id","loginForm")
print("My login form element is: ")
print(login_form)
driver.close()