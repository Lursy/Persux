import os
from data.cores_persux import *


def install():
    inst = os.path.exists('.usuario')
    if not inst:
        null = '&>/dev/null'
        os.system(f'apt upgrade -y {null}')
        os.system(f'python3 -m pip install --upgrade pip {null}')
        req = (('pip', 'lolcat'), ('pip', 'pyfiglet'), ('pkg', 'figlet -y'))
        for item in req:
            os.system(f'{item[0]}  install {item[1]} {null}')
        os.system('clear')
        user = str(input(f'{ve}Nome: {cy}'))
        os.system('rm -rf .Cor')
        cor = open('.Cor', 'w')
        cor.write(f"PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
        cor.close()
        os.system('rm -rf motd')
        user_file = open('.usuario', 'w')
        user_file.write(user)
        user_file.close()
    os.system('clear')


def git_pull():
    from time import sleep
    os.system('rm -rf pull')
    os.system('git pull &>pull')
    with open('pull', 'r') as p:
        pull = p.read()
    if 'Already up to date' in pull:
        pass
    elif 'fatal:' in pull:
        print(f'{ve}Atualizações não verificadas. Conecte-se a internet')
        sleep(2)
    else:
        os.system('python Persux.py')
        exit()
    os.system('rm -rf pull')
