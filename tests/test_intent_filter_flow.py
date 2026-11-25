import pytest
from steps.intent_steps import IntentSteps


@pytest.mark.regression
def test_intent_filter_modal_interactions(driver):
    """Verify interaction with Add Intent Filter modal (add_intent_or_intent_filter.xml)."""
    steps = IntentSteps(driver)
    steps.clear_intent_filter()
    steps.add_intent_filter()
