# Python selenium testing

Practicing with Selenium testing in python.

* Create a virtualenv (in this case using windows and powershell)
```bash
python -m venv pytesting
pytesting\Scripts\Activate.ps1
```
* install selenium:  
`pip install selenium`

* install and configure selenium drivers for chrome and firefox ( or for your preferred browser). Download the drivers and add the PATH in your environment.

* start to play with selenium :wink:


Example:

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")

elem = driver.find_element(By.NAME,"q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(8)

driver.close()
```

