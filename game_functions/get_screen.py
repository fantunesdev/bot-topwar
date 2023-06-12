import cv2
import PIL
import pyautogui
import pytesseract
import re

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
            return


def get_map_position():

    # Salvando o relatório dos favoritos
    pyautogui.click(960, 591)  # darkforces
    pyautogui.sleep(1)
    pyautogui.click(1107, 193)  # Favoritos
    pyautogui.sleep(1)
    pyautogui.click(1090, 553)  # Rival
    pyautogui.sleep(1)
    pyautogui.click(953, 700)  # Botão Confirme
    pyautogui.sleep(1)
    pyautogui.click(112, 472)  # Pesquisa no mapa
    pyautogui.sleep(1)
    pyautogui.click(1106, 289)  # Aba Rival
    pyautogui.sleep(1)

    # Lendo a posição
    test = pyautogui.screenshot(region=(1069, 380, 110, 25))
    test.save('img/coordinates.png')
    image = cv2.imread('img/coordinates.png')
    pure_text = pytesseract.image_to_string(image).split(' ')[1]
    handle_text = re.sub('[^A-Za-z0-9]+', '', pure_text)
    words_list = handle_text.split('Y')
    x = int(words_list[0].replace('X', ''))
    y = int(words_list[1])

    # apagando o relatório de rivais
    pyautogui.sleep(1)
    pyautogui.click(745, 234)  # Engrenagem
    pyautogui.sleep(1)
    pyautogui.click(760, 381)  # Checkbox
    pyautogui.sleep(1)
    pyautogui.click(1085, 924)  # Botão apagar
    pyautogui.sleep(1)
    pyautogui.click(1176, 231)  # Botão Fechar

    return x, y


def get_favorites_button_position():
    try:
        favorites_button = pyautogui.locateOnScreen('img/favorites_btn.png')
        x, y = favorites_button
        return x, y
    except ValueError:
        print('não reconheceu favoritos')


def get_rivals_button_position():
    pyautogui.sleep(2)
    rivals_button = pyautogui.locateOnScreen('img/rival_btn.png')
    x, y = rivals_button
    return x, y


def get_relatory_worldboss():
    pyautogui.sleep(2)
    try:
        relatory_worldboss = pyautogui.locateOnScreen('img/relatory_worldboss.png')
        x, y, w, h = relatory_worldboss
        pyautogui.sleep(1)
        time_image = pyautogui.screenshot(region=(x + 80, y + 28, 100, 23))
        time_image.save('img/time_image.png')
        # image = cv2.imread('img/time_image.png')
        # grayscale = PIL.ImageOps.invert(image)
        # grayscale.save('img/wgreyscale.png')
        # full_time = pytesseract.image_to_string(grayscale)
        # print('texto: ', full_time)
        # h, m, s = full_time.split(':')
        # return h, m, s
    except TypeError:
        print('não')
        return None
