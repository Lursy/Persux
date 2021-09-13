from data.ferramentas import *
from data.cores_persux import *
from data.menu import coresf, cor


def letra():
    os.system('clear')
    scor = user = rnick = rsenha = open('.usuario', 'r').readline()
    cor_letra = f"PS1='\[\e[0;31m\]┏(\[\e[0;34m\]{user}\[\e[0;31m\])" \
                f" [\[\e[0;32m\]\w\[\e[0;31m\]] \\n\[\e[0;31m\]┗► \[\e[1;:corm\]'"
    while True:
        clear()
        vn = os.path.exists('.Nick')
        vs = os.path.exists('.Senha')
        if vs:
            rsenha = open('.Senha', 'r').read()
        if vn:
            rnick = open('.Nick', 'r').read()
        print(coresf)
        cor()
        print(f'{vd}[i] {br}cor da letra no terminal\n')
        cores = str(input(f'\n{am}//: {br}'))
        for c in range(0, 8):
            if cores == f'{c+1}':
                if c != '8':
                    scor = cor_letra.replace(':cor', f'3{c+1}')
                else:
                    break
        if scor == user:
            print(f'{ve}{cores} não é um comando!')
            sleep(2)
            break
        os.system('rm -rf bash.bashrc')
        os.system('rm -rf .Cor')
        cor_file = open('.Cor', 'w')
        cor_file.write(f'{scor}')
        cor_file.close()
        rcor = open('.Cor', 'r').read()
        with open('bash.bashrc', 'w') as bash:
            bash.write((f'{inicio}\n{rsenha}\n{rnick}\n{rcor}\n{final}' if vs and vn
                        else f'{inicio}\n{rsenha}\n{rcor}\n{final}' if not vn
                        else f'{inicio}\n{rnick}\n{rcor}\n{final}'))
        break
