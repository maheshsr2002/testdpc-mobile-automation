import pytest
from steps.app_management_steps import AppManagementSteps


@pytest.mark.regression
def test_wipe_data_dialog_toggles(driver):
    """Verify navigating from policy dashboard to Wipe Data dialog and toggling checkboxes."""
    app_steps = AppManagementSteps(driver)

    result = app_steps.open_and_toggle_wipe_dialog(external_storage=True, reset_protection=True)
    assert result["external_storage"] is True
    assert result["reset_protection"] is True
