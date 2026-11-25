import pytest
from pages.wifi_modification_modal import WifiModificationModal


@pytest.mark.regression
def test_wifi_modification_modal_actions(driver):
    """Verify Wi-Fi modification modal controls (wifi_config_modification.xml)."""
    modal = WifiModificationModal(driver)
    modal.tap_update()
    modal.tap_remove()
