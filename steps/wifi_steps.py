from pages.wifi_config_page import WifiConfigPage


class WifiSteps:
    """Step definitions for Wi-Fi Configuration Dialog workflows (wifi_config_dialog.xml)."""

    def __init__(self, driver):
        self.wifi_page = WifiConfigPage(driver)

    def configure_wifi_network(self, ssid: str, password: str = None) -> None:
        """Fill in Wi-Fi SSID and optional password."""
        self.wifi_page.enter_ssid(ssid)
        if password and self.wifi_page.is_password_visible():
            self.wifi_page.enter_password(password)

    def read_entered_ssid(self) -> str:
        """Read the currently entered SSID."""
        return self.wifi_page.get_ssid()
