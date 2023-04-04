from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

a = Options()
a.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\Priya Khiwal\Chrome Webdriver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, chrome_options=a)

a.add_argument("headless")
a.add_argument("--start-maximized")
a.add_argument("--ignore-certificate-errors")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")