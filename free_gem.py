import sys

from game_functions import general_functions

param = sys.argv[1]

try:
    clicks = int(param)
    general_functions.free_gem(clicks)
except ValueError:
    print(f'ERRO! "{param}" não é um número inteiro!')
except KeyboardInterrupt:
    print('*** ENCERRANDO! ***')
    print("Obrigado por usar o TopWarFreeGem.")
