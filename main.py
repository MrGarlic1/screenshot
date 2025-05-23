from pyautogui import size as monitor_size
from PIL import ImageGrab
from datetime import datetime
from pathlib import Path
from time import sleep


def capture_screenshot() -> ImageGrab:
    width, height = monitor_size()

    image = ImageGrab.grab(
        bbox=(0, 96, width, height - 55)
    )

    # max_width = 1920
    # scale_factor = max_width / width
    # image = image.resize(size=(round(width * scale_factor), round(height * scale_factor)))
    return image


def main():
    subdir = input("Enter Folder Name: ")
    folder_path = f"Screenshots/{subdir}"
    Path(f"{folder_path}/Easy").mkdir(parents=True, exist_ok=True)
    Path(f"{folder_path}/Medium").mkdir(parents=True, exist_ok=True)
    Path(f"{folder_path}/Hard").mkdir(parents=True, exist_ok=True)
    print(f"Starting screen captures. Saving to {folder_path}.")

    interval = 15

    for _ in range(int(25*60/interval)):
        image = capture_screenshot()
        image.save(f"{folder_path}/{datetime.now().strftime("%Y%m%d%H%M%S")}.png")
        sleep(interval)

    print("Image capturing complete.")


if __name__ == "__main__":
    main()
