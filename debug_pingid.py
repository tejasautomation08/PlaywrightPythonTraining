"""
Debug script to inspect PingID window controls
Run this script to see all available controls in the PingID window
This helps identify correct control names if automation fails
"""

import time
from pingid_automation import PingIDAutomation


def main():
    """Debug PingID window controls"""
    print("=" * 60)
    print("PingID Window Inspector")
    print("=" * 60)
    print("\nThis script will:")
    print("1. Launch PingID.exe")
    print("2. Connect to the PingID window")
    print("3. Display all available controls and their properties")
    print("\nPlease ensure PingID.exe path is correct in config.py")
    print("=" * 60)

    input("\nPress Enter to start...")

    pingid = PingIDAutomation()

    # Launch PingID
    print("\n[1/3] Launching PingID...")
    if not pingid.launch_pingid():
        print("❌ Failed to launch PingID. Check exe_path in config.py")
        return

    # Connect to window
    print("\n[2/3] Connecting to PingID window...")
    if not pingid.connect_to_pingid_window():
        print("❌ Failed to connect to PingID window")
        return

    # Print window information
    print("\n[3/3] Inspecting window controls...")
    pingid.print_window_info()

    print("\n" + "=" * 60)
    print("Inspection complete!")
    print("Use the control identifiers above to update pingid_automation.py")
    print("if the automation is not working correctly.")
    print("=" * 60)


if __name__ == "__main__":
    main()
