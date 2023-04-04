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
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//a[text()='Shop']").click()

#  //a[contains(@href, 'Shop')]
#  a[href*='Shop']

phones = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for phone in phones:
    phoneName = phone.find_element(By.XPATH, "div/h4/a").text
    if phoneName == "Blackberry":
        phone.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CSS_SELECTOR, "div.checkbox").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
successText = driver.find_element(By.CSS_SELECTOR, "div.alert").text
assert "Success! Thank you!" in successText