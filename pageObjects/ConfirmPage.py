from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    selectCountry = (By.LINK_TEXT, "India")
    TandC = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "[type='submit']")
    success = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getCountry (self):
        return self.driver.find_element(*ConfirmPage.country)

    def clickCountry (self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def agreement (self):
        return self.driver.find_element(*ConfirmPage.TandC)

    def clickPurchase (self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def getSuccess (self):
        return  self.driver.find_element(*ConfirmPage.success)