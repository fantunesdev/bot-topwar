import cv2
import PIL
import pyautogui
import pytesseract
import re

# from game_functions.general_functions import get_cursor_position


def get_actual_vit():
    pyautogui.sleep(2)
    pyautogui.click(175, 154)  # mostrador de VIT
    pyautogui.sleep(1)

    # obtendo imagem
    vit_img_time = pyautogui.screenshot(region=(840, 493, 253, 25))
    vit_img_time.save('img/vit_img_time.png')
    pyautogui.click(375, 354)

    # Convertendo imagem em texto
    image = cv2.imread('img/vit_img_time.png')
    pure_text = pytesseract.image_to_string(image)
    text = pure_text.split(' ')[-1]
    h = int(text.split('h')[0])
    m = int(text.split('h')[1].split('m')[0])
    s = int(text.split('m')[-1].replace('s', ''))

    # calculando vit disponível
    vit_recharge_time = 345
    total_time = 25875
    remaining_time = (h * 3600) + (m * 60) + s
    actual_vit = (total_time - remaining_time) // vit_recharge_time
    return actual_vit


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


def get_map_position(target: str):
    darkforces = {
        'center': (960, 591),
        'favorites': (1107, 193),
        'rival': (1090, 553),
        'coordinates': (1069, 380, 110, 25)
    }

    boss = {
        'center': (951, 533),
        'favorites': (1145, 618),
        'rival': (),
        'coordinates': (1090, 380, 80, 25)
    }

    if target == 'boss':
        selected = boss
    else:
        selected = darkforces

    # Salvando o relatório dos favoritos
    pyautogui.click(selected['center'])  # center
    pyautogui.sleep(1)
    pyautogui.click(selected['favorites'])  # Favoritos
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
    test = pyautogui.screenshot(region=(selected['coordinates']))
    test.save('img/coordinates.png')
    image = cv2.imread('img/coordinates.png')
    if target == 'darkforces':
        pure_text = pytesseract.image_to_string(image).split(' ')[1].replace(':', '')  # darkforces
    if target == 'boss':
        pure_text = pytesseract.image_to_string(image)  # boss
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
