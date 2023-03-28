from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

a = Options()
a.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\Priya Khiwal\Chrome Webdriver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, chrome_options=a)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1235689")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.NAME,"name").send_keys("NIK")
driver.find_element(By.ID,"exampleFormControlSelect1").click()
driver.find_element(By.ID,"inlineRadio2").click()
driver.find_element(By.NAME,"bday").send_keys("26-08-1993")
driver.find_element(By.CLASS_NAME,"btn.btn-success").click()