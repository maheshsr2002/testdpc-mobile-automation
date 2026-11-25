from pages.add_intent_modal import AddIntentModal
from pages.cross_profile_intent_page import CrossProfileIntentPage


class IntentSteps:
    """Step definitions for Intent and Filter management."""

    def __init__(self, driver):
        self.add_intent_modal = AddIntentModal(driver)
        self.cross_profile_page = CrossProfileIntentPage(driver)

    def add_intent_filter(self) -> None:
        """Click Add in the intent filter dialog."""
        self.add_intent_modal.tap_add()

    def clear_intent_filter(self) -> None:
        """Click Clear in the intent filter dialog."""
        self.add_intent_modal.tap_clear()
