from pages.certificate_alias_modal import CertificateAliasModal
from pages.certificate_password_modal import CertificatePasswordModal
from pages.delegated_cert_page import DelegatedCertPage


class CertificateSteps:
    """Step definitions for Certificate management and modal prompts."""

    def __init__(self, driver):
        self.alias_modal = CertificateAliasModal(driver)
        self.password_modal = CertificatePasswordModal(driver)
        self.delegated_page = DelegatedCertPage(driver)

    def set_certificate_alias(self, alias: str) -> None:
        """Provide alias in the alias prompt modal."""
        self.alias_modal.enter_alias(alias)

    def provide_certificate_password(self, password: str) -> None:
        """Provide password in the password prompt modal."""
        self.password_modal.enter_password(password)

    def assign_delegated_cert_installer(self, pkg_name: str) -> None:
        """Assign delegated cert installer package."""
        self.delegated_page.enter_new_installer(pkg_name)
        self.delegated_page.tap_set()

    def clear_delegated_cert_installer(self) -> None:
        """Clear delegated cert installer package."""
        self.delegated_page.tap_clear()
