# C:\Users\Priya Khiwal\Firefox (gecko) Webdriver\geckodriver-v0.32.2-win-aarch64.zip

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.chrome.options import Options

# a = Options()
# a.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\Priya Khiwal\Firefox (gecko) Webdriver\geckodriver-v0.32.2-win-aarch64.zip")
driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/consulting")
driver.back()
driver.forward()
driver.close()