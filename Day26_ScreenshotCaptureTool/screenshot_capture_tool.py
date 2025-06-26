import pyautogui
import time
from datetime import datetime

def take_screenshot():
    choice=input("Do you want to Delay before capture? (yes/no): ").lower()

    if choice=="yes":
        delay=int(input("Enter delay in seconds: "))
        print(f"Capturing screenshot in {delay} seconds.....")
        time.sleep(delay)

        filename=input("Enter filename(leave blank to use timestamp:  ").strip()

        if not filename:
            filename=datetime.now().strftime("screenshot_%Y%m%d_%H%M%S.png")
        else:
            filename=f"{filename}.png"

        screenshot=pyautogui.screenshot()
        screenshot.save(filename)
        print(f"Screenshot saved as {filename}")

take_screenshot()