from Persux.data.menu import menu_nome
from Persux.data.cores_persux import *
from Persux.data.ferramentas import *


def nome_letra():
    while True:
        print(menu_nome)
        options = str(input(f'{am}//: {br}'))
        if options == '1':
            rnick = rsenha = antigo = open('.usuario', 'r').readline()
            os.system('rm -rf .usuario')
            vn = os.path.exists('.Nick')
            vs = os.path.exists('.Senha')
            clear()
            user = str(input(f'{am}Nome: {ve}'))
            with open('.usuario', 'w') as user_file:
                user_file.write(user)
            try:
                cor = open('.Cor', 'r').read()
            except FileNotFoundError:
                break
            os.system('rm -rf .Cor')
            with open('.Cor', 'w') as rcor:
                rcor.write(f'{cor.replace(antigo, user)}')
            rcor = cor.replace(antigo, user)
            if vs:
                rsenha = open('.Senha', 'r').read()
            if vn:
                rnick = open('.Nick', 'r').read()
            os.system('rm -rf bash.bashrc')
            with open('bash.bashrc', 'w') as bash:
                bash.write((f'{inicio}\n{rsenha}\n{rnick}\n{rcor}\n{final}' if vs and vn
                            else f'{inicio}\n{rsenha}\n{rcor}\n{final}' if not vn
                            else f'{inicio}\n{rnick}\n{rcor}\n{final}'))
        else:
            print(f'{ve}Comando inválido!' if options != '2' else '')
            sleep(2 if options != '2' else 0.5)
        break
