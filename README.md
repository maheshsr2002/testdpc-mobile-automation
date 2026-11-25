# TestDPC Mobile Test Automation Framework

An enterprise-grade, 5-layer mobile automation testing framework for **TestDPC 2.0.4** built with **Python**, **Appium**, **UiAutomator2**, and **pytest**.

---

## 1. Where Test Data is Fetched From

The framework separates test data and configurations into distinct, traceable sources:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          TEST DATA SOURCES                                  │
├───────────────────────────────┬─────────────────────────────────────────────┤
│ Source File                   │ Purpose & Data Fetched                      │
├───────────────────────────────┼─────────────────────────────────────────────┤
│ 1. data/setup_data.py         │ • Static Expected Strings & Test Inputs     │
│                               │   - Expected headers, labels, and copy      │
│                               │   - Radio option strings                    │
│                               │   - Test Wi-Fi SSIDs & credentials          │
│                               │   - Certificate aliases & passwords         │
│                               │   - Policy names and update options         │
├───────────────────────────────┼─────────────────────────────────────────────┤
│ 2. .env                       │ • Dynamic Environment Variables             │
│    (created from .env.example,│   - APPIUM_SERVER_URL (default: 127.0.0.1:4723)
│     read by config/settings.py)│   - PLATFORM_NAME (Android)                 │
│                               │   - AUTOMATION_NAME (UiAutomator2)          │
│                               │   - DEVICE_NAME (Android Emulator)          │
│                               │   - APP_PACKAGE (com.sample.android.testdpc)│
│                               │   - APP_ACTIVITY (.LaunchActivity)          │
│                               │   - APK_PATH (apps/testdpc.apk)             │
│                               │   - DEFAULT_TIMEOUT (15s)                   │
├───────────────────────────────┼─────────────────────────────────────────────┤
│ 3. APK Extraction Baseline    │ • Extracted APK Baseline Data (Reference)   │
│    (local reference used to   │   - Full mapping of Hex IDs to names/values │
│     generate data/setup_data) │   - Complete dump of all APK strings        │
│                               │   - AndroidManifest activities & permissions│
├───────────────────────────────┼─────────────────────────────────────────────┤
│ 4. Live Android Device /      │ • Runtime State Captured by Appium          │
│    Emulator (at test runtime) │   - driver.current_package                  │
│                               │   - driver.current_activity                 │
│                               │   - element.text via get_text()             │
│                               │   - element.is_selected() / checked state   │
└───────────────────────────────┴─────────────────────────────────────────────┘
```

---

## 2. Framework Architecture (5-Layer Design)

The project follows the Page Object Model (POM) and Separation of Concerns:

```text
MOBILE AUTOMATION/
├── apps/
│   └── testdpc.apk                  # Target Android APK under test
├── config/
│   ├── __init__.py                  # Exposes configuration constants
│   └── settings.py                  # Reads .env, sets paths, timeouts & capabilities
├── data/
│   ├── __init__.py                  # Exposes test data dictionaries
│   └── setup_data.py                # Expected UI text, test inputs, credentials
├── pages/
│   ├── __init__.py                  # Exports all Page Objects and Modals
│   ├── base_page.py                 # Core Appium interaction wrapper (waits, clicks, taps)
│   │
│   ├── # --- MODAL DIALOGS ---
│   ├── certificate_alias_modal.py   # Modal: Certificate alias prompt
│   ├── certificate_password_modal.py# Modal: Certificate password prompt
│   ├── wifi_config_page.py          # Modal: Wi-Fi network configuration dialog
│   ├── wifi_modification_modal.py   # Modal: Wi-Fi update/removal dialog
│   ├── wipe_data_dialog.py          # Modal: Factory reset & protection options
│   ├── add_intent_modal.py          # Modal: Add intent and filter dialog
│   ├── edit_restriction_modal.py    # Modal: App restrictions editor dialog
│   │
│   └── # --- SCREENS & ACTIVITIES ---
│       ├── setup_management_page.py # Setup management fragment
│       ├── add_account_page.py      # Add account activity
│       ├── permission_policy_page.py# Permission policy options
│       ├── system_update_policy_page.py # System update policy options
│       ├── manage_apps_page.py      # Enterprise application restrictions
│       ├── delegated_cert_page.py   # Delegated certificate installers
│       ├── network_usage_stats_page.py # Network data usage statistics
│       ├── media_display_page.py    # Media playback and controls
│       ├── cross_profile_intent_page.py # Cross-profile intent direction
│       ├── cosu_kiosk_page.py       # COSU / Kiosk provisioning
│       └── finish_provisioning_page.py # Setup completion screen
├── steps/
│   ├── __init__.py                  # Exports all Step choreography classes
│   ├── setup_steps.py               # Setup wizard choreography
│   ├── account_steps.py             # Account setup & skip steps
│   ├── wifi_steps.py                # Wi-Fi entry & config steps
│   ├── policy_steps.py              # Permission & update policy steps
│   ├── app_management_steps.py      # App restrictions & wipe dialog steps
│   ├── certificate_steps.py         # Cert alias, password & delegated installer steps
│   ├── network_stats_steps.py       # Network usage stats queries & date filters
│   ├── media_steps.py               # Media playback, stop, and delete steps
│   └── intent_steps.py              # Add intent modal & cross-profile intent steps
├── tests/
│   ├── __init__.py
│   ├── conftest.py                  # Driver fixture + screenshot on failure
│   ├── test_setup_flow.py           # Setup screen scenarios (3 tests)
│   ├── test_add_account_flow.py     # Add account scenarios (2 tests)
│   ├── test_wifi_config_flow.py     # Wi-Fi dialog scenarios (1 test)
│   ├── test_wifi_modification_flow.py # Wi-Fi modification modal scenarios (1 test)
│   ├── test_certificate_modals_flow.py # Certificate alias & password modals (2 tests)
│   ├── test_intent_filter_flow.py   # Add Intent filter modal scenarios (1 test)
│   ├── test_manage_apps_flow.py     # App management & wipe data dialog (1 test)
│   ├── test_policies_flow.py        # Permission & update policy scenarios (2 tests)
│   ├── test_network_stats_flow.py   # Network stats query scenarios (1 test)
│   └── test_media_display_flow.py   # Media player controls scenarios (1 test)
├── reports/
│   └── screenshots/                 # Auto-saved PNG screenshots on test failure
├── _extracted_apk/                  # Decompiled APK layouts, manifests, and strings
├── .env                             # Local environment variables (gitignored)
├── .gitignore                       # Standard Python, test artifacts, and temp files
├── pytest.ini                       # Testpaths, markers, and execution options
└── requirements.txt                 # Python dependencies
```

---

## 3. Prerequisites

* **Python 3.10+** (Python 3.14 installed in `.venv`)
* **Node.js** (v24.x)
* **Appium Server & Driver**:
  ```powershell
  npm install -g appium
  appium driver install uiautomator2
  ```
* **Android SDK & Emulator**:
  - `ANDROID_HOME`: `C:\Users\Mahesh\AppData\Local\Android\Sdk`
  - Emulator AVD: `Medium_Phone_API_37.0` (or any configured AVD)

---

## 4. Setup & Installation

1. **Activate Virtual Environment**:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

2. **Install Dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

---

## 5. Running the Tests

### Step 1: Boot your Android Emulator
In Android Studio, launch **Device Manager** and start `Medium_Phone_API_37.0` (or launch via terminal):
```powershell
emulator -avd Medium_Phone_API_37.0
```
Verify the device is online:
```powershell
adb devices
```

### Step 2: Start Appium Server
In a separate terminal tab:
```powershell
appium
```

### Step 3: Run Tests

* **Run Smoke Tests**:
  ```powershell
  .\.venv\Scripts\pytest.exe -m smoke
  ```

* **Run Full Regression Suite (All 15 Tests)**:
  ```powershell
  .\.venv\Scripts\pytest.exe
  ```

* **Run a Specific Test Module**:
  ```powershell
  .\.venv\Scripts\pytest.exe tests/test_setup_flow.py
  ```

* **Generate HTML / Detailed Report**:
  ```powershell
  .\.venv\Scripts\pytest.exe -v --tb=short
  ```

---

## 6. Failure Screenshots

When any test fails, the custom `pytest_runtest_makereport` hook in [`tests/conftest.py`](file:///d:/mobile%20automation%20test%20dpc%202.0.4/tests/conftest.py) automatically captures a full-screen screenshot and saves it to:
```
reports/screenshots/<test_name>.png
```
