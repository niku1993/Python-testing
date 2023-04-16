import pytest as pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# import time

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        driver = webdriver.Chrome(executable_path=r"C:\Users\Priya Khiwal\Chrome Webdriver\chromedriver_win32\chromedriver.exe")
    elif browser_name == "firefox":
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=r"C:\Users\Priya Khiwal\geckodriver-v0.33.0-win32\geckodriver.exe", options=options)
    elif browser_name == "edge":
        # options = Options()
        # options.binary_location = r'C:\Users\Priya Khiwal\Downloads\MicrosoftEdgeSetup.exe'
        driver = webdriver.Edge(executable_path=r"C:\Users\Priya Khiwal\Downloads\edgedriver_win32\msedgedriver.exe")


    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

