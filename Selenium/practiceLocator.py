from cgitb import text
from operator import contains

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

a=Options()
a.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\Priya Khiwal\Chrome Webdriver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, chrome_options=a)

driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.find_element(By.XPATH,"//span[text()= 'Account & Lists']").click()

# //span[contains(text(),'Account & Lists')]
# //span[text()= "Account & Lists"]

driver.find_element(By.NAME,'email').send_keys("nitish.kataria1993@gmail.com")
driver.find_element(By.ID,'continue').click()
driver.find_element(By.ID,'ap_password').send_keys('NIKU1993')
driver.find_element(By.ID,'signInSubmit').click()
# driver.close()
