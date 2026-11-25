from pages.network_usage_stats_page import NetworkUsageStatsPage


class NetworkStatsSteps:
    """Step definitions for Network Usage Statistics workflows."""

    def __init__(self, driver):
        self.stats_page = NetworkUsageStatsPage(driver)

    def inspect_network_stats(self) -> dict:
        """Capture network usage screen details."""
        return {
            "current_package": self.stats_page.driver.current_package,
            "summary": self.stats_page.get_summary_text(),
        }

    def return_to_apps_list(self) -> None:
        """Navigate back to applications list."""
        self.stats_page.tap_back_to_apps()
