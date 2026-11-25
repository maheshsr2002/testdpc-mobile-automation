import pytest
from steps.media_steps import MediaSteps


@pytest.mark.regression
def test_media_playback_controls(driver):
    """Verify media display playback controls (fragment_media_display.xml)."""
    steps = MediaSteps(driver)
    steps.play_media_content()
    steps.stop_media_content()
    steps.delete_media_content()
