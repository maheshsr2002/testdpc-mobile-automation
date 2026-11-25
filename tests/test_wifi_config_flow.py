import pytest
from data.setup_data import WIFI_CONFIG_DATA
from steps.wifi_steps import WifiSteps


@pytest.mark.regression
def test_wifi_config_input(driver):
    """Verify entering Wi-Fi SSID and configuration in Wi-Fi dialog."""
    wifi_steps = WifiSteps(driver)
    wifi_steps.configure_wifi_network(
        ssid=WIFI_CONFIG_DATA["test_ssid"],
        password=WIFI_CONFIG_DATA["test_password"]
    )

    entered_ssid = wifi_steps.read_entered_ssid()
    assert entered_ssid == WIFI_CONFIG_DATA["test_ssid"]
