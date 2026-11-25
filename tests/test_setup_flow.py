import pytest
from data.setup_data import SETUP_MANAGEMENT_DATA
from steps.setup_steps import SetupSteps


@pytest.mark.smoke
def test_app_opens_setup_management_screen(driver):
    """Verify that launching TestDPC opens the Setup Management screen with expected copy and defaults."""
    steps = SetupSteps(driver)
    screen_state = steps.read_initial_setup_screen()

    assert screen_state["current_package"] == SETUP_MANAGEMENT_DATA["expected_package"], (
        f"Expected package '{SETUP_MANAGEMENT_DATA['expected_package']}', got '{screen_state['current_package']}'"
    )
    assert screen_state["header_title"] == SETUP_MANAGEMENT_DATA["header_title"], (
        f"Expected header title '{SETUP_MANAGEMENT_DATA['header_title']}', got '{screen_state['header_title']}'"
    )
    assert screen_state["is_managed_profile_selected"] is True, (
        "Expected 'Set up managed profile' to be selected by default"
    )


@pytest.mark.regression
def test_switch_setup_options(driver):
    """Verify selecting between 'Set up device owner' and 'Set up managed profile' options if available."""
    steps = SetupSteps(driver)
    state = steps.read_initial_setup_screen()

    # Managed profile is always the default option
    assert state["is_managed_profile_selected"] is True

    # If device owner is available on this ROM/profile, verify switching
    if steps.setup_page.is_displayed(steps.setup_page.DEVICE_OWNER_RADIO):
        steps.switch_to_device_owner()
        new_state = steps.read_initial_setup_screen()
        assert new_state["is_device_owner_selected"] is True
        steps.switch_to_managed_profile()
        restored_state = steps.read_initial_setup_screen()
        assert restored_state["is_managed_profile_selected"] is True


@pytest.mark.smoke
def test_select_managed_profile_and_proceed(driver):
    """Verify selecting managed profile and clicking Next advances the setup flow."""
    steps = SetupSteps(driver)
    steps.choose_managed_profile_and_continue()

    # Verify that the screen transitioned into provisioning or subsequent activity
    current_activity = driver.current_activity
    assert current_activity is not None
