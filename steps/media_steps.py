from pages.media_display_page import MediaDisplayPage


class MediaSteps:
    """Step definitions for Media playback controls."""

    def __init__(self, driver):
        self.media_page = MediaDisplayPage(driver)

    def play_media_content(self) -> None:
        """Trigger media playback."""
        self.media_page.tap_play()

    def stop_media_content(self) -> None:
        """Stop media playback."""
        self.media_page.tap_stop()

    def delete_media_content(self) -> None:
        """Delete media item."""
        self.media_page.tap_delete()
