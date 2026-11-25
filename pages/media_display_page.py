from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class MediaDisplayPage(BasePage):
    """Page Object for Media Display screen (fragment_media_display.xml)."""

    IMAGE_VIEW = (AppiumBy.ID, f"{APP_PACKAGE}:id/image")
    VIDEO_VIEW = (AppiumBy.ID, f"{APP_PACKAGE}:id/video")
    PLAY_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/play_button")
    STOP_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/stop_button")
    DELETE_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/delete_button")

    def tap_play(self) -> None:
        """Click Play media button."""
        self.tap(self.PLAY_BUTTON)

    def tap_stop(self) -> None:
        """Click Stop media button."""
        self.tap(self.STOP_BUTTON)

    def tap_delete(self) -> None:
        """Click Delete media button."""
        self.tap(self.DELETE_BUTTON)

    def is_image_displayed(self) -> bool:
        """Check if image view is visible."""
        return self.is_displayed(self.IMAGE_VIEW)
