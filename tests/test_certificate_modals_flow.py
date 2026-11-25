import pytest
from data.setup_data import CERTIFICATE_DATA
from steps.certificate_steps import CertificateSteps


@pytest.mark.regression
def test_certificate_alias_modal_input(driver):
    """Verify entering alias in the Certificate Alias Prompt modal."""
    steps = CertificateSteps(driver)
    steps.set_certificate_alias(CERTIFICATE_DATA["sample_alias"])
    assert steps.alias_modal.get_alias() == CERTIFICATE_DATA["sample_alias"]


@pytest.mark.regression
def test_certificate_password_modal_input(driver):
    """Verify entering password in Certificate Password Prompt modal."""
    steps = CertificateSteps(driver)
    steps.provide_certificate_password(CERTIFICATE_DATA["sample_password"])
    # Verify input was accepted
    assert steps.password_modal.get_text(steps.password_modal.PASSWORD_INPUT) is not None
