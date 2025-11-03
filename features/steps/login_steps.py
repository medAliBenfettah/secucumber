# from behave import given, when, then
# from pages.login_page import LoginPage
# from typing import TYPE_CHECKING
# import allure


# @given('Im on the OrangeHRM login page')
# def step_impl_given_on_login_page(context):
#     # assign and cast so static analysis can infer type for context.login_page
#     context.login_page = LoginPage(context.driver)
#     context.login_page.open()
#     assert context.login_page.is_login_page_displayed(), "Login page is not displayed"
    
    
# @when('I login with username "{username}"')
# def step_impl_enter_username(context, username):
#     context.login_page.enter_username(username)
    
# @when('I login with password "{password}"')
# def step_impl_enter_password(context, password):
#     context.login_page.enter_password(password)
    
# @when('I click the login button')
# def step_impl_click_login_button(context):
#     context.login_page.click_login_button()
    
# @when('I leave the username field blank')
# def step_impl_leave_username_blank(context):
#     pass

# @when('I leave the password field blank')
# def step_impl_leave_password_blank(context):
#     pass

# @when('I click the forget password link')
# def step_impl_click_forget_password_link(context):
#     context.login_page.click_forget_password_link()
    
# @then('I should see the dashboard')
# def step_impl_verify_dashboard(context):
#     """
#     Verify that login was successful and dashboard is displayed
#     """
#     assert context.login_page.is_login_successful(), \
#         "Login failed - Dashboard not displayed"


# @then('I should see the user dropdown in the header')
# def step_impl_verify_user_dropdown(context):
#     """
#     Verify user dropdown is visible (another indicator of successful login)
#     """
#     assert context.login_page.is_user_dropdown_displayed(), \
#         "User dropdown not visible"
        
# @then('I should see an error message')
# def step_impl_verify_error_message(context):
#     """
#     Verify that an error message is displayed
#     """
#     assert context.login_page.is_error_message_displayed(), \
#         "Error message not displayed"
    
#     # Take screenshot for documentation
#     context.login_page.take_screenshot("error_message_displayed")


# @then('the error message should contain "{expected_text}"')
# def step_impl_verify_error_text(context, expected_text):
#     """
#     Verify error message contains specific text
    
#     Args:
#         context: Behave context
#         expected_text: Text that should be in the error message
#     """
#     actual_message = context.login_page.get_error_message_text()
#     assert expected_text.lower() in actual_message.lower(), \
#         f"Expected '{expected_text}' in error message, but got '{actual_message}'"


# @then('I should remain on the login page')
# def step_impl_verify_still_on_login_page(context):
#     """
#     Verify user is still on login page (login failed)
#     """
#     assert context.login_page.is_login_page_displayed(), \
#         "Not on login page anymore"


# @then('I should see the forgot password link')
# def step_impl_verify_forgot_password_link(context):
#     """
#     Verify forgot password link is visible
#     """
#     assert context.login_page.is_element_visible(
#         context.login_page.FORGET_PASSWORD_LINK
#     ), "Forgot password link not visible"


# @then('I should be redirected to password reset page')
# def step_impl_verify_password_reset_page(context):
#     """
#     Verify user was redirected to password reset page
#     """
#     current_url = context.login_page.get_current_url()
#     assert "requestPasswordResetCode" in current_url, \
#         f"Not on password reset page. Current URL: {current_url}"

from behave import given, when, then
from pages.login_page import LoginPage
import allure


# ==================== GIVEN STEPS (Preconditions) ====================

@given('I am on the OrangeHRM login page')
def step_impl_given_on_login_page(context):
    """
    Navigate to the login page
    
    Args:
        context: Behave context object containing driver
    """
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    assert context.login_page.is_login_page_displayed(), "Login page not loaded"


# ==================== WHEN STEPS (Actions) ====================

@when('I enter valid username "{username}"')
def step_impl_enter_username(context, username):
    """
    Enter username into username field
    
    Args:
        context: Behave context
        username: Username to enter (captured from Gherkin step)
    """
    context.login_page.enter_username(username)


@when('I enter valid password "{password}"')
def step_impl_enter_password(context, password):
    """
    Enter password into password field
    
    Args:
        context: Behave context
        password: Password to enter (captured from Gherkin step)
    """
    context.login_page.enter_password(password)


# ---- Additional step aliases to handle typos / alternate phrasing from feature files ----


@when('I enter invalid username "{username}"')
def step_impl_enter_invalid_username(context, username):
    """Alias to support steps that use the word 'invalid' explicitly."""
    context.login_page.enter_username(username)


@when('I enter invalid password "{password}"')
def step_impl_enter_invalid_password(context, password):
    """Alias to support steps that use the word 'invalid' explicitly."""
    context.login_page.enter_password(password)


@when('II click on the login button')
def step_impl_click_login_typo(context):
    """Handle typo in feature file where 'I' was typed twice."""
    context.login_page.click_login_button()


@then('I should see and error message "{expected_text}"')
def step_impl_verify_error_message_typo(context, expected_text):
    """Handle typo 'and' instead of 'an' in feature file and verify error text."""
    actual_message = context.login_page.get_error_message_text()
    assert expected_text.lower() in actual_message.lower(), (
        f"Expected '{expected_text}' in error message, but got '{actual_message}'"
    )


# Accept single-quoted parameter variants from Scenario Outline examples
@when("I enter username '{username}'")
def step_impl_enter_username_single_quote(context, username):
    context.login_page.enter_username(username)


@when("I enter password '{password}'")
def step_impl_enter_password_single_quote(context, password):
    context.login_page.enter_password(password)


@when('I leave the username field empty')
def step_impl_leave_username_field_empty(context):
    # Keep consistent behavior: do nothing so field remains empty
    pass


@when('I leave the password field empty')
def step_impl_leave_password_field_empty(context):
    # Keep consistent behavior: do nothing so field remains empty
    pass


@when('I click on the login button')
def step_impl_click_login(context):
    """Click the login button"""
    context.login_page.click_login_button()


@when('I enter username "{username}"')
def step_impl_enter_username_generic(context, username):
    """Generic username entry (without 'valid')"""
    context.login_page.enter_username(username)


@when('I enter password "{password}"')
def step_impl_enter_password_generic(context, password):
    """Generic password entry (without 'valid')"""
    context.login_page.enter_password(password)


@when('I click the login button')
def step_impl_click_login_generic(context):
    """Generic login button click"""
    context.login_page.click_login_button()


@when('I leave username field empty')
def step_impl_leave_username_empty(context):
    """Don't enter anything in username field"""
    # Do nothing - field remains empty
    pass


@when('I leave password field empty')
def step_impl_leave_password_empty(context):
    """Don't enter anything in password field"""
    # Do nothing - field remains empty
    pass


@when('I click the forgot password link')
def step_impl_click_forgot_password(context):
    """Click the forgot password link"""
    context.login_page.click_forgot_password()


# ==================== THEN STEPS (Assertions/Verifications) ====================

@then('I should be redirected to the dashboard page')
def step_impl_verify_dashboard(context):
    """
    Verify that login was successful and dashboard is displayed
    """
    assert context.login_page.is_login_successful(), \
        "Login failed - Dashboard not displayed"


@then('I should see the dropdown in the header')
def step_impl_verify_user_dropdown(context):
    """
    Verify user dropdown is visible (another indicator of successful login)
    """
    assert context.login_page.is_user_dropdown_displayed(), \
        "User dropdown not visible"


@then('I should see the dashboard')
def step_impl_verify_dashboard_generic(context):
    """Generic dashboard verification"""
    assert context.login_page.is_login_successful(), \
        "Login failed - Dashboard not displayed"


@then('I should see the user dropdown in the header')
def step_impl_verify_user_dropdown_generic(context):
    """Generic user dropdown verification"""
    assert context.login_page.is_user_dropdown_displayed(), \
        "User dropdown not visible"


@then('I should see an error message')
def step_impl_verify_error_message(context):
    """
    Verify that an error message is displayed
    """
    assert context.login_page.is_error_message_displayed(), \
        "Error message not displayed"
    
    # Take screenshot for documentation
    context.login_page.take_screenshot("error_message_displayed")


@then('the error message should contain "{expected_text}"')
def step_impl_verify_error_text(context, expected_text):
    """
    Verify error message contains specific text
    
    Args:
        context: Behave context
        expected_text: Text that should be in the error message
    """
    actual_message = context.login_page.get_error_message_text()
    assert expected_text.lower() in actual_message.lower(), \
        f"Expected '{expected_text}' in error message, but got '{actual_message}'"


@then('I should remain on the login page')
def step_impl_verify_still_on_login_page(context):
    """
    Verify user is still on login page (login failed)
    """
    assert context.login_page.is_login_page_displayed(), \
        "Not on login page anymore"


@then('I should see the forgot password link')
def step_impl_verify_forgot_password_link(context):
    """
    Verify forgot password link is visible
    """
    assert context.login_page.is_element_visible(
        context.login_page.FORGOT_PASSWORD_LINK
    ), "Forgot password link not visible"


@then('I should be redirected to password reset page')
def step_impl_verify_password_reset_page(context):
    """
    Verify user was redirected to password reset page
    """
    current_url = context.login_page.get_current_url()
    assert "requestPasswordResetCode" in current_url, \
        f"Not on password reset page. Current URL: {current_url}"