from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class AddAccountPage(BasePage):
    """Page Object for the Add Account screen (activity_add_account.xml)."""

    HEADER_TITLE = (AppiumBy.ID, f"{APP_PACKAGE}:id/suw_layout_title")
    ACCOUNT_OPTIONS_GROUP = (AppiumBy.ID, f"{APP_PACKAGE}:id/add_account_options")
    ADD_ACCOUNT_RADIO = (AppiumBy.ID, f"{APP_PACKAGE}:id/add_account")
    ADD_ACCOUNT_WITH_NAME_RADIO = (AppiumBy.ID, f"{APP_PACKAGE}:id/add_account_with_name")
    SKIP_ACCOUNT_RADIO = (AppiumBy.ID, f"{APP_PACKAGE}:id/add_account_skip")
    NEXT_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/suw_navbar_next")
    BACK_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/suw_navbar_back")

    def get_header_title(self) -> str:
        """Retrieve the header title."""
        return self.get_text(self.HEADER_TITLE)

    def select_add_account(self) -> None:
        """Select 'Add account' radio option."""
        self.tap(self.ADD_ACCOUNT_RADIO)

    def select_add_account_with_name(self) -> None:
        """Select 'Add account with name' radio option."""
        self.tap(self.ADD_ACCOUNT_WITH_NAME_RADIO)

    def select_skip(self) -> None:
        """Select 'Skip' radio option."""
        self.tap(self.SKIP_ACCOUNT_RADIO)

    def is_skip_selected(self) -> bool:
        """Check if skip option is currently selected."""
        return self.is_selected(self.SKIP_ACCOUNT_RADIO)

    def is_add_account_selected(self) -> bool:
        """Check if add account option is selected."""
        return self.is_selected(self.ADD_ACCOUNT_RADIO)

    def tap_next(self) -> None:
        """Tap Next button."""
        self.tap(self.NEXT_BUTTON)

    def tap_back(self) -> None:
        """Tap Back button."""
        self.tap(self.BACK_BUTTON)
