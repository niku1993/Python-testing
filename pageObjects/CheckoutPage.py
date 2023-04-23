from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOutClick = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout = (By.XPATH, "//button[@class='btn btn-success']")


    def getCardTitles (self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter (self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getClick (self):
        return self.driver.find_element(*CheckoutPage.checkOutClick)

    def checkOutItems (self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
