from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """Base Page Object containing reusable Appium UI interactions and explicit waits."""

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout

    def wait_for_visible(self, locator: tuple):
        """Wait until an element is visible on screen."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator: tuple):
        """Wait until an element is clickable."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def tap(self, locator: tuple) -> None:
        """Tap on an element after ensuring it is clickable."""
        element = self.wait_for_clickable(locator)
        element.click()

    def type_text(self, locator: tuple, text: str) -> None:
        """Clear existing text and type new text into an input field."""
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Retrieve the visible text of an element."""
        return self.wait_for_visible(locator).text

    def is_displayed(self, locator: tuple) -> bool:
        """Check if an element is currently displayed without throwing TimeoutException."""
        try:
            elements = self.driver.find_elements(*locator)
            return len(elements) > 0 and elements[0].is_displayed()
        except Exception:
            return False

    def is_selected(self, locator: tuple) -> bool:
        """Check if a checkbox or radio button is currently checked/selected."""
        try:
            if not self.is_displayed(locator):
                return False
            elements = self.driver.find_elements(*locator)
            if not elements:
                return False
            el = elements[0]
            return el.is_selected() or el.get_attribute("checked") == "true"
        except Exception:
            return False
