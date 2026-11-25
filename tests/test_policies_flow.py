import pytest
from steps.policy_steps import PolicySteps


@pytest.mark.regression
def test_set_permission_policy_options(driver):
    """Verify selecting runtime permission policy options."""
    policy_steps = PolicySteps(driver)

    policy_steps.set_permission_policy("auto_accept")
    assert policy_steps.permission_page.is_auto_accept_selected() is True

    policy_steps.set_permission_policy("auto_deny")
    assert policy_steps.permission_page.is_auto_deny_selected() is True


@pytest.mark.regression
def test_set_system_update_policy(driver):
    """Verify selecting system update policy modes."""
    policy_steps = PolicySteps(driver)

    policy_steps.set_system_update_policy("automatic")
    assert policy_steps.system_update_page.is_selected(
        policy_steps.system_update_page.AUTOMATIC_RADIO
    ) is True
