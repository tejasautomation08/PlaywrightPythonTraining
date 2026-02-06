import time
from pywinauto.application import Application
from pywinauto import Desktop
import subprocess
import allure
import pytest

@allure.feature('Calculator Application')
@allure.story('Basic Arithmetic Operations')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Verify Calculator Addition: 9 + 1 = 10')
@allure.description('Test validates basic addition operation in Windows Calculator using pywinauto UI automation')
@allure.tag('calculator', 'desktop-app', 'arithmetic')
def test_calculator_addition():
    """Test calculator addition operation using pywinauto"""

    with allure.step("Launch Calculator application"):
        print("Launching Calculator...")
        subprocess.Popen("calc.exe")
        time.sleep(3)
        allure.attach("calc.exe", name="Application", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Verify Calculator launched successfully"):
        try:
            desktop = Desktop(backend="uia")
            calc_window = desktop.window(title="Calculator", class_name="ApplicationFrameWindow")
            calc_window.set_focus()
            print("Calculator launched successfully!")
            print(f"Window Title: {calc_window.window_text()}")
            allure.attach(f"Window Title: {calc_window.window_text()}",
                         name="Calculator Window Info",
                         attachment_type=allure.attachment_type.TEXT)
            time.sleep(1)

        except Exception as e:
            allure.attach(str(e), name="Launch Error", attachment_type=allure.attachment_type.TEXT)
            print(f"\nError occurred during launch: {str(e)}")
            pytest.fail(f"Failed to launch Calculator: {str(e)}")

    with allure.step("Click on number 9"):
        try:
            print("\nClicking on Nine...")
            nine_button = calc_window.child_window(auto_id="num9Button", control_type="Button")
            nine_button.click()
            time.sleep(0.5)
        except Exception as e:
            allure.attach(str(e), name="Click Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"Failed to click number 9: {str(e)}")

    with allure.step("Click on Plus operator"):
        try:
            print("Clicking on Plus...")
            plus_button = calc_window.child_window(auto_id="plusButton", control_type="Button")
            plus_button.click()
            time.sleep(0.5)
        except Exception as e:
            allure.attach(str(e), name="Click Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"Failed to click Plus operator: {str(e)}")

    with allure.step("Click on number 1"):
        try:
            print("Clicking on One...")
            one_button = calc_window.child_window(auto_id="num1Button", control_type="Button")
            one_button.click()
            time.sleep(0.5)
        except Exception as e:
            allure.attach(str(e), name="Click Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"Failed to click number 1: {str(e)}")

    with allure.step("Click on Equals button"):
        try:
            print("Clicking on Equals...")
            equals_button = calc_window.child_window(auto_id="equalButton", control_type="Button")
            equals_button.click()
            time.sleep(0.5)
        except Exception as e:
            allure.attach(str(e), name="Click Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"Failed to click Equals: {str(e)}")

    with allure.step("Verify calculation result equals 10"):
        try:
            print("\nGetting result...")
            result_display = calc_window.child_window(auto_id="CalculatorResults", control_type="Text")
            result_text = result_display.window_text()
            print(f"\nCalculation Result: {result_text}")
            allure.attach(result_text,
                         name="Calculation Result",
                         attachment_type=allure.attachment_type.TEXT)

            # Assert the result contains 10
            assert "10" in result_text, f"Expected result to contain '10', but got: {result_text}"

        except AssertionError as e:
            allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
            raise
        except Exception as e:
            allure.attach(str(e), name="Verification Error", attachment_type=allure.attachment_type.TEXT)
            print(f"\nError occurred: {str(e)}")
            print("\nInspecting Calculator structure for debugging...")

            try:
                desktop = Desktop(backend="uia")
                calc_window = desktop.window(title="Calculator")
                print("\nPrinting Calculator control identifiers...")
                calc_window.print_control_identifiers(depth=5, filename="calculator_structure.txt")
                print("Structure saved to calculator_structure.txt")
                allure.attach.file("calculator_structure.txt",
                                  name="Calculator Structure",
                                  attachment_type=allure.attachment_type.TEXT)
            except Exception as debug_error:
                print(f"Debug error: {debug_error}")

            pytest.fail(f"Failed to verify result: {str(e)}")

    with allure.step("Close Calculator application"):
        try:
            print("\nClosing Calculator...")
            calc_window.close()
            print("\nTest completed successfully!")
        except Exception as e:
            print(f"Warning: Failed to close Calculator: {str(e)}")
            # Don't fail the test if closing fails