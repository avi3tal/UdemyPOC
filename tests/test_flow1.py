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
        webdev = courses.browse_courses.development(hover=True).web_development
#         dev = courses.browse_courses.development(hover=False)
#         webdev = dev.lmenu.web_development()
        webdev.search = "selenium"
        webdev.free = True
        self.assertTrue(2 <= len(webdev.courses) <= 10, "Courses count is not between 2 - 10")
        assert [c for c in webdev.courses if c.free]
        assert [c for c in webdev.courses if "Selenium" in c.title]