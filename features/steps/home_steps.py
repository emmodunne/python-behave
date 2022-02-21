from behave import *

@given('user is on the homepage')
def step_impl(context):
    context.home_page.assert_login_success()
