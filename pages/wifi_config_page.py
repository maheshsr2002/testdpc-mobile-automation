from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class WifiConfigPage(BasePage):
    """Page Object for Wi-Fi Configuration Dialog (wifi_config_dialog.xml)."""

    SSID_INPUT = (AppiumBy.ID, f"{APP_PACKAGE}:id/ssid")
    SECURITY_SPINNER = (AppiumBy.ID, f"{APP_PACKAGE}:id/security")
    PASSWORD_LAYOUT = (AppiumBy.ID, f"{APP_PACKAGE}:id/password_layout")
    PASSWORD_INPUT = (AppiumBy.ID, f"{APP_PACKAGE}:id/password")

    def enter_ssid(self, ssid: str) -> None:
        """Enter Wi-Fi network SSID."""
        self.type_text(self.SSID_INPUT, ssid)

    def get_ssid(self) -> str:
        """Get entered SSID."""
        return self.get_text(self.SSID_INPUT)

    def enter_password(self, password: str) -> None:
        """Enter Wi-Fi password."""
        self.type_text(self.PASSWORD_INPUT, password)

    def is_password_visible(self) -> bool:
        """Check whether password input field is currently visible."""
        return self.is_displayed(self.PASSWORD_LAYOUT)

    def tap_security_dropdown(self) -> None:
        """Open the security selection spinner."""
        self.tap(self.SECURITY_SPINNER)
