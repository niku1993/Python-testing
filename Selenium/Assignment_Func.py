import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
expected_result = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actual_result = []
a=Options()
a.add_experimental_option("detach",True)

service_obj = Service(r"C:\Users\Priya Khiwal\Chrome Webdriver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, chrome_options = a)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, "[class='search-keyword']").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    actual_result.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH,"div/button").click()
# print(actual_result)
assert expected_result == actual_result

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
promo = driver.find_element(By.CLASS_NAME, "promoInfo").text
assert "applied" in promo

#sum validation
prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum=0
for price in prices:
    sum = sum + int(price.text)

print(sum)

totalAmount = float(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == totalAmount

discountedAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert discountedAmount < totalAmount