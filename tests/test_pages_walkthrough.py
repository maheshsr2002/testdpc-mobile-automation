import time
import pytest
from pages.policy_dashboard_page import PolicyDashboardPage
from pages.wipe_data_dialog import WipeDataDialog
from pages.system_update_policy_page import SystemUpdatePolicyPage
from pages.permission_policy_page import PermissionPolicyPage
from pages.network_usage_stats_page import NetworkUsageStatsPage
from pages.delegated_cert_page import DelegatedCertPage
from pages.certificate_alias_modal import CertificateAliasModal


@pytest.mark.smoke
def test_walkthrough_all_pages(driver):
    """Walk through all key pages and modals live on the emulator screen."""
    dashboard = PolicyDashboardPage(driver)
    
    # 1. Verify Policy Dashboard
    print("\n[Page 1] Verifying Policy Management Dashboard...")
    assert dashboard.is_dashboard_displayed()
    time.sleep(2)

    # 2. Page/Modal: Wipe Data Dialog
    print("[Page 2] Opening Wipe Data Dialog modal...")
    dashboard.open_wipe_data_dialog()
    wipe_dialog = WipeDataDialog(driver)
    time.sleep(1.5)
    
    print("  -> Toggling External Storage checkbox")
    wipe_dialog.toggle_external_storage()
    time.sleep(1)
    print("  -> Toggling Reset Protection checkbox")
    wipe_dialog.toggle_reset_protection()
    time.sleep(2)
    print("  -> Dismissing Wipe Data dialog")
    wipe_dialog.tap_cancel()
    time.sleep(1.5)

    # 3. Page/Modal: System Update Policy
    print("[Page 3] Opening System Update Policy dialog...")
    dashboard.open_system_update_policy()
    system_update = SystemUpdatePolicyPage(driver)
    time.sleep(1.5)

    print("  -> Selecting Automatic update policy")
    system_update.select_automatic()
    time.sleep(1)
    print("  -> Selecting Windowed update policy")
    system_update.select_windowed()
    time.sleep(1)
    print("  -> Selecting Postpone update policy")
    system_update.select_postpone()
    time.sleep(2)
    print("  -> Dismissing System Update Policy dialog")
    driver.back()
    time.sleep(1.5)

    # 4. Page/Modal: Runtime Permission Policy
    print("[Page 4] Opening Runtime Permission Policy dialog...")
    dashboard.open_permission_policy()
    permission_page = PermissionPolicyPage(driver)
    time.sleep(1.5)

    print("  -> Selecting Auto Accept")
    permission_page.select_auto_accept()
    time.sleep(1)
    print("  -> Selecting Auto Deny")
    permission_page.select_auto_deny()
    time.sleep(1)
    print("  -> Selecting Prompt User")
    permission_page.select_prompt()
    time.sleep(2)
    print("  -> Dismissing Permission Policy dialog")
    driver.back()
    time.sleep(1.5)

    # 5. Page: Delegated Certificate Installer
    print("[Page 5] Opening Delegated Certificate Installer page...")
    dashboard.open_delegated_cert_installer()
    delegated_cert = DelegatedCertPage(driver)
    time.sleep(1.5)

    print("  -> Entering sample installer package name")
    delegated_cert.enter_new_installer("com.example.certinstaller")
    time.sleep(2.5)
    print("  -> Navigating back to Policy Dashboard")
    driver.back()
    time.sleep(1.5)

    # 6. Page: Network Data Usage Stats
    print("[Page 6] Opening Network Data Usage Stats page...")
    dashboard.open_network_stats()
    network_stats = NetworkUsageStatsPage(driver)
    time.sleep(2)

    print("  -> Returning back to Policy Dashboard")
    driver.back()
    time.sleep(2)

    # 7. Page/Modal: Certificate Alias Modal
    print("[Page 7] Opening Certificate Alias Prompt modal...")
    dashboard.open_certificate_alias_modal()
    cert_alias_modal = CertificateAliasModal(driver)
    time.sleep(1.5)

    print("  -> Entering certificate alias 'enterprise_vpn_key'")
    cert_alias_modal.enter_alias("enterprise_vpn_key")
    time.sleep(2)
    print("  -> Dismissing Certificate Alias modal")
    cert_alias_modal.tap_cancel()
    time.sleep(1.5)

    print("\nAll pages and modals successfully displayed and navigated on emulator!")
