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

        log = self.getLogger()

        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()

        log.info("getting all the card titles")

        cards = checkoutPage.getCardTitles()

        confirmPage = ConfirmPage(self.driver)

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        checkoutPage.getClick().click()
        confirmPage = checkoutPage.checkOutItems()
        log.info("Entering country name as India")

        confirmPage.getCountry().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.clickCountry().click()
        confirmPage.agreement().click()
        confirmPage.clickPurchase().click()
        textMatch = confirmPage.getSuccess().text
        log.info("Text received from application is" + textMatch)

        assert ('Success! Thank you!' in textMatch)