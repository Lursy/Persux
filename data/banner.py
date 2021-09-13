from Persux.data.ferramentas import *
from Persux.data.menu import *


def banner():
    while True:
        rsenha = snick = name = 'error'
        rcor = open('.Cor', 'r').read()
        vs = os.path.exists('.Senha')
        vn = os.path.exists('.Nick')
        if vs:
            rsenha = open('.Senha', 'r').read()
        if vn:
            print(ban_sen)
            ban_exists = str(input(f'{am}//: {br}'))
            if ban_exists == '1':
                clear()
                pass
            elif ban_exists == '2':
                os.system('rm -rf .Nick')
                os.system('rm -rf bash.bashrc')
                with open('bash.bashrc', 'w') as bash:
                    bash.write(f'{inicio}\n' + f'\n{rsenha}\n{rcor}' if vs
                               else f'{rcor}' + f'{final}')
                print(f'{vd}!Sucess!')
                sleep(1)
                break
            elif ban_exists == '3':
                clear()
                break
            else:
                print(f'{ve}{ban_exists} não é um comando')
                sleep(2)
                break
        os.system('clear')
        print(bannerf)
        nick = str(input(f'{am}Nick: {br}'))
        clear()
        print(f"{rx}{figlet.renderText('Styles')}")
        styles()
        print(f'{vd}[i] {br}formatação do banner\n')
        int_styles = str(input(f'\n{am}//: {br}'))
        tstyle = [figlet, poison, lean, block, alligator, cosmic, rozzo, sblood, larry3d]
        for c, item in enumerate(tstyle):
            if int_styles == f'{c+1}':
                name = item.renderText(f'{nick}')
        if name == 'error':
            print(f'{ve}Comando não identificado!')
            sleep(2)
            break
        clear()
        sleep(1)
        print(f'{vd}\nbanner selecionado\n\n{br}{name}')
        sleep(2)
        with open('banner', 'w') as sbanner:
            sbanner.write(f'{name}'.rstrip().lstrip())
        clear()
        print(f"{az}{figlet.renderText('Cores')}")
        cor()
        print(f'{vd}[i] {br}cor do banner\n')
        cor_name = str(input(f'\n{am}//: {br}'))
        cor_banner = '''echo -e '\e[0;:corm'
cat /data/data/com.termux/files/usr/etc/banner
echo -e '\e[m\\n\\n' '''
        for c in range(0, 8):
            if cor_name == f'{c+1}':
                if c != '8':
                    snick = cor_banner.replace(':cor', f'3{c+1}')
                else:
                    break
        if cor_name.lower() == 'lursy':
            snick = f"cat /data/data/com.termux/files/usr/etc/banner|lolcat && echo -e '\\n\\n'"
        if snick == 'error':
            print(f'{ve}{cor_name} não é um comando!')
            sleep(2)
            break
        os.system('rm -rf bash.bashrc')
        nick_file = open('.Nick', 'w')
        nick_file.write(f'{snick}')
        nick_file.close()
        rnick = open('.Nick', 'r').read()
        bash = open('bash.bashrc', 'w')
        bash.write(f'{inicio}\n{rsenha}\n{rnick}\n{rcor}\n{final}'if vs
                   else f'{inicio}\n{rnick}\n{rcor}\n{final}')
        bash.close()
        print(f'{vd}!Sucess!')
        sleep(1)
        break
