from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

a = Options()
a.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\Priya Khiwal\Chrome Webdriver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, chrome_options=a)

browserSortedVeggielist = []

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on column header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

# collect all veggie names -> browserSortedVeggielist
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")

for ele in veggieWebElements :
    browserSortedVeggielist.append(ele.text)

originalBrowserSortedList = browserSortedVeggielist.copy()

# Sort this browserSortedVeggielist -> newSortedList
browserSortedVeggielist.sort()

# browserSortedVeggielist == newSortedList

assert browserSortedVeggielist == originalBrowserSortedList

