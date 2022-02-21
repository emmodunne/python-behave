from nose.tools import assert_in

from features.browser import Browser


class LoginPageElements(object):

    USER = 'username'
    PASS = 'password'
    SUBMIT = 'submit'


class LoginPage(Browser):
    # login page actions

    def navigate_to_login_page(self):
        self.driver.get('http://localhost:8082/spring-security-web-login/login.html')

    def get_page_title(self):
        return self.driver.title

    def get_login_error(self):
        text = 'Bad credentials'
        assert_in(text, self.driver.page_source)

    def set_username(self, username):
        user_name_field = self.driver.find_element_by_name(LoginPageElements.USER)
        user_name_field.send_keys(username)

    def set_password(self, password):
        user_name_field = self.driver.find_element_by_name(LoginPageElements.PASS)
        user_name_field.send_keys(password)

    def submit_login(self):
        self.driver.find_element_by_name(LoginPageElements.SUBMIT).click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.submit_login()
