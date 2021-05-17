from pages.filter_bodystyle_results_page import FilterResultsPage
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager
from nose.plugins.attrib import attr
###

##nosetests testcases/checkbox_page_test.py --with-html --html-file=nosetestsnew.html

#nosetests -s -v --nologcapture -a group=smoke all_tests.py

#nosetests -s -v --nologcapture -a group=smoke testcases/filter_by_Price_test.py testcases/filter_by_BodyStyle_test.py


#nosetests -s -v --nologcapture -a group=smoke testcases/filter_by_Price_test.py testcases/filter_by_BodyStyle_test.py --with-html --html-file=nosetestsnew.html
####

class Filter_By_Price(DriverManager):
    @attr(group=['smoke'])
    def test_filter_by_price(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_on_element("//div[@class='searchFiltersFilter'][3]//div[@class='button___1zwWw filterDropDownButton']/span")
        welcome_page.slide_price_bar("//div[@class='handle___1xiof handle___1xiof-0 ']")
        welcome_page.click_on_element("//span[contains(text(),'Close')]")



