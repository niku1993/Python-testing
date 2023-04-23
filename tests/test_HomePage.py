import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])  # homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys(getData["lastname"])  # homepage.getEmail().send_keys(getData[1])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(),
                                getData["gender"])  # self.selectOptionByText(homepage.getGender(), getData[2])
        homepage.getSubmitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert "Success" in alertText
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param