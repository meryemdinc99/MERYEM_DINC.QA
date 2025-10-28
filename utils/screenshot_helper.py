import os
import datetime

def take_screenshot(driver, test_name, folder="screenshots"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/{test_name}_{timestamp}.png"
    driver.save_screenshot(filename)
    return filename
