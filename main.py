import os
import pyperclip

from utils import notifier
from utils import uploader
from utils import files

SCREENSHOT_DIR_PATH = f"{os.path.expanduser('~')}/Pictures"

def main():
    notifier.send("File Uploader", "Uploader started in the background.\nTake a screenshot and a URL will be copied.")

    screenshot_dir = os.path.join(SCREENSHOT_DIR_PATH, "Screenshots")
    stored_files = os.listdir(screenshot_dir)

    while True:
        newest_file = files.get_newest_file(screenshot_dir)
        newest_file_no_path = newest_file.split("/")[-1]

        if newest_file_no_path not in stored_files:
            url = uploader.upload_screenshot(newest_file)
            pyperclip.copy(url)
            stored_files.append(newest_file_no_path)

            print(f"Copied to clipboard: {url}")
            notifier.send("File Uploader", "Screenshot copied to clipboard")

if __name__ == "__main__":
    main()