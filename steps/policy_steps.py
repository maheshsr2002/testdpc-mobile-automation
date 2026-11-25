from pages.policy_dashboard_page import PolicyDashboardPage
from pages.permission_policy_page import PermissionPolicyPage
from pages.system_update_policy_page import SystemUpdatePolicyPage


class PolicySteps:
    """Step definitions for enterprise policy configuration workflows."""

    def __init__(self, driver):
        self.dashboard = PolicyDashboardPage(driver)
        self.permission_page = PermissionPolicyPage(driver)
        self.system_update_page = SystemUpdatePolicyPage(driver)

    def set_permission_policy(self, policy: str) -> None:
        """Navigate to and configure runtime permission policy ('prompt', 'auto_accept', 'auto_deny')."""
        self.dashboard.open_permission_policy()
        if policy == "auto_accept":
            self.permission_page.select_auto_accept()
        elif policy == "auto_deny":
            self.permission_page.select_auto_deny()
        else:
            self.permission_page.select_prompt()

    def set_system_update_policy(self, policy_type: str) -> None:
        """Navigate to and configure system update policy ('automatic', 'windowed', 'postpone', 'none')."""
        self.dashboard.open_system_update_policy()
        if policy_type == "automatic":
            self.system_update_page.select_automatic()
        elif policy_type == "windowed":
            self.system_update_page.select_windowed()
        elif policy_type == "postpone":
            self.system_update_page.select_postpone()
        else:
            self.system_update_page.select_none()
