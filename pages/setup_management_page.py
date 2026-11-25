from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class SetupManagementPage(BasePage):
    """Page Object for the initial Setup Management screen in TestDPC."""

    # Locators dynamically formatted with APP_PACKAGE
    HEADER_TITLE = (AppiumBy.ID, f"{APP_PACKAGE}:id/suw_layout_title")
    SETUP_OPTIONS_GROUP = (AppiumBy.ID, f"{APP_PACKAGE}:id/setup_options")
    MANAGED_PROFILE_RADIO = (AppiumBy.ID, f"{APP_PACKAGE}:id/setup_managed_profile")
    DEVICE_OWNER_RADIO = (AppiumBy.ID, f"{APP_PACKAGE}:id/setup_device_owner")
    NEXT_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/suw_navbar_next")
    BACK_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/suw_navbar_back")
    MORE_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/suw_navbar_more")

    def get_header_title(self) -> str:
        """Retrieve screen header text."""
        return self.get_text(self.HEADER_TITLE)

    def is_managed_profile_selected(self) -> bool:
        """Check whether 'Set up managed profile' radio option is selected."""
        return self.is_selected(self.MANAGED_PROFILE_RADIO)

    def is_device_owner_selected(self) -> bool:
        """Check whether 'Set up device owner' radio option is selected."""
        return self.is_selected(self.DEVICE_OWNER_RADIO)

    def select_managed_profile(self) -> None:
        """Select 'Set up managed profile' option."""
        self.tap(self.MANAGED_PROFILE_RADIO)

    def select_device_owner(self) -> None:
        """Select 'Set up device owner' option."""
        self.tap(self.DEVICE_OWNER_RADIO)

    def tap_next(self) -> None:
        """Click the bottom navigation 'Next' button."""
        self.tap(self.NEXT_BUTTON)

    def tap_back(self) -> None:
        """Click the bottom navigation 'Back' button."""
        self.tap(self.BACK_BUTTON)
