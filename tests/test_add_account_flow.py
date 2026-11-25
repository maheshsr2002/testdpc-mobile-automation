import pytest
from data.setup_data import SETUP_MANAGEMENT_DATA, ADD_ACCOUNT_DATA
from steps.setup_steps import SetupSteps
from steps.account_steps import AccountSteps


@pytest.mark.smoke
def test_setup_flow_transitions_to_add_account(driver):
    """Verify that completing initial setup advances to the Add Account screen."""
    setup_steps = SetupSteps(driver)
    setup_steps.choose_managed_profile_and_continue()

    account_steps = AccountSteps(driver)
    state = account_steps.read_account_screen_state()

    assert state["current_package"] == SETUP_MANAGEMENT_DATA["expected_package"]
    assert state["is_skip_selected"] is not None


@pytest.mark.regression
def test_select_add_account_options(driver):
    """Verify selecting between skip and add account options."""
    setup_steps = SetupSteps(driver)
    setup_steps.choose_managed_profile_and_continue()

    account_steps = AccountSteps(driver)
    account_steps.choose_add_account()
    state = account_steps.read_account_screen_state()
    assert state["is_add_account_selected"] is True
