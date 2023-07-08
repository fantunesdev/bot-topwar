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
    print('*** ERRO *** É necessário passar um parâmetro. Por favor, selecione uma das opções válidas.\n')
    print_menu()
    exit(-1)

try:
    if param1 == 'darkforces':
        general_functions.attack_dark_forces()
    if param1 == 'boss':
        general_functions.attack_wordl_boss()
    if param1 == 'refugee':
        general_functions.rescue_refugees()
    if param1 == 'warhammer':
        general_functions.attack_warhammer()
    if param1 == 'freegem':
        try:
            param2 = sys.argv[2]
        except IndexError:
            print('O é necessário passar o número de clicks como parâmetro.')
            exit(-1)
        clicks = int(param2)
        general_functions.free_gem(clicks)
    if param1 == 'dev':
        ...
    if param1 == 'cursor':
        general_functions.get_cursor_position()
    else:
        print('*** ERRO *** Opção de parâmetro inválida.\n')
        print_menu()
        print('*** ENCERRANDO! ***')
except KeyboardInterrupt:
    print('*** ENCERRANDO! ***')
