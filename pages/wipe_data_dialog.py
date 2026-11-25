from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class WipeDataDialog(BasePage):
    """Page Object for Wipe Data confirmation prompt (wipe_data_dialog_prompt.xml)."""

    EXTERNAL_STORAGE_CHECKBOX = (AppiumBy.ID, f"{APP_PACKAGE}:id/external_storage_checkbox")
    RESET_PROTECTION_CHECKBOX = (AppiumBy.ID, f"{APP_PACKAGE}:id/reset_protection_checkbox")
    CANCEL_BUTTON = (AppiumBy.ID, "android:id/button2")
    WIPE_BUTTON = (AppiumBy.ID, "android:id/button1")

    def toggle_external_storage(self) -> None:
        """Toggle wipe external storage option."""
        self.tap(self.EXTERNAL_STORAGE_CHECKBOX)

    def toggle_reset_protection(self) -> None:
        """Toggle wipe factory reset protection data option."""
        self.tap(self.RESET_PROTECTION_CHECKBOX)

    def is_external_storage_checked(self) -> bool:
        """Check if external storage checkbox is enabled."""
        return self.is_selected(self.EXTERNAL_STORAGE_CHECKBOX)

    def is_reset_protection_checked(self) -> bool:
        """Check if reset protection checkbox is enabled."""
        return self.is_selected(self.RESET_PROTECTION_CHECKBOX)

    def tap_cancel(self) -> None:
        """Dismiss wipe dialog by clicking Cancel button."""
        self.tap(self.CANCEL_BUTTON)

    def tap_wipe(self) -> None:
        """Confirm wipe data by clicking Wipe button."""
        self.tap(self.WIPE_BUTTON)
