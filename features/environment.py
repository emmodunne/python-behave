from features.browser import Browser
from features.pages.login_page import LoginPage
from features.pages.home_page import HomePage

def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.home_page = HomePage()

    context.login_page.navigate_to_login_page()


def after_all(context):
    context.browser.close()
