'''
@author: avi
'''
from udemylib.pom.page import Page
from udemylib.pom.development import Development
from udemylib.pom.web_development import WebDevelopment
from udemylib.webelement import WebElement

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class _DevelopmentWE(WebElement):
    '''
    In case of hover, DevelopmentWebElement will expose
    all sub categories as properties
    '''
    def __init__(self, element, driver):
        super(_DevelopmentWE, self).__init__(element)
        self._d = driver

    @property
    def web_development(self):
        e = self.find_element_by_locator("class=ud_web-development")
        e.click()
        return WebDevelopment(self._d).wait_until_loaded()


class LeftMenu(WebElement):
    '''
    Left Menu element to list all elements in the menu and control
    as attributes

    TODO: add all menu elements
    '''
    loc = {
        'devel': "xpath=//li[@data-submenu-id='submenu-development']",
        'toolbar_on': "xpath=//*[class='hide-wrapper-left-btn on']",
        "submenu-devel": "id=submenu-development",
        "menu": "class=dropdown-menu"}

    def __init__(self, element, driver):
        super(LeftMenu, self).__init__(element)
        self._d = driver

    def development(self, hover=True):
        '''
        :description: Not a property in order to support hover or page navigation
        :param hover: hover attribute or navigate to attribute page
        :return: Page if hover=False, WebElement if hover=True
        '''
        e = self.find_elements_by_locator(LeftMenu.loc["devel"])[-1]
        if hover:
            subdev = ActionChains(self._d).move_to_element(e)
            subdev.perform()
            return _DevelopmentWE(e, self._d)
        else:
            # TODO: support navigation from development webpage
            # instead of hover 
            e.click()
            return Development(self._d)


class Courses(Page):

    # FIXME: fined better locators
    loc = {
        'courses': 'class=ud-angular-loaded',
        'toolbar': 'class=hide-wrapper-left-btn',
        'toolbar_on': "xpath=//*[class='hide-wrapper-left-btn on']"}

    def wait_until_loaded(self):
        self.wait_for_available(Courses.loc['courses'])
        return self

    @property
    def browse_courses(self):
        '''
        Property to simplify the access to menu elements
        '''
        # Make sure Browse Courses menu is displayed
        self.browse_courses = True
        return LeftMenu(self.find_element_by_locator(LeftMenu.loc['menu']), self.driver)

    @browse_courses.setter
    def browse_courses(self, on):
        '''
        :description: Control if Browse Courses menu is displayed or not
        :param on: Boolean to control menu display
        
        '''
        try:
            e = self.find_element_by_locator(LeftMenu.loc['menu'])
            if not on:
                e.click()
        except NoSuchElementException:
            if on:
                self.find_element_by_locator(Courses.loc['toolbar']).click()
