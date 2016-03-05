'''
@author: avi
'''
from udemylib.pom import page
from udemylib.pom.courses import Courses
from udemylib import errors
from udemylib.webelement import WebElement

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException


class _LogIn(WebElement):
    locators = {
        'email': 'id=id_email',
        'password': 'id=id_password',
        'submit': 'id=submit-id-submit',
        'error': 'class=form-error',
        'user-dropdown': 'class=user-dropdown'}

    def __init__(self, element):
        super(_LogIn, self).__init__(element)
        self.__email = None
        self.__password = None

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, val):
        self.__email = val
        e = self.find_element_by_locator(_LogIn.locators['email'])
        e.send_keys(val)
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, val):
        self.__password = val
        e = self.find_element_by_locator(_LogIn.locators['password'])
        e.send_keys(val)

    def submit(self):
        e = self.find_element_by_locator(_LogIn.locators['submit'])
        e.click()
        try:
            e = self.login_error_displayed()
            raise errors.LoginError('Failed to login {}'.format(e))
        except NoSuchElementException:
            # Meaning login succeeded
            pass

    def login_error_displayed(self):
        e = self.find_element_by_locator(_LogIn.locators['error'])
        return e


class Base(page.Page):
    locators = {
    'login': 'class=ud-popup',
    'login_box': 'class=loginbox-v4',
    'main_page': 'class=search-inp-container'}

    def login(self, email, password):
        self.wait_until_loaded()
        self.find_element_by_locator(Base.locators["login"]).click()
        self.wait_for_available(Base.locators['login_box'])
        login = _LogIn(self.find_element_by_locator(Base.locators['login_box']))
        login.email = email
        login.password = password
        login.submit()
        return Courses(self.driver).wait_until_loaded()
    
    def open(self, page_url):
        self.driver.get(page_url)
        return self.wait_until_loaded()
    
    def wait_until_loaded(self):
        self.wait_for_available(Base.locators['main_page'])
        return self