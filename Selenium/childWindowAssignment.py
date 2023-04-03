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
driver = webdriver.Chrome(service=service_obj, chrome_options=a)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
window2 = driver.window_handles
driver.switch_to.window(window2[1])
email = driver.find_element(By.XPATH, "//a[text()='mentor@rahulshettyacademy.com']").text
driver.switch_to.window(window2[0])
driver.find_element(By.XPATH, "//input[@name='username']").send_keys(email)
driver.find_element(By.NAME, "password").send_keys("Assignment")
driver.find_element(By.NAME, "signin").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert")))
print(driver.find_element(By.CSS_SELECTOR, ".alert").text)