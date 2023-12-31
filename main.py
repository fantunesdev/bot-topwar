import sys

from game_functions import general_functions, handle_log
from game_functions import get_screen


def print_menu():
    print('Opções válidas:')
    print('darkforces - Ataca a força das trevas. (É necessário passar a VIT atual).')
    print('boss       - Ataca o chefão mundial.')
    print('refugee    - Resgate de refugiados. (É necessário passar a VIT atual).')
    print('warhammer  - Ataca warhammers.')
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
        if len(sys.argv) > 2:
            try:
                recharges = int(sys.argv[2])
            except ValueError:
                print(f'Você passou o parâmetro: {sys.argv[2]}. O número de recargas precisa ser um número inteiro.')
                exit(-1)
        else:
            recharges = 0
        if recharges < 0:
            print('Você precisa passar um número maior que 1.')
            exit(-1)
        if recharges > 20:
            print('Você precisa passar um número menor que 20.')
            exit(-1)
        general_functions.handle_attack_dark_forces(recharges)
    elif param1 == 'boss':
        general_functions.attack_world_boss()
    elif param1 == 'refugee':
        general_functions.rescue_refugees()
    elif param1 == 'warhammer':
        general_functions.attack_warhammer()
    elif param1 == 'freegem':
        try:
            param2 = sys.argv[2]
        except IndexError:
            print('O é necessário passar o número de clicks como parâmetro.')
            exit(-1)
        clicks = int(param2)
        general_functions.free_gem(clicks)
    elif param1 == 'dev':
        pass
    elif param1 == 'cursor':
        general_functions.get_cursor_position()
    else:
        print('*** ERRO *** Opção de parâmetro inválida.\n')
        print_menu()
        print('*** ENCERRANDO! ***')
except KeyboardInterrupt:
    print('*** ENCERRANDO! ***')
