from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class ManageAppsPage(BasePage):
    """Page Object for Application Management screen (manage_apps.xml)."""

    HEADER_TEXT = (AppiumBy.ID, f"{APP_PACKAGE}:id/header_text")
    APPS_SPINNER = (AppiumBy.ID, f"{APP_PACKAGE}:id/managed_apps_list")
    ADD_ROW_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/add_new_row")
    APP_LIST_VIEW = (AppiumBy.ID, f"{APP_PACKAGE}:id/app_list_view")
    LOAD_DEFAULT_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/load_default_button")
    RESET_APP_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/reset_app")
    SAVE_APP_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/save_app")

    def select_app_from_dropdown(self) -> None:
        """Open the managed apps list spinner."""
        self.tap(self.APPS_SPINNER)

    def tap_load_manifest_restrictions(self) -> None:
        """Click 'Load Manifest Restrictions' button."""
        self.tap(self.LOAD_DEFAULT_BUTTON)

    def tap_add_new_row(self) -> None:
        """Click '+' to add restriction row."""
        self.tap(self.ADD_ROW_BUTTON)

    def tap_save_app(self) -> None:
        """Click Save app restrictions button."""
        self.tap(self.SAVE_APP_BUTTON)

    def tap_reset_app(self) -> None:
        """Click Reset app restrictions button."""
        self.tap(self.RESET_APP_BUTTON)
