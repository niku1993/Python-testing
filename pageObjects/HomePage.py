from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    CheckBox = (By.ID, "exampleCheck1")
    Gender = (By.ID, "exampleFormControlSelect1")
    submitForm = (By.XPATH, "//input[@value='Submit']")
    SuccessMessage = (By.CSS_SELECTOR, "[class*='alert-success']")


    def shopItems (self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return  self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.CheckBox)

    def getGender(self):
        return self.driver.find_element(*HomePage.Gender)

    def getSubmitForm(self):
        return self.driver.find_element(*HomePage.submitForm)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.SuccessMessage)