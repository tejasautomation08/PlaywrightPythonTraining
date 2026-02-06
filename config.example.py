"""
Configuration file for test automation settings
Copy this file to config.py and update with your actual values
"""

# PingID Configuration
PINGID_CONFIG = {
    "exe_path": r"C:\Program Files (x86)\Ping Identity\PingID\PingID.exe",  # Update this path to your actual PingID.exe location
    "pin": "YOUR_PIN_HERE",  # Update this with your actual PIN
    "wait_timeout": 10  # Seconds to wait for PingID window to appear
}

# Browser Configuration
BROWSER_CONFIG = {
    "headless": False,
    "slow_mo": 500  # Milliseconds to slow down browser actions for visibility
}
