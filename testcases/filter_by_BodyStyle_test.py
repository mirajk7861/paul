from pages.filter_bodystyle_results_page import FilterResultsPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager
from nose.plugins.attrib import attr


class Filter_By_BodyStyle(DriverManager):
    @attr(group=['smoke'])
    def test_filter_by_bodyStyle(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_on_element("//div[@class='searchFiltersFilter'][2]//div[@class='button___1zwWw filterDropDownButton']/span")
        welcome_page.toggleCheckbox("//input[@value='CampingBus']//following-sibling::span[@class='checkbox___2AreI']", "Check")
        welcome_page.toggleCheckbox("//div[@data-value='Van']//span[@class='checkbox___2AreI']",
                                    "Check")
        welcome_page.click_on_element("//div[@class='searchFiltersFilter'][2]//div[@class='button___1zwWw filterDropDownButton']/span")

        filterresults_bodytype = FilterResultsPage(self.driver)
        filterresults_bodytype.verify_mismatch_elements_present("//div[@class='nameLine___2lL3C camperCardNameLine']/span[text()='Camper bus']")
        filterresults_bodytype.verify_mismatch_elements_present("//div[@class='nameLine___2lL3C camperCardNameLine']/span[text()='Box van']")


