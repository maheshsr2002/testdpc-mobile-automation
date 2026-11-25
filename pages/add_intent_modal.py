from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class AddIntentModal(BasePage):
    """Modal dialog for adding Intent and Intent Filters (add_intent_or_intent_filter.xml)."""

    INTENT_FILTER_TEXT = (AppiumBy.ID, f"{APP_PACKAGE}:id/tv_intent_filter")
    CLEAR_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/btn_clear")
    ADD_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/btn_add")

    def get_filter_text(self) -> str:
        """Retrieve current intent filter description."""
        return self.get_text(self.INTENT_FILTER_TEXT)

    def tap_clear(self) -> None:
        """Click clear button."""
        self.tap(self.CLEAR_BUTTON)

    def tap_add(self) -> None:
        """Click add button."""
        self.tap(self.ADD_BUTTON)
