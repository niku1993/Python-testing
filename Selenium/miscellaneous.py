from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

a = Options()
a.add_experimental_option("detach", True)
# a.add_argument("headless")
# headless mode is when test is running in background, it is not visible or it will not open any browser in the frontend

service_obj = Service(r"C:\Users\Priya Khiwal\Chrome Webdriver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, chrome_options=a)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scroll(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")