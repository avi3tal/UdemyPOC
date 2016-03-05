'''
@author: avi
'''
from udemylib.pom import page
from udemylib.pom.web_development import WebDevelopment
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LeftMenu(object):
    '''
    Left Menu element to access all categories as attributes
    '''
    def __init__(self, driver):
        self._d = driver

    def web_development(self):
        # FIXME: find a better locator for web-development
        e = WebDriverWait(self._d, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.chan-title")))
        e.click()
        return WebDevelopment(self._d).wait_until_loaded()


class Development(page.Page):
    loc = {
        'main': 'class=ud-angular-loaded'}

    def wait_until_loaded(self):
        self.wait_for_available(Development.loc['main'])
        return self
    
    @property
    def lmenu(self):
        return LeftMenu(self.driver)