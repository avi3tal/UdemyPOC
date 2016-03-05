'''
@author: avi
'''
from udemylib.pom.page import Page
from udemylib.webelement import Search as SearchElement, CheckBox


class Search(SearchElement):
    def __init__(self):
        self.locator = 'name=q'
        self.wait_to = "id=ud_courseimpressiontracker"


class Free(CheckBox):
    def __init__(self):
        self.locator = "xpath=//div[@id='ud_courseimpressiontracker']/div[2]/div/div/div/div/ul/li/ul/li[2]/a/label/span/i"
        self.wait_to = "id=ud_courseimpressiontracker"


class ListRow(object):
    def __init__(self, element):
        self.element = element

    @property
    def free(self):
        return 'Free' in self.element.find_element_by_locator("class=price").text

    @property
    def title(self):
        return self.element.find_element_by_locator("class=title").text


class WebDevelopment(Page):
    loc = {
        'main_page': "xpath=//h1[contains(text(), 'Web Development')]"}

    def wait_until_loaded(self, loc=None):
        loc = loc or WebDevelopment.loc['main_page']
        self.wait_for_available(loc)
        return self

    search = Search()
    free = Free()

    @property
    def courses(self):
        html_list = self.find_element_by_locator("id=courses")
        return [ListRow(li) for li in html_list.find_elements_by_locator("tag=li")]