import pytest
from steps.network_stats_steps import NetworkStatsSteps


@pytest.mark.regression
def test_network_stats_screen_interactions(driver):
    """Verify interacting with Network Usage Stats screen (network_usage_stats.xml)."""
    steps = NetworkStatsSteps(driver)
    steps.stats_page.tap_start_date()
    steps.stats_page.tap_end_date()
    steps.return_to_apps_list()
