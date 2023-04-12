import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

a = Options()
a.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\Priya Khiwal\Chrome Webdriver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj, chrome_options=a)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(5)
driver.switch_to.frame("courses-iframe")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='JOIN NOW']")))

driver.find_element(By.XPATH, "//a[text()='JOIN NOW']").click()