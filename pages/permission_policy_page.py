from appium.webdriver.common.appiumby import AppiumBy
from config.settings import APP_PACKAGE
from pages.base_page import BasePage


class PermissionPolicyPage(BasePage):
    """Page Object for Permission Policy configuration (set_permission_policy.xml)."""

    POLICY_GROUP = (AppiumBy.ID, f"{APP_PACKAGE}:id/set_permission_group")
    PROMPT_RADIO = (AppiumBy.ID, f"{APP_PACKAGE}:id/prompt")
    AUTO_ACCEPT_RADIO = (AppiumBy.ID, f"{APP_PACKAGE}:id/accept")
    AUTO_DENY_RADIO = (AppiumBy.ID, f"{APP_PACKAGE}:id/deny")

    def select_prompt(self) -> None:
        """Select 'Prompt user' policy."""
        self.tap(self.PROMPT_RADIO)

    def select_auto_accept(self) -> None:
        """Select 'Auto accept' policy."""
        self.tap(self.AUTO_ACCEPT_RADIO)

    def select_auto_deny(self) -> None:
        """Select 'Auto deny' policy."""
        self.tap(self.AUTO_DENY_RADIO)

    def is_prompt_selected(self) -> bool:
        """Check if Prompt policy is selected."""
        return self.is_selected(self.PROMPT_RADIO)

    def is_auto_accept_selected(self) -> bool:
        """Check if Auto Accept policy is selected."""
        return self.is_selected(self.AUTO_ACCEPT_RADIO)

    def is_auto_deny_selected(self) -> bool:
        """Check if Auto Deny policy is selected."""
        return self.is_selected(self.AUTO_DENY_RADIO)
