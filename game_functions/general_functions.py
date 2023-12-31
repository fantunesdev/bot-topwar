import datetime
import math
import random

import pyautogui

from config import base_location, boss_rgb, favorite_rgb
from game_functions import get_screen, handle_log

buttons = {
    'magnifier': (756, 1018),
    'search': (958, 999),
    'attack': (955, 510),
    'diana_squad': (1487, 919),
    'level': {
        '67': (852, 929),
        '76': (959, 929),
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
    pyautogui.displayMousePosition()


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
        pyautogui.sleep(3)
        pyautogui.click(1595, 313)
        remaining_clicks -= 1
        print(f'Limite (hoje): {remaining_clicks}.')

        if not remaining_clicks == 0:
            for i in range(5):
                pyautogui.sleep(60)
                pyautogui.click(1287, 212)
                pyautogui.sleep(1)
                pyautogui.click(1406, 212)


def handle_attack_dark_forces(recharges: int):
    pyautogui.sleep(2)
    print(f'{get_now()} - Iniciando ataque com {recharges} recargas.')
    if recharges == 0:
        vit = get_screen.get_actual_vit()
        if vit > 25:
            attack_dark_forces(vit)
        else:
            print(f'{get_now()} - Não há VIT suficiente para fazer o ataque sem recargas: {vit}.')
    else:
        for i in range(recharges):
            vit = get_screen.get_actual_vit()
            if vit < 25:
                add_vit_value = 50
                print(f'{get_now()} - Não há VIT suficiente. Fazendo a {i + 1}ª recarga.')
                restore_vit(add_vit_value)
                pyautogui.sleep(1)
                pyautogui.click(1705, 350)
            attack_dark_forces(vit)
    print(f'{get_now()} - Fim do ataque.')


def attack_dark_forces(vit):
    counter = 0
    while True:
        pyautogui.sleep(1)
        pyautogui.click(buttons['magnifier'])
        pyautogui.sleep(1)
        pyautogui.click(buttons['rival'])
        pyautogui.sleep(1)
        # select_level(counter)
        pyautogui.sleep(1)
        # select_force(counter)
        pyautogui.sleep(1)
        pyautogui.click(buttons['search'])
        pyautogui.sleep(1)
        pyautogui.click(buttons['center'])
        pyautogui.sleep(1)
        get_screen.save_relatory()
        pyautogui.sleep(1)
        x, y = get_screen.get_relatory()
        pyautogui.sleep(1)
        time = calculate_time(x, y, 'darkforces')
        print(f'{get_now()} - O tempo de marcha é de {time} segundos.')
        pyautogui.click(buttons['center'])
        pyautogui.sleep(1)
        pyautogui.click(buttons['5_attack'])
        pyautogui.sleep(1)
        pyautogui.click(buttons['diana_squad'])
        pyautogui.sleep(1)
        pyautogui.click(buttons['attack'])
        pyautogui.sleep(240 + (time * 2) + 2)

        vit = get_screen.get_actual_vit()
        print(f'{get_now()} - VIT disponível: {vit}.')

        counter += 1
        if vit < 25:
            break


def attack_world_boss():
    pyautogui.sleep(2)
    button_rgb = boss_rgb
    now = datetime.datetime.now()
    if now.hour in [1, 9, 17]:
        x, y = get_screen.get_button_position(button_rgb)
    else:
        print(f'{get_now()} - Fora do horário do evento do chefão. Encerrando.')
        exit(62)
    pyautogui.click(x, y)  # worldboss button position
    pyautogui.sleep(1)
    pyautogui.click(970, 762)  # Pesquisa rápida
    pyautogui.sleep(1)
    pyautogui.click(buttons['center'])
    pyautogui.sleep(1)
    get_screen.save_relatory()
    pyautogui.sleep(1)
    x, y = get_screen.get_relatory()
    pyautogui.sleep(1)
    time = calculate_time(x, y, 'boss')
    print(f'{get_now()} - O tempo de marcha é de {time} segundos.')
    for i in range(0, 5):
        pyautogui.click(buttons['center'])
        pyautogui.sleep(1)
        pyautogui.click(1056, 894)  # botão atacar
        pyautogui.sleep(1)
        pyautogui.click(1485, 920)  # Diana squad
        pyautogui.sleep(1)
        pyautogui.click(952, 516)  # Marchar
        pyautogui.sleep(time)
        message = {
            'text': 'Chefão Mundial',
            'action': 'Ataque'
        }
        handle_log.write_log(message)
        print(f'Atacou o Chefão! Retornando...')
        pyautogui.sleep(time)
        print('Chegou na base.')
        pyautogui.sleep(2)
    handle_log.read_log()


def rescue_refugees():
    pyautogui.sleep(2)
    vit = get_screen.get_actual_vit()
    print(f'VIT inicial: {vit}.')
    while True:
        print(f'Iniciando resgate.')
        pyautogui.sleep(1)
        pyautogui.click(1867, 250)  # Botão de evento regular
        pyautogui.sleep(1)
        pyautogui.click(1183, 225)  # Aba dos refugiados
        pyautogui.sleep(1)
        pyautogui.click(1124, 1010)  # Abre o inventário com as cartas na primeira posição
        pyautogui.sleep(1)
        pyautogui.click(757, 328)  # Abre carta dos refugiados
        pyautogui.sleep(1)
        pyautogui.click(957, 1017)  # Clica em Usa
        pyautogui.sleep(2)
        pyautogui.click(960, 602)  # Clica nos refugiados
        pyautogui.sleep(1)
        pyautogui.click(1060, 492)  # Clica no botão Reunir
        pyautogui.sleep(1)
        pyautogui.click(1488, 920)  # Seleciona Diana Squad
        pyautogui.sleep(1)
        pyautogui.click(960, 510)  # Envia
        pyautogui.sleep(80)
        vit = get_screen.get_actual_vit()
        print(f'Resgatou os refugiados. VIT disponível: {vit}')
        if vit < 5:
            print(f'Fim do resgate. A VIT acabou. {vit}')
            break


def attack_warhammer():
    pyautogui.sleep(2)
    for i in range(2):
        vit = get_screen.get_actual_vit()
        pyautogui.sleep(3)
        pyautogui.click(736, 1019)  # Lupa de pesquisa
        pyautogui.sleep(1)
        pyautogui.click(1030, 560)  # Aba reunir
        pyautogui.sleep(1)
        pyautogui.click(1040, 933)  # Level 70 de warhammer
        pyautogui.sleep(1)
        pyautogui.click(963, 1011)  # Botão Pesquisar
        pyautogui.sleep(1)
        x, y = get_screen.get_map_position('warhammer')
        time = calculate_time(x, y, 'warhammer')
        pyautogui.sleep(1)
        pyautogui.click(963, 608)  # Warhammer centralizado
        pyautogui.sleep(1)
        pyautogui.click(1065, 487)  # botão reunir
        pyautogui.sleep(1)
        pyautogui.click(1487, 926)  # Diana Squad
        pyautogui.sleep(1)
        pyautogui.click(959, 513)  # Botão lutar
        pyautogui.sleep(60 + time)
        if vit < 10:
            break


def restore_vit(portion: int):
    print(f'{get_now()} - Recarregando {portion} de VIT.')
    if portion in (10, 50):
        portion_button = {
            '10': (825, 632),
            '50': (965, 632)
        }
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
    pyautogui.sleep(1)
    if iterations % 12 == 0:
        level = int(get_screen.get_dark_forces_level())
        if level >= max_level or iterations == 0:
            pyautogui.click(buttons['level']['76'])
        else:
            pyautogui.click(buttons['level']['increase'])


def calculate_time(x: int, y: int, target: str):
    base = base_location

    if target == 'boss':
        velocity = 1.89746
    elif target == 'warhammer':
        velocity = 1.5
    else:
        velocity = 2.325807970587723

    target = {
        'x': x,
        'y': y
    }

    target_x = base['x'] - target['x']
    target_y = base['y'] - target['y']
    distance = (target_x ** 2 + target_y ** 2) ** (1 / 2)
    time = math.ceil(distance / velocity)

    return time


def get_now():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')



def handle_auto_join(value: bool):
    pyautogui.sleep(2)
    pyautogui.click(1862, 756)  # Botão da aliança
    pyautogui.sleep(1)
    pyautogui.click(865, 863)  # Botão Batalhas
    pyautogui.sleep(1)
    pyautogui.click(1087, 952)  # Botão Participar
    pyautogui.sleep(1)
    if value == True:
        pyautogui.click(885, 919)  # Botão Aberto
    else:
        pyautogui.click(1104, 919)  # Botão Fechado
    for i in range(3):
        pyautogui.sleep(1)
        pyautogui.click(733, 152)  # Click para sair da janela.
