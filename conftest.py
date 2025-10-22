import pytest
from utils.driver_factory import DriverFactory


@pytest.fixture(scope="Session")
def driver():
    """Fixture to initialize and quit the WebDriver."""
    print("\n🚀 Launching the browser ...")
    driver_instance = DriverFactory.create_driver()
    
    yield driver_instance
    
    print("\n🛑 Closing browser...")

    DriverFactory.quit_driver(driver_instance)
    
