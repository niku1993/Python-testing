from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

a = Options()
a.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\Priya Khiwal\Edge Webdriver\edgedriver_win64\msedgedriver.exe")

driver = webdriver.Edge(service=service_obj,options=a)

driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("")