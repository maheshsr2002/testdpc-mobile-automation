from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class WifiModificationModal(BasePage):
    """Modal dialog for Wi-Fi Configuration modification/removal (wifi_config_modification.xml)."""

    CONFIGS_LIST = (AppiumBy.ID, f"{APP_PACKAGE}:id/wifiConfigs")
    UPDATE_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/updateSelectedConfig")
    REMOVE_BUTTON = (AppiumBy.ID, f"{APP_PACKAGE}:id/removeSelectedConfig")

    def tap_update(self) -> None:
        """Tap 'Update' on selected Wi-Fi config."""
        self.tap(self.UPDATE_BUTTON)

    def tap_remove(self) -> None:
        """Tap 'Remove' on selected Wi-Fi config."""
        self.tap(self.REMOVE_BUTTON)

    def is_configs_list_displayed(self) -> bool:
        """Check whether Wi-Fi configurations list is displayed."""
        return self.is_displayed(self.CONFIGS_LIST)
