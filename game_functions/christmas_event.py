import pyautogui
from game_functions import general_functions as gn


def bonfire_party(clicks: int):
    gn.open_game()
    pyautogui.sleep(5)
    gn.find_map_location(397, 481)
    print('Abrindo a janela do evento...')
    pyautogui.click(959, 562)
    pyautogui.sleep(3)
    for iteration in range(clicks):
        pyautogui.sleep(0.15)
        pyautogui.click(958, 915)