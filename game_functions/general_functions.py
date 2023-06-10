import datetime
import random

import pyautogui

from game_functions import get_screen, handle_log

buttons = {
    'magnifier': (756, 1018),
    'search': (958, 999),
    'attack': (955, 510),
    'diana_squad': (1487, 919),
    'level': {
        '67': (852, 929),
        '80': (999, 929),
        '81': (1013, 929),
        '82': (1026, 929),
        '83': (1039, 929),
        '84': (1050, 929),
        '85': (1060, 929),
        '86': (1065, 929),
        'increase': (1100, 929),
        'decrease': (820, 929)
    },
    'rival': (768, 557),
    'forces': {
        'air_force': (1122, 720),
        'navy': (954, 720),
        'army': (795, 720)
    },
    'center': (967, 593),
    '5_attack': (878, 471)
}


def get_cursor_position():
    while True:
        print(pyautogui.position(), ' Aperte Ctrl+C para parar.')


def open_game():
    print('Abrindo o Top War...')
    pyautogui.hotkey('winleft', 'space')
    pyautogui.sleep(1)
    pyautogui.hotkey('winleft')
    pyautogui.sleep(1)
    pyautogui.write('topwar')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('winleft', 'space')
    print('Jogo aberto.')


def find_map_location(x: int, y: int):
    print('Localizando uma posição no mapa...')
    # Abrir o localizador do mapa
    pyautogui.click(111, 473)
    pyautogui.sleep(1)
    # Setando o posicionamento
    pyautogui.doubleClick(970, 873)
    pyautogui.sleep(1)
    pyautogui.write(f'{x}')
    pyautogui.sleep(1)
    pyautogui.doubleClick(1094, 877)
    pyautogui.click(968, 932)
    pyautogui.sleep(1)
    pyautogui.write(f'{y}')
    pyautogui.hotkey('enter')


def free_gem(clicks: int):
    pyautogui.sleep(5)
    remaining_clicks = clicks
    for iteration in range(clicks):
        pyautogui.sleep(1)
        pyautogui.click(1595, 313)
        remaining_clicks -= 1
        print(f'Limite (hoje): {remaining_clicks}.')

        if not remaining_clicks == 0:
            for i in range(5):
                pyautogui.sleep(60)
                pyautogui.click(1287, 212)
                pyautogui.sleep(1)
                pyautogui.click(1406, 221)


def attack_dark_forces(vit: int):
    pyautogui.sleep(2)
    recharges = 3
    for i in range(recharges):
        if vit < 25:
            add_vit_value = 10
            restore_vit(add_vit_value)
            vit += add_vit_value
            pyautogui.click(1705, 350)
            print(f'VIT disponível: {vit}.')
        else:
            counter = 0
            while True:
                pyautogui.sleep(1)
                pyautogui.click(buttons['magnifier'])
                pyautogui.sleep(1)
                pyautogui.click(buttons['rival'])
                pyautogui.sleep(1)
                select_level(counter)
                pyautogui.sleep(1)
                select_force(counter)
                pyautogui.sleep(1)
                pyautogui.click(buttons['search'])
                pyautogui.sleep(1)
                pyautogui.click(buttons['center'])
                pyautogui.sleep(1)
                pyautogui.click(buttons['5_attack'])
                pyautogui.sleep(1)
                pyautogui.click(buttons['diana_squad'])
                pyautogui.sleep(1)
                pyautogui.click(buttons['attack'])
                vit -= 15
                print(f'VIT disponível: {vit}.')
                pyautogui.sleep(350)
                vit += 1
                counter += 1
                if vit < 25:
                    break
        print(f'Iteração: {i + 1}')

    print('Fim do pograma.')


def restore_vit(portion: int):
    if portion in (10, 50):
        portion_button = {
            '10': (825, 632),
            '50': (965, 632)
        }
        print(f'Recarregando {portion} de VIT.')
        pyautogui.sleep(1)
        pyautogui.click(222, 150)
        pyautogui.sleep(1)
        pyautogui.click(portion_button[str(portion)])
        pyautogui.sleep(1)
        pyautogui.click(961, 771)
    else:
        print('Valores válidos: 10, 50.')


def select_force(counter: int):
    pyautogui.sleep(1)
    force_index = counter % 3
    force_key = list(buttons['forces'])[force_index]
    force = buttons['forces'][force_key]
    pyautogui.click(force)


def select_level(iterations: int):
    max_level = 83
    for counter in range(iterations):
        pyautogui.sleep(1)
        if counter < 6:
            level = 80
            selected_level = buttons['level'][str(level)]
            pyautogui.click(selected_level)
        elif level >= max_level:
            print('condição 3')
            level = 80
            selected_level = buttons['level']['80']
            pyautogui.click(selected_level)
        elif counter % 6 == 0:
            print('condição 2')
            level = int(get_screen.get_dark_forces_level())
            pyautogui.click(buttons['level']['increase'])


def attack_wordl_boss(minutes: int, seconds: int):
    pyautogui.sleep(2)
    for i in range(5):
        try:
            x, y = get_screen.get_wordl_boss_position()
            pyautogui.click(x, y)
            pyautogui.sleep(1)
            pyautogui.click(960, 767)  # botão pesquisa rápida
            pyautogui.sleep(1)
            pyautogui.click(957, 505)  # Chefão
            pyautogui.sleep(1)
            pyautogui.click(1056, 894)  #botão atacar
            pyautogui.sleep(1)
            pyautogui.click(1483, 920)  # Diana squad
            pyautogui.sleep(1)
            pyautogui.click(952, 516)  # Marchar
            message = {
                'text': 'Chefão Mundial',
                'action': 'Ataque'
            }
            handle_log.write_log(message)
            time = (minutes * 60 + seconds) * 2 + 3
            pyautogui.sleep(time)
        except TypeError:
            print('O chefão não foi encontrado.')
            break
