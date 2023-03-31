import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

a=Options()
a.add_experimental_option("detach",True)

service_obj = Service(r"C:\Users\Priya Khiwal\Chrome Webdriver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, chrome_options = a)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break
# driver.find_element(By.XPATH,"//a[text()='India']").click()

output = driver.find_element(By.ID,"autosuggest").get_attribute("value")

print (output)

assert output == "India"