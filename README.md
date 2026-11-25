# TestDPC Mobile Test Automation Framework

An enterprise-grade, 5-layer mobile automation testing framework for **TestDPC** (Android Enterprise Device Policy Controller) built with **Python**, **Appium**, **UiAutomator2**, and **pytest**.

---

## 1. Project Overview & Target App

* **Target Application**: [TestDPC](https://github.com/googlesamples/android-testdpc) (Package: `com.sample.android.testdpc`, Launcher Activity: `.LaunchActivity`)
* **Purpose**: Automate validation of Android Enterprise device management capabilities, policy enforcement, work profile provisioning, and device administration workflows.
* **Core Technology Stack**:
  * **Language**: Python 3.10+ (tested on Python 3.12 / 3.14)
  * **Mobile Automation**: Appium 2.x with `uiautomator2` driver
  * **Test Runner**: pytest 8.x / 9.x
  * **Architecture Pattern**: 5-Layer Page Object Model (POM) with Step Choreography
  * **CI/CD Pipeline**: GitHub Actions automated workflow

### Automation Scope
* **Setup & Provisioning**: Unprovisioned device setup wizard, Managed Profile vs. Device Owner selection.
* **Enterprise Policy Management**: Dynamic list navigation, Runtime Permission policies (Prompt / Auto Accept / Auto Deny), System Update maintenance policies (Automatic / Windowed / Postpone).
* **Device & App Management**: Factory Reset & Wipe Data dialog (external storage & protection flags), application restrictions, system apps management.
* **Security & Certificates**: Certificate alias override modal, delegated certificate installer package assignment.
* **Data & Usage Monitoring**: Network Data Usage statistics queries, date range filters.
* **Advanced Modes**: Kiosk / COSU (Corporate-Owned Single-Use) mode, cross-profile intent routing.

---

## 2. Prerequisites & Environment Setup

Ensure the following tools are installed on your workstation:

* **Python 3.10+**: With `pip` and virtual environment support.
* **Node.js**: v18.x or v20.x+ LTS.
* **Appium Server & UiAutomator2 Driver**:
  ```bash
  npm install -g appium
  appium driver install uiautomator2
  ```
* **Android SDK & Platform Tools**:
  * Set `ANDROID_HOME` in your environment (e.g. `%LOCALAPPDATA%\Android\Sdk` on Windows, or `$HOME/Library/Android/sdk` on macOS).
  * Ensure `platform-tools` (containing `adb`) is added to your system `PATH`.
* **Android Device or Emulator**:
  * Minimum Android API level: **API 21+** (Android 5.0 Lollipop).
  * Recommended: **API 31+** (Android 12+) Google APIs system image.

---

## 3. Project Structure

The framework strictly enforces separation of concerns across 5 architectural layers:

```text
mobile-automation-testdpc/
├── .github/
│   └── workflows/
│       └── ci.yml                   # Automated GitHub Actions CI/CD pipeline
├── apps/
│   └── testdpc.apk                  # Tracked target Android APK under test
├── config/
│   ├── __init__.py                  # Configuration exports
│   └── settings.py                  # Environment loader, timeouts, and Appium capabilities
├── data/
│   ├── __init__.py                  # Test data exports
│   └── setup_data.py                # Expected UI strings, policy types, and mock test inputs
├── pages/
│   ├── __init__.py                  # Exports all Page Objects and Modals
│   ├── base_page.py                 # Core driver wrapper (explicit waits, taps, inputs)
│   ├── policy_dashboard_page.py     # Main Policy Management ListView with UiScrollable
│   ├── setup_management_page.py     # Initial setup wizard screen
│   ├── wipe_data_dialog.py          # Wipe data confirmation modal
│   ├── system_update_policy_page.py # System update maintenance options
│   ├── permission_policy_page.py    # Runtime permission configuration dialog
│   ├── delegated_cert_page.py       # Delegated certificate installer screen
│   ├── network_usage_stats_page.py  # Network data usage statistics screen
│   ├── certificate_alias_modal.py   # Certificate alias override modal
│   ├── certificate_password_modal.py# Certificate password prompt modal
│   ├── wifi_config_page.py          # Wi-Fi configuration modal
│   ├── wifi_modification_modal.py   # Wi-Fi modification dialog
│   ├── manage_apps_page.py          # App restrictions and management
│   ├── edit_restriction_modal.py    # Application restriction editor modal
│   ├── media_display_page.py        # Media capture and playback controls
│   ├── cross_profile_intent_page.py # Cross-profile intent direction screen
│   ├── add_intent_modal.py          # Add intent filter modal
│   ├── cosu_kiosk_page.py           # Kiosk mode configuration screen
│   ├── add_account_page.py          # Add account provisioning screen
│   └── finish_provisioning_page.py  # Provisioning completion screen
├── steps/
│   ├── __init__.py                  # Step choreography exports
│   ├── setup_steps.py               # Setup wizard choreography
│   ├── policy_steps.py              # Permission and update policy workflows
│   ├── app_management_steps.py      # App restrictions and wipe data workflows
│   ├── certificate_steps.py         # Certificate overrides and installer steps
│   ├── network_stats_steps.py       # Network usage query workflows
│   ├── wifi_steps.py                # Wi-Fi entry workflows
│   ├── media_steps.py               # Media playback workflows
│   ├── intent_steps.py              # Cross-profile intent workflows
│   └── account_steps.py             # Provisioning account steps
├── tests/
│   ├── __init__.py
│   ├── conftest.py                  # Appium session fixture, app reset, failure screenshot hook
│   ├── test_setup_flow.py           # Unprovisioned setup wizard scenarios
│   ├── test_pages_walkthrough.py    # Multi-page live UI navigation walkthrough
│   ├── test_manage_apps_flow.py     # App management & wipe data scenarios
│   ├── test_policies_flow.py        # System update & permission policy scenarios
│   ├── test_certificate_modals_flow.py # Certificate modal scenarios
│   ├── test_network_stats_flow.py   # Network usage statistics scenarios
│   ├── test_wifi_config_flow.py     # Wi-Fi configuration scenarios
│   ├── test_wifi_modification_flow.py # Wi-Fi update scenarios
│   ├── test_media_display_flow.py   # Media player control scenarios
│   ├── test_intent_filter_flow.py   # Intent filter modal scenarios
│   └── test_add_account_flow.py     # Add account provisioning scenarios
├── reports/
│   └── screenshots/                 # Captured full-screen PNGs on test failures (gitignored)
├── .env.example                     # Environment template for collaborators & CI
├── .gitignore                       # Ignored secrets, local caches, logs, and build artifacts
├── pytest.ini                       # Test discovery paths, options, and markers
└── requirements.txt                 # Python project dependencies
```

---

## 4. Configuration & Environment Variables

The framework reads its configuration from a local `.env` file via `config/settings.py`.

### 1. Create your local `.env`:
Copy the provided template:

**On Windows PowerShell:**
```powershell
Copy-Item .env.example .env
```

**On macOS / Linux:**
```bash
cp .env.example .env
```

### 2. Supported Configuration Variables:

| Variable | Default Value | Description |
| :--- | :--- | :--- |
| `APPIUM_SERVER_URL` | `http://127.0.0.1:4723` | Appium 2.x server endpoint |
| `PLATFORM_NAME` | `Android` | Target mobile OS platform |
| `AUTOMATION_NAME` | `UiAutomator2` | Appium automation engine driver |
| `DEVICE_NAME` | `Android Emulator` | Connected device or emulator identifier |
| `APP_PACKAGE` | `com.sample.android.testdpc` | Target application package ID |
| `APP_ACTIVITY` | `com.sample.android.testdpc.LaunchActivity` | Main entry point activity |
| `APP_WAIT_ACTIVITY` | `com.sample.android.testdpc.PolicyManagementActivity,com.sample.android.testdpc.LaunchActivity` | Target activities to await upon app launch |
| `APK_PATH` | `apps/testdpc.apk` | Relative path to target APK file |
| `DEFAULT_TIMEOUT` | `15` | Explicit wait timeout in seconds |

> [!NOTE]
> `.gitignore` is configured to ignore extraneous binary builds (`*.apk`), while explicitly tracking `!apps/*.apk`. The official `apps/testdpc.apk` binary is committed to the repository so tests can run immediately without manual downloads.

---

## 5. Device State & Provisioning Notes

TestDPC operates in **two distinct lifecycle states**. Understanding these states is essential for running the correct test suites:

### Mode A: Unprovisioned Setup Mode
* **Active Screen**: `Setup Management` (`activity_setup_management.xml`)
* **When to Use**: To test initial onboarding wizards and profile creation (`tests/test_setup_flow.py`).
* **Resetting from Device Owner to Unprovisioned Mode**:
  Launch TestDPC on the device or emulator:
  ```bash
  adb shell am start -n com.sample.android.testdpc/.LaunchActivity
  ```
  Scroll to the bottom of the policy list, tap **"Remove this device owner"**, and click **OK** on the confirmation dialog.

### Mode B: Active Device Owner Mode
* **Active Screen**: `Policy Management` Dashboard
* **When to Use**: To test all 50+ enterprise policies, dialog modals, wipe data, app restrictions, and network stats (`tests/test_pages_walkthrough.py`, `tests/test_policies_flow.py`, `tests/test_manage_apps_flow.py`).
* **Prerequisites for Enabling Device Owner via ADB**:
  1. The target device or emulator must have **no user accounts** (Google, Exchange, etc.) configured. If an account is present, Android security blocks provisioning.
  2. No pre-existing Profile Owner or Device Owner can be active.
* **Enabling Device Owner Command**:
  ```bash
  adb shell dpm set-device-owner com.sample.android.testdpc/.DeviceAdminReceiver
  ```

---

## 6. How to Run Tests

### Step 1: Start your Android Emulator or connect a physical device
Verify that your device is detected and online:
```bash
adb devices
```

### Step 2: Start Appium Server
In a separate terminal window, launch Appium:
```bash
appium
```

### Step 3: Execute Test Suites

* **Run Multi-Page Live UI Walkthrough** (Visits and exercises 7 pages/modals live on screen):
  ```bash
  pytest tests/test_pages_walkthrough.py -v -s
  ```

* **Run Setup Wizard Flow**:
  ```bash
  pytest tests/test_setup_flow.py -v
  ```

* **Run Smoke Test Suite**:
  ```bash
  pytest -m smoke -v
  ```

* **Run Regression Policy & Management Tests**:
  ```bash
  pytest tests/test_manage_apps_flow.py tests/test_policies_flow.py -v
  ```

* **Run Full Suite Test Discovery**:
  ```bash
  pytest --collect-only -q
  ```

---

## 7. Test Reporting & Failure Artifacts

* **Terminal Console Reporting**: Standard execution summaries and tracebacks are output directly to the terminal. Use `--tb=short` for concise stack traces (optional: `--html=reports/report.html` if `pytest-html` is installed):
  ```bash
  pytest tests/ -v --tb=short
  ```
* **JUnit XML Test Results**: Generate machine-readable test reports for CI/CD dashboards:
  ```bash
  pytest tests/ --junitxml=reports/test-results.xml
  ```
* **Automated Failure Screenshots**: When any test fails, the custom `pytest_runtest_makereport` hook in `tests/conftest.py` automatically captures a full-resolution PNG and saves it to:
  ```text
  reports/screenshots/<test_name>.png
  ```

---

## 8. Continuous Integration (CI/CD)

The repository includes a GitHub Actions pipeline in [`.github/workflows/ci.yml`](.github/workflows/ci.yml) that triggers automatically on every `push` and `pull_request` to `main`:

* **Stage 1: Framework Validation (Ubuntu)**: Runs on `ubuntu-latest`, verifies Python dependencies, validates imports, and executes test discovery (`pytest --collect-only -v`).
* **Stage 2: Android Emulator E2E Suite (macOS)**: Runs on `macos-13` utilizing hardware-accelerated virtualization to boot an Android API 33 emulator, launches Appium, and installs the target APK with the `--bypass-low-target-sdk-block` flag (required on modern Android APIs for SDK 23 targets).
* **Stage 3: Artifact Publishing**: Automatically collects execution logs and failure screenshots and uploads them as downloadable GitHub Actions artifacts.
