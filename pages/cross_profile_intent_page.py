from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class CrossProfileIntentPage(BasePage):
    """Page Object for Cross Profile Intents (cross_profile_intent.xml)."""

    DIRECTION_SPINNER = (AppiumBy.ID, f"{APP_PACKAGE}:id/cross_profile_intent_direction")
    FLAGS_TEXT = (AppiumBy.ID, f"{APP_PACKAGE}:id/cross_profile_intent_filters_flags")

    def tap_direction_dropdown(self) -> None:
        """Open cross-profile direction spinner."""
        self.tap(self.DIRECTION_SPINNER)

    def get_flags_text(self) -> str:
        """Read intent filter flags text."""
        return self.get_text(self.FLAGS_TEXT)
