
import logging

from pages.welcome_page import WelcomePage
from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class FilterResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)


    def verify_mismatch_elements_present(self, xpath):
        self.services.assert_mismatch_elements_present(xpath)

    def verifypriceFilter(self, ):
        welcome_page = WelcomePage(self.driver)
        actual_price = welcome_page.services.get_text_by_xpath("//div[@class='min___1uvut']")
        expected_price =self.services.getTextOfElement("div[@class ='button___1zwWw filterDropDownButton button_active___10hA1 filterDropDownButtonActive']")
        assert actual_price == expected_price, "price selected and price displayed should match"
