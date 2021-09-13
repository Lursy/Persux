from data.ferramentas import *
from data.cores_persux import *
from data.menu import senhaf, ban_sen


def senha():
    while True:
        rnick = ''
        vn = os.path.exists('.Nick')
        vs = os.path.exists('.Senha')
        if vn:
            rnick = open('.Nick', 'r')
        rcor = open('.Cor', 'r')
        if vs:
            print(ban_sen)
            sen_exists = str(input(f'{am}//: {br}'))
            if sen_exists == '1':
                os.system('clear')
                pass
            elif sen_exists == '2':
                os.system('rm -rf .Senha')
                os.system('rm -rf bash.bashrc')
                bash = open('bash.bashrc', 'w')
                bash.write(f'{inicio}\n' + f'\n{rnick.read()}\n{rcor.read()}' if vn
                           else f'{rcor.read()}' + f'{final}')
                bash.close()
                print(f'{vd}!Sucess!')
                sleep(1)
                break
            elif sen_exists == '3':
                os.system('clear')
                break
            else:
                print(f'{ve}{sen_exists} não é um comando')
                sleep(2)
                break
        clear()
        print(senhaf)
        senhaa = str(input(f'{am}Senha: {br}'))
        senhab = str(input(f'{am}Confirme a senha: {br}'))
        if senhaa == senhab:
            ssenha = f'''
echo 'import os
from time import sleep
def menu():
    try:
        User = input("\\033[0;31mSenha: \\033[0;36m")
        if User == "{senhab}":
            sleep(1)
            os.system("clear")
        elif User != "{senhab}":
            os.system("clear")
            menu()
    except:
         print("Senha Não identificada!")
         sleep(1)
         os.system("clear")
         menu()
menu()' >> usr.py
python usr.py
rm -rf usr.py'''
            os.system('rm -rf .Senha')
            os.system('rm -rf bash.bashrc')
            senha_file = open('.Senha', 'w')
            senha_file.write(ssenha)
            senha_file.close()
            rsenha = open('.Senha', 'r')
            bash = open('bash.bashrc', 'w')
            bash.write(f'{inicio}\n{rsenha.read()}\n{rnick.read()}\n{rcor.read()}\n{final}' if vn
                       else f'{inicio}\n{rsenha.read()}\n{rcor.read()}\n{final}')
            bash.close()
            break
