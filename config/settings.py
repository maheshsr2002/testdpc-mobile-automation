import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = Path(__file__).resolve().parent.parent

APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
PLATFORM_NAME = os.getenv("PLATFORM_NAME", "Android")
AUTOMATION_NAME = os.getenv("AUTOMATION_NAME", "UiAutomator2")
DEVICE_NAME = os.getenv("DEVICE_NAME", "Android Emulator")
APP_PACKAGE = os.getenv("APP_PACKAGE", "com.sample.android.testdpc")
APP_ACTIVITY = os.getenv("APP_ACTIVITY", "com.sample.android.testdpc.LaunchActivity")
APP_WAIT_ACTIVITY = os.getenv("APP_WAIT_ACTIVITY", "com.sample.android.testdpc.PolicyManagementActivity,com.sample.android.testdpc.LaunchActivity")
APK_PATH = str((ROOT_DIR / os.getenv("APK_PATH", "apps/testdpc.apk")).resolve())
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "15"))
