from pages.policy_dashboard_page import PolicyDashboardPage
from pages.manage_apps_page import ManageAppsPage
from pages.wipe_data_dialog import WipeDataDialog


class AppManagementSteps:
    """Step definitions for app management and wipe data workflows."""

    def __init__(self, driver):
        self.dashboard = PolicyDashboardPage(driver)
        self.apps_page = ManageAppsPage(driver)
        self.wipe_dialog = WipeDataDialog(driver)

    def load_manifest_restrictions(self) -> None:
        """Load manifest restrictions for the selected application."""
        self.dashboard.open_app_restrictions()
        self.apps_page.tap_load_manifest_restrictions()

    def save_app_restrictions(self) -> None:
        """Save application restrictions."""
        self.apps_page.tap_save_app()

    def reset_app_restrictions(self) -> None:
        """Reset application restrictions to baseline."""
        self.apps_page.tap_reset_app()

    def open_and_toggle_wipe_dialog(self, external_storage: bool = False, reset_protection: bool = False) -> dict:
        """Navigate from policy dashboard, open Wipe Data dialog, toggle options, and dismiss."""
        self.dashboard.open_wipe_data_dialog()
        if external_storage != self.wipe_dialog.is_external_storage_checked():
            self.wipe_dialog.toggle_external_storage()
        if reset_protection != self.wipe_dialog.is_reset_protection_checked():
            self.wipe_dialog.toggle_reset_protection()

        result = {
            "external_storage": self.wipe_dialog.is_external_storage_checked(),
            "reset_protection": self.wipe_dialog.is_reset_protection_checked(),
        }
        self.wipe_dialog.tap_cancel()
        return result
