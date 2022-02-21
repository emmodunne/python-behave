from nose.tools import assert_true

from features.browser import Browser


class HomePageElements(object):

    PAGE_TEXT = 'userText'

class HomePage(Browser):

    def assert_login_success(self):
        assert_true(self.driver.find_element_by_id(HomePageElements.PAGE_TEXT))

    def get_page_title(self):
        return self.driver.title

