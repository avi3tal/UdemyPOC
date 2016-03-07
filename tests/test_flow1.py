'''
@author: avi
'''
import pytest
import unittest
from udemylib.driver import WebDriver

conf = {'driver_args': {'desired_capabilities': {'browserName': 'firefox'},
                        'command_executor': 'http://127.0.0.1:4444/wd/hub'},
        'page_url': "https://www.udemy.com/",
        'login': {'email': 'avi3tal@gmail.com',
                  'password': '123456'}}

from udemylib.pom.base import Base


class TestUdemyFlow1(unittest.TestCase):
    def setup_method(self, method):
        self.driver = WebDriver(**conf['driver_args'])

    def teardown_method(self, method):
        self.driver.close()
        self.driver.quit()

    def test_login(self):
        page = Base(self.driver).open(conf['page_url'])
        print page.login(**conf['login'])

    @pytest.mark.testme
    def test_goodluck(self):
        '''
        :description: main test described in README.rst
        '''
        page = Base(self.driver).open(conf['page_url'])
        courses = page.login(**conf['login'])
        # NOTE: in case hover=True Failed to navigate
        # comment line 38 and uncomment lines 39-40
        webdev = courses.browse_courses.development(hover=True).web_development
#         dev = courses.browse_courses.development(hover=False)
#         webdev = dev.lmenu.web_development()
        webdev.search = "selenium"
        webdev.free = True

        # check courses len is higher or equel to 2 or lower or equal to 10
        self.assertTrue(2 <= len(webdev.courses) <= 10,
            "Failed to verify Courses count is between 2 - 10")

        # Filter only Free courses and verify that the len before the filter
        # and after the filter is equal
        assert len([c for c in webdev.courses if c.free]) == len(webdev.courses), "Failed to verify All courses are Free"

        # Filter courses with Selenium in title so that only if list is empty
        # assertion Error will raise.
        assert [c for c in webdev.courses if "Selenium" in c.title], "Failed to verify at least one course has Selenium in title"