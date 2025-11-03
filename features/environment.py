# from selenium import webdriver
# from utils.config import Config
# from utils.driver_factory import DriverFactory
# import allure
# try:
#     from allure_behave.hooks import allure_reporter
# except Exception:
#     # allure-behave integration is optional; if not installed we still want tests to run
#     allure_reporter = None

# def before_all(context):
#     print("\n" + "="*50)
#     print("🚀 Starting Test Execution")
#     print("="*50)

# def before_scenario(context, scenario):
#     print(f"\n▶️  Starting Scenario: {scenario.name}"))
    
#     #creating the webDriver instance
#     context.driver = DriverFactory.create_driver()
#     context.driver.maximize_window()
    
#     context.config = Config(
    
#     allure.dynamic.title(scenario.name)
#     allure.dynamic.description(f"Testing: {scenario.name}")
    
#     for tag in scenario.tags:
#         allure.dynamic.tag(tag)

# def after_scenario(context, scenario):
#     if scenario.status == "failed":
#         print(f"❌ Scenario Failed: {scenario.name}")
        
#         # Take screenshot and attach to Allure report
#         try:
#             screenshot = context.driver.get_screenshot_as_png()
#             allure.attach(
#                 screenshot,
#                 name=f"failure_{scenario.name}",
#                 attachment_type=allure.attachment_type.PNG
#             )
#         except Exception as e:
#             print(f"Could not take screenshot: {e}")
#     else:
#         print(f"✅ Scenario Passed: {scenario.name}")
    
#     # Close browser
#     if hasattr(context, 'driver'):
#         # use the existing quit_driver from DriverFactory
#         DriverFactory.quit_driver(context.driver)

# def after_all(context):
#     print("\n" + "="*50)
#     print("🏁 Test Execution Completed")
#     print("="*50)

from utils.driver_factory import DriverFactory
from utils.config import Config

print("✅ environment.py: Imports successful")  # Debug line


def before_all(context):
    """Runs once before all tests"""
    print("\n" + "="*50)
    print("🚀 Starting Test Execution")
    print("="*50)


def before_scenario(context, scenario):
    """Runs before each scenario"""
    print(f"\n▶️  Starting Scenario: {scenario.name}")
    print("Creating driver...")  # Debug line
    
    # Create WebDriver instance
    context.driver = DriverFactory.create_driver()
    print("Driver created successfully")  # Debug line
    
    context.driver.maximize_window()
    print("Window maximized")  # Debug line
    
    # Store config under a different attribute name to avoid clashing with behave's internal 'config'
    print("Setting context.config_obj...")  # Debug line
    context.config_obj = Config
    print(f"context.config_obj set to: {context.config_obj}")  # Debug line


def after_scenario(context, scenario):
    """Runs after each scenario"""
    if scenario.status == "failed":
        print(f"❌ Scenario Failed: {scenario.name}")
    else:
        print(f"✅ Scenario Passed: {scenario.name}")
    
    # Close browser
    if hasattr(context, 'driver'):
        # use DriverFactory.quit_driver which exists
        DriverFactory.quit_driver(context.driver)


def after_all(context):
    """Runs once after all tests"""
    print("\n" + "="*50)
    print("🏁 Test Execution Completed")
    print("="*50)