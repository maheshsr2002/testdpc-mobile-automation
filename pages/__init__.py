"""Page Object Model (POM) layer containing page locators, modals, and atomic interactions."""
from .base_page import BasePage
from .setup_management_page import SetupManagementPage
from .add_account_page import AddAccountPage
from .wifi_config_page import WifiConfigPage
from .permission_policy_page import PermissionPolicyPage
from .system_update_policy_page import SystemUpdatePolicyPage
from .manage_apps_page import ManageAppsPage
from .wipe_data_dialog import WipeDataDialog
from .policy_dashboard_page import PolicyDashboardPage

# Modal Dialogs
from .certificate_alias_modal import CertificateAliasModal
from .certificate_password_modal import CertificatePasswordModal
from .wifi_modification_modal import WifiModificationModal
from .add_intent_modal import AddIntentModal
from .edit_restriction_modal import EditRestrictionModal

# Screens
from .delegated_cert_page import DelegatedCertPage
from .network_usage_stats_page import NetworkUsageStatsPage
from .media_display_page import MediaDisplayPage
from .cross_profile_intent_page import CrossProfileIntentPage
from .cosu_kiosk_page import CosuKioskPage
from .finish_provisioning_page import FinishProvisioningPage

__all__ = [
    "BasePage",
    "SetupManagementPage",
    "AddAccountPage",
    "WifiConfigPage",
    "PermissionPolicyPage",
    "SystemUpdatePolicyPage",
    "ManageAppsPage",
    "WipeDataDialog",
    "PolicyDashboardPage",
    # Modals
    "CertificateAliasModal",
    "CertificatePasswordModal",
    "WifiModificationModal",
    "AddIntentModal",
    "EditRestrictionModal",
    # Screens
    "DelegatedCertPage",
    "NetworkUsageStatsPage",
    "MediaDisplayPage",
    "CrossProfileIntentPage",
    "CosuKioskPage",
    "FinishProvisioningPage",
]
