from pathlib import Path
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.settings import (
    APPIUM_SERVER_URL,
    PLATFORM_NAME,
    AUTOMATION_NAME,
    DEVICE_NAME,
    APP_PACKAGE,
    APP_ACTIVITY,
    APP_WAIT_ACTIVITY,
    DEFAULT_TIMEOUT,
)


@pytest.fixture
def driver():
    """Appium Driver lifecycle fixture."""
    options = UiAutomator2Options()
    options.platform_name = PLATFORM_NAME
    options.automation_name = AUTOMATION_NAME
    options.device_name = DEVICE_NAME
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY
    options.app_wait_activity = APP_WAIT_ACTIVITY
    options.no_reset = True
    options.set_capability("appium:forceAppLaunch", True)
    options.set_capability("appium:appInstallArgs", ["--bypass-low-target-sdk-block"])

    drv = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    drv.implicitly_wait(DEFAULT_TIMEOUT)

    # Cleanly ensure TestDPC is active on its setup screen
    try:
        drv.terminate_app("com.google.android.apps.work.clouddpc")
        drv.activate_app(APP_PACKAGE)
    except Exception:
        pass

    yield drv

    try:
        drv.terminate_app("com.google.android.apps.work.clouddpc")
        drv.activate_app(APP_PACKAGE)
        drv.quit()
    except Exception:
        pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captures screenshot automatically upon test failure."""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        drv = item.funcargs.get("driver")
        if drv:
            try:
                screenshots_dir = Path("reports/screenshots")
                screenshots_dir.mkdir(parents=True, exist_ok=True)
                screenshot_file = screenshots_dir / f"{item.name}.png"
                drv.save_screenshot(str(screenshot_file))
            except Exception:
                pass
