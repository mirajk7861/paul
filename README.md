

This is web automation framework, implemented using Python & Webdriver. 
Page Object Model (POM) is used to  make the code more readable, maintainable, and reusable.

## _Prerequisite:_

1. Python
2. pip
3. Selenium/WebDriver
4. nosetests & nose-html-reporting
5. Browsers (Firefox, Chrome, IE)
6. Respective Browser drivers
7. Pycharm

### How to run?

###


#nosetests -s -v --nologcapture -a group=smoke testcases/filter_by_Price_test.py testcases/filter_by_BodyStyle_test.py --with-html --html-file=nosetestsnew.html




**_Note:_** Kindly set the respective browser's driver path either to System variable or update it in `drivermanager.py`

e.g: self.driver = webdriver.Firefox(executable_path="geckodriver path") # in case of Firefox browser.




***

## _Coverage Plan:_

| Contents                  |                                 | Status |
|---------------------------|---------------------------------|--------|
|                           |                                 |        |
| Framework level           | Page Object Model               | Done   |
|                           | Profiles                        | Done   |
|                           | Grids                           |        |
|                           | Cross browsers & cross platform |        |
|                           |                                 |        |
| Locators                  | Learning how to get locators.   |        |
|                           |                                 |        |
| Functionality To Automate | Challenging DOM                 | Done   |
|                           | Checkboxes                      | Done   |
|                           | Context Menu                    | Done   |
|                           | Disappearing Elements           | Done   |
|                           | Drag and Drop                   | Done   |
|                           | Dropdown                        | Done   |
|                           | Dynamic Content                 |        |
|                           | Dynamic Controls                | Done   |
|                           | Dynamic Loading                 | Done   |
|                           | File Download                   | Done   |
|                           | File Upload                     | Done   |
|                           | Floating Menu                   |        |
|                           | Frames                          | Done   |
|                           | Horizontal Slider               |        |
|                           | Hovers                          | Done   |
|                           | Infinite Scroll                 |        |
|                           | JQuery UI Menus                 |        |
|                           | JavaScript Alerts               |        |
|                           | Key Presses                     |        |
|                           | Large & Deep DOM                |        |
|                           | Multiple Windows                | Done   |
|                           | Nested Frames                   | Done   |
|                           | Notification Messages           |        |
|                           | Redirect Link                   |        |
|                           | Shifting Content                |        |





