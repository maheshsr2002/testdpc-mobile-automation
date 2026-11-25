from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class SystemUpdatePolicyPage(BasePage):
    """Page Object for System Update Policy screen (system_update_policy.xml)."""

    CURRENT_POLICY_TEXT = (AppiumBy.ID, f"{APP_PACKAGE}:id/system_update_policy_current")
    POLICY_SELECTION_GROUP = (AppiumBy.ID, f"{APP_PACKAGE}:id/system_update_policy_selection")
    AUTOMATIC_RADIO = (AppiumBy.ID, f"{APP_PACKAGE}:id/system_update_policy_automatic")
    WINDOWED_RADIO = (AppiumBy.ID, f"{APP_PACKAGE}:id/system_update_policy_Windowed")
    POSTPONE_RADIO = (AppiumBy.ID, f"{APP_PACKAGE}:id/system_update_policy_postpone")
    NONE_RADIO = (AppiumBy.ID, f"{APP_PACKAGE}:id/system_update_policy_none")
    WINDOWED_DETAILS_LAYOUT = (AppiumBy.ID, f"{APP_PACKAGE}:id/system_update_policy_windowed_details")
    START_WINDOW_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/system_update_policy_window_start")
    END_WINDOW_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/system_update_policy_window_end")
    SET_POLICY_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/system_update_policy_set")

    def get_current_policy_text(self) -> str:
        """Retrieve currently configured update policy description."""
        return self.get_text(self.CURRENT_POLICY_TEXT)

    def select_automatic(self) -> None:
        """Select Automatic update policy."""
        self.tap(self.AUTOMATIC_RADIO)

    def select_windowed(self) -> None:
        """Select Windowed maintenance policy."""
        self.tap(self.WINDOWED_RADIO)

    def select_postpone(self) -> None:
        """Select Postpone update policy."""
        self.tap(self.POSTPONE_RADIO)

    def select_none(self) -> None:
        """Select None update policy."""
        self.tap(self.NONE_RADIO)

    def tap_set_policy(self) -> None:
        """Click the 'Set Policy' button."""
        self.tap(self.SET_POLICY_BUTTON)

    def is_windowed_details_visible(self) -> bool:
        """Check whether windowed start/end time settings are displayed."""
        return self.is_displayed(self.WINDOWED_DETAILS_LAYOUT)
