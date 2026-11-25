from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class EditRestrictionModal(BasePage):
    """Modal dialog for editing app restrictions (edit_restriction_layout.xml)."""

    TYPE_SPINNER = (AppiumBy.ID, f"{APP_PACKAGE}:id/type_spinner")
    RESTRICTION_KEY_INPUT = (AppiumBy.ID, f"{APP_PACKAGE}:id/restriction_key")
    VALUE_BOOL_SWITCH = (AppiumBy.ID, f"{APP_PACKAGE}:id/value_bool")
    VALUE_STR_INPUT = (AppiumBy.ID, f"{APP_PACKAGE}:id/value_int_str")

    def select_type(self) -> None:
        """Open type dropdown."""
        self.tap(self.TYPE_SPINNER)

    def enter_key(self, key: str) -> None:
        """Enter restriction key."""
        self.type_text(self.RESTRICTION_KEY_INPUT, key)

    def enter_string_value(self, value: str) -> None:
        """Enter string/integer value."""
        self.type_text(self.VALUE_STR_INPUT, value)

    def toggle_bool(self) -> None:
        """Toggle boolean switch."""
        self.tap(self.VALUE_BOOL_SWITCH)
