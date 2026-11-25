from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class CertificatePasswordModal(BasePage):
    """Modal dialog for prompting Certificate Password (certificate_password_prompt.xml)."""

    PASSWORD_INPUT = (AppiumBy.ID, f"{APP_PACKAGE}:id/password_input")
    INCORRECT_PASSWORD_TEXT = (AppiumBy.ID, f"{APP_PACKAGE}:id/incorrect_password")

    def enter_password(self, password: str) -> None:
        """Enter certificate password."""
        self.type_text(self.PASSWORD_INPUT, password)

    def is_incorrect_password_displayed(self) -> bool:
        """Check whether incorrect password warning is displayed."""
        return self.is_displayed(self.INCORRECT_PASSWORD_TEXT)
