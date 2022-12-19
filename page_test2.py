from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()
driver.get("file:///C:\\Users\\carlo\\git\\LinkedIN\\python-automating-testing\\page_test2.html")

select = Select(driver.find_element(By.NAME, "numReturnSelect"))
select.select_by_index(4)
time.sleep(2)

select.select_by_visible_text("200")
time.sleep(2)

select.select_by_value("250")
time.sleep(2)

options = select.options
print(options)

submit_button = driver.find_element(By.NAME, "continue")
submit_button.submit()
time.sleep(2)

driver.close()