from pages.add_account_page import AddAccountPage


class AccountSteps:
    """Step definitions for Add Account screen workflows (activity_add_account.xml)."""

    def __init__(self, driver):
        self.account_page = AddAccountPage(driver)

    def read_account_screen_state(self) -> dict:
        """Capture current Add Account screen state."""
        return {
            "current_package": self.account_page.driver.current_package,
            "header_title": self.account_page.get_header_title(),
            "is_skip_selected": self.account_page.is_skip_selected(),
            "is_add_account_selected": self.account_page.is_add_account_selected(),
        }

    def choose_skip_and_continue(self) -> None:
        """Select skip option and continue setup."""
        self.account_page.select_skip()
        self.account_page.tap_next()

    def choose_add_account(self) -> None:
        """Select add account option."""
        self.account_page.select_add_account()
