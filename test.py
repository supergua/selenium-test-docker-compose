from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

driver = webdriver.Remote(command_executor='http://6.100.3.226:4444/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)

url = 'http://www.kjb2c.com'

driver.get(url)
print(driver.title)
driver.get_screenshot_as_file('homepage.jpg')
time.sleep(2)
driver.quit()
