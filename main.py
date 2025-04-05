from pyautogui import size as monitor_size
from PIL import ImageGrab
from datetime import datetime
from pathlib import Path
from time import sleep


def capture_screenshot() -> ImageGrab:
    width, height = monitor_size()
    target_ratio = 16/9

    if width/height < target_ratio:  # Screen too tall (e.g 16:10, 4:3)
        target_height = width * 9 / 16
        target_width = width
    else:  # Screen too wide (e.g. 21:9, ultrawide)
        target_width = height * 16 / 9
        target_height = height

    image = ImageGrab.grab(
        bbox=(round((width - target_width)/2), round((height - target_height)//2), round(width - (width - target_width)//2), round(height - (height - target_height)//2))
    )
    max_width = 1920
    scale_factor = max_width / width
    image = image.resize(size=(round(width * scale_factor), round(height * scale_factor)))
    return image


def main():
    subdir = input("Enter Folder Name: ")
    folder_path = f"Screenshots/{subdir}"
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    print(f"Starting screen captures. Saving to {folder_path}.")

    for _ in range(1000):
        image = capture_screenshot()
        image.save(f"{folder_path}/{datetime.now().strftime("%Y%m%d%H%M%S")}.png")
        sleep(15)


if __name__ == "__main__":
    main()
