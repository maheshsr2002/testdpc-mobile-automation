from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class CosuKioskPage(BasePage):
    """Page Object for COSU / Kiosk Mode activity (enable_cosu_activity.xml)."""

    STATUS_TEXT = (AppiumBy.ID, f"{APP_PACKAGE}:id/status_text")
    HEADER_TITLE = (AppiumBy.ID, f"{APP_PACKAGE}:id/suw_layout_title")

    def get_status_text(self) -> str:
        """Read current COSU provisioning status message."""
        return self.get_text(self.STATUS_TEXT)
