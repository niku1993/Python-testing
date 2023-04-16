import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        checkoutPage = CheckoutPage(self.driver)
        cards = checkoutPage.getCardTitles()

        confirmPage = ConfirmPage(self.driver)

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        checkoutPage.getClick().click()
        time.sleep(5)
        checkoutPage.checkOutItems().click()

        confirmPage.getCountry().send_keys("ind")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        confirmPage.clickCountry().click()
        confirmPage.agreement().click()
        confirmPage.clickPurchase().click()
        textMatch = confirmPage.getSuccess().text

        assert ('Success! Thank you!' in textMatch)