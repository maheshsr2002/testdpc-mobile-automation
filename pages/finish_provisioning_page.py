from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class FinishProvisioningPage(BasePage):
    """Page Object for Provisioning completion screen (enable_profile_activity.xml / enable_device_owner_activity.xml)."""

    APP_LABEL = (AppiumBy.ID, f"{APP_PACKAGE}:id/app_label")
    APP_ICON = (AppiumBy.ID, f"{APP_PACKAGE}:id/app_icon")
    HEADER_TITLE = (AppiumBy.ID, f"{APP_PACKAGE}:id/suw_layout_title")
    FINISH_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/suw_navbar_next")

    def get_app_label(self) -> str:
        """Read app label on finished screen."""
        return self.get_text(self.APP_LABEL)

    def tap_finish(self) -> None:
        """Click bottom finish button."""
        self.tap(self.FINISH_BUTTON)

    def is_app_icon_displayed(self) -> bool:
        """Check if badged app icon is visible."""
        return self.is_displayed(self.APP_ICON)
