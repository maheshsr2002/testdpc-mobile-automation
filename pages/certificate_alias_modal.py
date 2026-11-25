from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class CertificateAliasModal(BasePage):
    """Modal dialog for prompting Certificate Alias (certificate_alias_prompt.xml)."""

    CERTIFICATE_NAME = (AppiumBy.ID, f"{APP_PACKAGE}:id/certificate_alias_prompt_certificate_name")
    ALIAS_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    CANCEL_BUTTON = (AppiumBy.ID, "android:id/button2")
    OK_BUTTON = (AppiumBy.ID, "android:id/button1")

    def enter_alias(self, alias: str) -> None:
        """Enter certificate alias."""
        self.type_text(self.ALIAS_INPUT, alias)

    def get_alias(self) -> str:
        """Get entered alias text."""
        return self.get_text(self.ALIAS_INPUT)

    def tap_cancel(self) -> None:
        """Click Cancel on certificate alias modal."""
        self.tap(self.CANCEL_BUTTON)

    def tap_ok(self) -> None:
        """Click OK on certificate alias modal."""
        self.tap(self.OK_BUTTON)
