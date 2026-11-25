from config.settings import APP_PACKAGE

SETUP_MANAGEMENT_DATA = {
    "expected_package": APP_PACKAGE,
    "header_title": "Setup Management",
    "managed_profile_option": "Set up managed profile",
    "device_owner_option": "Set up device owner",
    "setup_message": (
        "This app is currently not the owner of this device or profile. "
        "Please select an option below and click NEXT to set up appropriate management by this app."
    ),
    "next_button": "Next",
    "back_button": "Back",
}

ADD_ACCOUNT_DATA = {
    "header_title": "Setup finished successfully",
    "add_account_option": "Add account",
    "add_account_with_name_option": "Add account with name",
    "skip_option": "Skip",
}

WIFI_CONFIG_DATA = {
    "test_ssid": "Enterprise_Secure_WiFi",
    "test_password": "TestPassword123!",
}

POLICY_DATA = {
    "permission_policies": ["prompt", "auto_accept", "auto_deny"],
    "system_update_policies": ["automatic", "windowed", "postpone", "none"],
}

CERTIFICATE_DATA = {
    "sample_alias": "EnterpriseClientCert2026",
    "sample_password": "SecureCertPassword!99",
    "delegated_package": "com.example.certinstaller",
}

INTENT_FILTER_DATA = {
    "sample_action": "android.intent.action.VIEW",
    "sample_scheme": "https",
}

NETWORK_STATS_DATA = {
    "query_types": ["summary", "detailed", "historical"],
}
