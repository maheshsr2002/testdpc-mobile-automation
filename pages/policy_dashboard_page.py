import time
from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class PolicyDashboardPage(BasePage):
    """Page Object for the main enterprise Policy Management dashboard list view."""

    ACTION_BAR_TITLE = (AppiumBy.XPATH, "//*[@text='Policy management']")
    DEVICE_OWNER_SUMMARY = (AppiumBy.XPATH, "//*[@text='This app is the device owner.']")
    POLICY_LIST = (AppiumBy.ID, "android:id/list")

    def is_dashboard_displayed(self) -> bool:
        """Check if Policy management dashboard is displayed."""
        return self.is_displayed(self.ACTION_BAR_TITLE)

    def scroll_and_click_item(self, item_title: str) -> None:
        """Smoothly scroll the list view until item_title is visible and click it."""
        time.sleep(1)
        selector = (
            f'new UiScrollable(new UiSelector().resourceId("android:id/list"))'
            f'.scrollIntoView(new UiSelector().text("{item_title}"))'
        )
        element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
        time.sleep(1)
        element.click()
        time.sleep(1)

    def open_wipe_data_dialog(self) -> None:
        """Navigate to and open the Wipe data dialog."""
        self.scroll_and_click_item("Wipe data")

    def open_system_update_policy(self) -> None:
        """Navigate to and open the Manage system update policy dialog."""
        self.scroll_and_click_item("Manage system update policy")

    def open_permission_policy(self) -> None:
        """Navigate to and open Get/Set default permission policy dialog."""
        self.scroll_and_click_item("Get/Set default permission policy")

    def open_certificate_alias_modal(self) -> None:
        """Navigate to and open Override client certificates with alias modal."""
        self.scroll_and_click_item("Override client certificates with alias")

    def open_wifi_management(self) -> None:
        """Navigate to and open the Wifi management section."""
        self.scroll_and_click_item("Wifi management")

    def open_delegated_cert_installer(self) -> None:
        """Navigate to and open Manage delegated certificate installer."""
        self.scroll_and_click_item("Manage delegated certificate installer")

    def open_network_stats(self) -> None:
        """Navigate to Network Data Usage Stats."""
        self.scroll_and_click_item("Network Data Usage Stats")

    def open_app_restrictions(self) -> None:
        """Navigate to Manage app restrictions."""
        self.scroll_and_click_item("Manage app restrictions")
