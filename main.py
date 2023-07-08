import sys

from game_functions import general_functions, handle_log
from game_functions import get_screen


def print_menu():
    print('Opções válidas:')
    print('darkforces - Ataca a força das trevas. (É necessário passar a VIT atual).')
    print('boss       - Ataca o chefão mundial.')
    print('refugee    - Resgate de refugiados. (É necessário passar a VIT atual).')
    print('gem        - Coleta os diamantes diários gratuitos. (É necessário passar o número de clicks).')
    print('cursor     - Printa no console a posição do cursor')


try:
    param1 = sys.argv[1]
except IndexError as message:
    print_menu()
try:
    if param1 == 'darkforces':
        param2 = sys.argv[2]
        vit = int(param2)
        general_functions.attack_dark_forces(vit)
    if param1 == 'boss':
        general_functions.attack_wordl_boss()
    if param1 == 'refugee':
        general_functions.rescue_refugees()
    if param1 == 'warhammer':
        general_functions.attack_warhammer()
    if param1 == 'freegem':
        param2 = sys.argv[2]
        clicks = int(param2)
        general_functions.free_gem(clicks)
    if param1 == 'dev':
        get_screen.get_relatory()
    if param1 == 'cursor':
        general_functions.get_cursor_position()
    # else:
    #     raise KeyError
except NameError as message:
    if 'param1' == message.name:
        print('*** ERRO *** O parâmetro 1 é obrigatório.\n')
        print_menu()

except KeyError as message:
    print('*** ERRO *** Opção de parâmetro inválida.\n')
    print_menu()
except KeyboardInterrupt:
    print('*** ENCERRANDO! ***')
