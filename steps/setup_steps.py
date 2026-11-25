import time
from pages.setup_management_page import SetupManagementPage


class SetupSteps:
    """Step definitions for TestDPC Setup screen choreography (business flows without assertions)."""

    def __init__(self, driver):
        self.setup_page = SetupManagementPage(driver)

    def read_initial_setup_screen(self) -> dict:
        """Capture current screen state and details."""
        header = self.setup_page.get_header_title()
        time.sleep(1)
        return {
            "current_package": self.setup_page.driver.current_package,
            "current_activity": self.setup_page.driver.current_activity,
            "header_title": header,
            "is_managed_profile_selected": self.setup_page.is_managed_profile_selected(),
            "is_device_owner_selected": self.setup_page.is_device_owner_selected(),
        }

    def choose_managed_profile_and_continue(self) -> None:
        """Select managed profile and proceed to next screen."""
        time.sleep(1)
        self.setup_page.select_managed_profile()
        time.sleep(1.5)
        self.setup_page.tap_next()
        time.sleep(1.5)

    def choose_device_owner_and_continue(self) -> None:
        """Select device owner and proceed to next screen."""
        time.sleep(1)
        self.setup_page.select_device_owner()
        time.sleep(1.5)
        self.setup_page.tap_next()
        time.sleep(1.5)

    def switch_to_device_owner(self) -> None:
        """Switch radio selection to device owner."""
        time.sleep(1)
        self.setup_page.select_device_owner()
        time.sleep(1)

    def switch_to_managed_profile(self) -> None:
        """Switch radio selection to managed profile."""
        time.sleep(1)
        self.setup_page.select_managed_profile()
        time.sleep(1)
