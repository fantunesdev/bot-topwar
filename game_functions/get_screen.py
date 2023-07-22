import cv2
import PIL
import pyautogui
import pytesseract
import re

# from game_functions.general_functions import get_cursor_position


def save_relatory():
    pyautogui.sleep(1)
    favorite_button_rgb = {
        'r': 40,
        'g': 130,
        'b': 76,
        'name': 'favorite'
    }
    rival_button_rgb = {
        'r': 239,
        'g': 67,
        'b': 48,
        'name': 'rival'
    }
    confirme_button_rgb = {
        'r': 104,
        'g': 146,
        'b': 248,
        'name': 'confirme'
    }
    favorites_button_position = get_button_position(favorite_button_rgb)
    pyautogui.sleep(1)
    pyautogui.click(favorites_button_position)
    pyautogui.sleep(1)
    rival_button_position = get_button_position(rival_button_rgb)
    pyautogui.sleep(1)
    pyautogui.click(rival_button_position)
    confirme_button_position = get_button_position(confirme_button_rgb)
    pyautogui.sleep(1)
    pyautogui.click(confirme_button_position)
    pyautogui.sleep(1)


def get_button_position(button_rgb: dict):

    screenshot = pyautogui.screenshot(region=(0, 0, 1920, 1080))
    width, heigh = screenshot.size
    target = []

    for x in range(0, width):
        for y in range(0, heigh):
            r, g, b = screenshot.getpixel((x, y))
            if r == button_rgb['r'] and g == button_rgb['g'] and b == button_rgb['b']:
                target.append(x)
                target.append(y)

    try:
        target = [target[0], target[1]]
    except KeyError:
        print('As cores do botão mudaram. Por favor obtenha as novas cores e tente de novo.')
        exit(-1)

    return target


def get_relatory():
    pyautogui.sleep(1)

    pyautogui.click(112, 472)  # Pesquisa no mapa
    pyautogui.sleep(1)
    pyautogui.click(1106, 289)  # Aba Rival
    pyautogui.sleep(1)

    test = pyautogui.screenshot(region=(1069, 380, 110, 25))
    test.save('img/coordinates.png')
    image = cv2.imread('img/coordinates.png')
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


def get_actual_vit():
    pyautogui.sleep(2)
    pyautogui.click(175, 154)  # mostrador de VIT
    pyautogui.sleep(1)

    # obtendo imagem
    vit_img_time = pyautogui.screenshot(region=(840, 493, 253, 25))
    vit_img_time.save('img/vit_img_time.png')
    pyautogui.click(1175, 423)  # Botão fechar

    # Convertendo imagem em texto
    image = cv2.imread('img/vit_img_time.png')
    pure_text = pytesseract.image_to_string(image)
    text = pure_text.split(' ')[-1]
    h, m, s = 0, 0, 0
    try:
        try:
            h = int(text.split('h')[0])
        except ValueError:
            print('Não foi possível obter as horas para o carregamento total de VIT. Setando o valor padrão: 0.')
            h = 0
        try:
            m = int(text.split('h')[1].split('m')[0])
        except ValueError:
            print('Não foi possível obter os minutos para o carregamento total de VIT. Setando o valor padrão: 0.')
            m = 0
        try:
            s = int(text.split('m')[-1].replace('s', ''))
        except ValueError:
            print('Não foi possível obter os segundos para o carregamento total de VIT. Setando o valor padrão: 0.')
            s = 0
    except IndexError:
        pyautogui.click(1176, 114)  # Botão pra retornar à base
        pyautogui.sleep(1)
        pyautogui.click(1176, 114)
        # get_actual_vit()

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


def get_map_position(target: str):
    darkforces = {
        'center': (960, 591),
        'favorites': (1107, 193),
        'rival': (1090, 553),
        'coordinates': (1069, 380, 110, 25)
    }

    warhammer = {
        'center': (950, 617),
        'favorites': (1142, 219),
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
    if target == 'warhammer':
        selected = warhammer
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
    if target == 'warhammer':
        pure_text = pytesseract.image_to_string(image)  # boss
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
