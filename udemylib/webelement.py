'''
@author: avi
'''
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement


class WebElement(SeleniumWebElement):
    def __init__(self, element):
        super(WebElement, self).__init__(element.parent, element.id)

    def find_element_by_locator(self, locator):
        locator_type, locator_value = locator.split('=', 1)
        if locator_type == 'class':
            return WebElement(self.find_element_by_class_name(locator_value))
        elif locator_type == 'css':
            return WebElement(self.find_element_by_css_selector(locator_value))
        elif locator_type == 'id':
            return WebElement(self.find_element_by_id(locator_value))
        elif locator_type == 'link':
            return WebElement(self.find_element_by_link_text(locator_value))
        elif locator_type == 'name':
            return WebElement(self.find_element_by_name(locator_value))
        elif locator_type == 'plink':
            return WebElement(self.find_element_by_partial_link_text(locator_value))
        elif locator_type == 'tag':
            return WebElement(self.find_element_by_tag_name(locator_value))
        elif locator_type == 'xpath':
            return WebElement(self.find_element_by_xpath(locator_value))
        else:
            raise Exception('Invalid locator')

    def find_elements_by_locator(self, locator):
        locator_type, locator_value = locator.split('=', 1)
        if locator_type == 'class':
            elements = self.find_elements_by_class_name(locator_value)
        elif locator_type == 'css':
            elements = self.find_elements_by_css_selector(locator_value)
        elif locator_type == 'id':
            elements = self.find_elements_by_id(locator_value)
        elif locator_type == 'link':
            elements = self.find_elements_by_link_text(locator_value)
        elif locator_type == 'name':
            elements = self.find_elements_by_name(locator_value)
        elif locator_type == 'plink':
            elements = self.find_elements_by_partial_link_text(locator_value)
        elif locator_type == 'tag':
            elements = self.find_elements_by_tag_name(locator_value)
        elif locator_type == 'xpath':
            elements = self.find_elements_by_xpath(locator_value)
        else:
            raise Exception('Invalid locator')

        return [WebElement(e) for e in elements]


class Text(object):

    def __set__(self, instance, value):
        try:
            e = instance.element.find_element_by_locator(self.locator)
        except AttributeError:
            e = instance.driver.find_element_by_locator(self.locator)
        if value == "clear()":
            e.clear()
        else:
            e.send_keys(value)

    def __get__(self, instance, owner=None):
        try:
            e = instance.element.find_element_by_locator(self.locator)
        except AttributeError:
            e = instance.driver.find_element_by_locator(self.locator)
        text = None
        if e.tag_name in ["input", "textarea"]:
            text = e.get_attribute("value")
        else:
            text = e.text
        return text


class Search(object):

    def __set__(self, instance, value):
        try:
            d = instance.element
        except AttributeError:
            d = instance.driver
        e = d.find_element_by_locator(self.locator)

        if value == "clear()":
            e.clear()
        else:
            e.send_keys(value)
            e = instance.driver.find_element_by_locator("css=button.ud_i_search.search-btn")
            e.click()
            instance.wait_until_loaded(getattr(self, 'wait_to', None))

    def __get__(self, instance, owner=None):
        try:
            d = instance.element
        except AttributeError:
            d = instance.driver
        e = d.find_element_by_locator(self.locator)

        text = None
        if e.tag_name in ["input", "textarea"]:
            text = e.get_attribute("value")
        else:
            text = e.text
        return text


class CheckBox(object):

    def __set__(self, instance, value):
        try:
            e = instance.element.find_element_by_locator(self.locator)
        except AttributeError:
            e = instance.driver.find_element_by_locator(self.locator)
        if e.is_selected() != value:
            e.click()
            instance.wait_until_loaded(getattr(self, 'wait_to', None))

    def __get__(self, instance, owner=None):
        try:
            e = instance.element.find_element_by_locator(self.locator)
        except AttributeError:
            e = instance.driver.find_element_by_locator(self.locator)
        return e.is_selected()
