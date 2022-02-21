from behave import *


# navigate to gmail using the url set in login_page.py
# if title is 'Gmail' then navigation was successful
@given('user is on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()

# username and password parameters are set in login.feature
@when('user enters username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)
    
# if the user can access the account button and sign out then they are logged in
@then('the user is logged in')
def step_impl(context):
    context.home_page.assert_login_success()

# if the invalid password error appears an invalid password was entered
@then('the user is not logged in')
def step_impl(context):
    context.login_page.get_login_error()
