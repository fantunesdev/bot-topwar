import cv2
import PIL
import pyautogui
import pytesseract

# from game_functions.general_functions import get_cursor_position


def get_vit_value():
    # get_cursor_position()
    pyautogui.sleep(2)
    vit_img = pyautogui.screenshot(region=(156, 145, 28, 16))
    # vit_img = pyautogui.screenshot(region=(918, 985, 93, 27)) # botão search
    vit_img.save('img/vit_status.png')
    color = PIL.Image.open('img/vit_status.png').convert('L')
    grayscale = PIL.ImageOps.invert(color)
    grayscale.save('img/greyscale.png')
    image = cv2.imread('img/vit_status1.png')
    texto = pytesseract.image_to_string(image)
    # texto = pytesseract.image_to_string(PIL.ImageOps.invert(PIL.Image.open('img/vit_status1.png').convert('L')))
    print(texto)


def get_dark_forces_level():
    pyautogui.sleep(1)
    dark_forces_level_image = pyautogui.screenshot(region=(925, 894, 65, 17))
    dark_forces_level_image.save('img/dark_forces_level.png')
    image = cv2.imread('img/dark_forces_level.png')
    text = pytesseract.image_to_string(image)
    level_value = text.split(':')[1].split('.')[0].split('°')[0]
    return level_value


def get_wordl_boss_position():
    pyautogui.sleep(2)
    for i in range(5):
        try:
            wordl_boss_button = pyautogui.locateOnScreen('img/worldboss.png')
            x, y, width, height = wordl_boss_button
            return x + 15, y + 15
        except TypeError:
            return None


def calculate_position():
    pyautogui.sleep(2)
    test = pyautogui.screenshot(region=(60, 460, 120, 20))
    test.save('img/test.png')
    image = cv2.imread('img/test.png')
    text = pytesseract.image_to_string(image)
    print(text)
