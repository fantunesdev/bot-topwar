import sys

from game_functions import general_functions, handle_log
from game_functions import get_screen



try:
    param1 = sys.argv[1]
except IndexError as message:
    print()
try:
    if param1 == 'darkforces':
        param2 = sys.argv[2]
        vit = int(param2)
        general_functions.attack_dark_forces(vit)
    # general_functions.restore_vit(10)
    if param1 == 'getcursor':
        general_functions.get_cursor_position()
    # get_screen.get_vit_value
    if param1 == 'level':
        print(get_screen.get_dark_forces_level())
    # general_functions.select_level(30)
    if param1 == 'worldboss':
        try:
            minutes = int(sys.argv[2])
            seconds = int(sys.argv[3])
            general_functions.attack_wordl_boss(minutes, seconds)
        except IndexError:
            print('É necessário informar os parâmetros: Minutos e Segundos.')
        except ValueError:
            print('É necessário que os parâmetros minutos e segundos sejam números inteiros')
    if param1 == 'readlog':
        handle_log.read_log()
    else:
        raise KeyError
except NameError as message:
    if 'param1' == message.name:
        print('*** ERRO *** O parâmetro 1 é obrigatório.\n')
        print('Opções válidas:')
        print('darkforces - Ataca a força das trevas. (É necessário passar a vit atual).')
        print('getcursor  - Printa no console a posição do cursor')
        print('level      - Obtém o nível da força das trevas a ser atacada.')
except KeyError as message:
    print('*** ERRO *** Opção de parâmetro inválida.\n')
    print('Opções válidas:')
    print('darkforces - Ataca a força das trevas. (É necessário passar a vit atual).')
    print('getcursor  - Printa no console a posição do cursor')
    print('level      - Obtém o nível da força das trevas a ser atacada.')
except KeyboardInterrupt:
    print('*** ENCERRANDO! ***')



# get_screen.get_vit_value()
