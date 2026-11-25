from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class DelegatedCertPage(BasePage):
    """Page Object for Delegated Certificate Installer management (delegated_cert_installer.xml)."""

    CURRENT_INSTALLER_TEXT = (AppiumBy.ID, f"{APP_PACKAGE}:id/delegated_cert_installer_current")
    APP_LIST = (AppiumBy.ID, f"{APP_PACKAGE}:id/delegated_cert_installer_app_list")
    NEW_INSTALLER_INPUT = (AppiumBy.ID, f"{APP_PACKAGE}:id/delegated_cert_installer_new")
    SET_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/delegated_cert_installer_set")
    CLEAR_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/delegated_cert_installer_clear")

    def enter_new_installer(self, pkg_name: str) -> None:
        """Enter package name for new delegated cert installer."""
        self.type_text(self.NEW_INSTALLER_INPUT, pkg_name)

    def tap_set(self) -> None:
        """Click 'Set' installer button."""
        self.tap(self.SET_BUTTON)

    def tap_clear(self) -> None:
        """Click 'Clear' installer button."""
        self.tap(self.CLEAR_BUTTON)

    def get_current_installer(self) -> str:
        """Read current installer text."""
        return self.get_text(self.CURRENT_INSTALLER_TEXT)
