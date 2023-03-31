from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

a = Options()
a.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\Priya Khiwal\Chrome Webdriver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, chrome_options=a)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1235689")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("NIK")
# driver.find_element(By.ID,"exampleFormControlSelect1").click()
#dropdownStatic

dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")
# dropdown.select_by_value()
# if there is value attribute given, we can select_by_value as well (above mentioned), however in this example value attribute is not given

# driver.find_element(By.ID,"inlineRadio2").click()
driver.find_element(By.CSS_SELECTOR,"input[id='inlineRadio2']").click()
driver.find_element(By.NAME,"bday").send_keys("26-08-1993")

#driver.find_element(By.CLASS_NAME,"btn.btn-success").click()

# to click on Submit button, we can use XPATH locator as well. Syntax for XPATH : //tagname[@attribute='value']

driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("U 1993")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()