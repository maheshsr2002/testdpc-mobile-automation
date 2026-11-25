"""Configuration module for mobile test automation."""
from .settings import (
    ROOT_DIR,
    APPIUM_SERVER_URL,
    PLATFORM_NAME,
    AUTOMATION_NAME,
    DEVICE_NAME,
    APP_PACKAGE,
    APP_ACTIVITY,
    APK_PATH,
    DEFAULT_TIMEOUT,
)

__all__ = [
    "ROOT_DIR",
    "APPIUM_SERVER_URL",
    "PLATFORM_NAME",
    "AUTOMATION_NAME",
    "DEVICE_NAME",
    "APP_PACKAGE",
    "APP_ACTIVITY",
    "APK_PATH",
    "DEFAULT_TIMEOUT",
]
