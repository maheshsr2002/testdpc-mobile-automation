from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class NetworkUsageStatsPage(BasePage):
    """Page Object for Network Usage Statistics screen (network_usage_stats.xml)."""

    QUERY_SPINNER = (AppiumBy.ID, f"{APP_PACKAGE}:id/query_type_spinner")
    START_DATE_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/start_date_button")
    END_DATE_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/end_date_button")
    SUMMARY_TEXT = (AppiumBy.ID, f"{APP_PACKAGE}:id/data_usage_summary")
    APP_HISTORY_LIST = (AppiumBy.ID, f"{APP_PACKAGE}:id/app_history")
    BACK_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/back_to_apps_button")

    def select_query_type(self) -> None:
        """Open network query type spinner."""
        self.tap(self.QUERY_SPINNER)

    def tap_start_date(self) -> None:
        """Click start date picker button."""
        self.tap(self.START_DATE_BUTTON)

    def tap_end_date(self) -> None:
        """Click end date picker button."""
        self.tap(self.END_DATE_BUTTON)

    def get_summary_text(self) -> str:
        """Read data usage summary."""
        return self.get_text(self.SUMMARY_TEXT)

    def tap_back_to_apps(self) -> None:
        """Click back to apps button."""
        self.tap(self.BACK_BUTTON)
