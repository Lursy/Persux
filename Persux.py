from data.install import *

print("\033[H\033[2J\033[3J") # Clear the screen
atualizar = input("Deseja atualizar o repositório? [s/n]? ").strip().lower()
if atualizar == 's':
    git_pull()

os.chdir('/data/data/com.termux/files/usr/etc/')
usr = os.path.exists('.usuario')
install()

try:
   while True:
        from time import sleep
        from data.menu import *
        from data.ferramentas import *
        clear()
        if not usr:
            """
            In this case the user haven't run the script anytime yet
            """

            print(f'{cy}~Lursy: {vd}Olá...')
            sleep(1)
            print('        É sua primeira vez por aqui?')
            sleep(3.5)
            clear()
            print(f'{cy}~Lursy: {vd}Bem... ')
            sleep(1)
            print('        Seja bem vindo!!')
            sleep(2)
            print('        Esse é o menu, fique a vontade :D')
            sleep(1.4)
        print(persuxf.rstrip(), '2.2\n\n')
        user = (open('.usuario', 'r')).readline()
        print(f'''{ve}┏━━━━━━━━━━━━━━━━━┓
  {am}[ 1 ] {br}-{cy} letra
  {am}[ 2 ] {br}-{cy} banner
  {am}[ 3 ] {br}-{cy} senha
  {am}[ 4 ] {br}-{cy} {user}
  {am}[ 5 ] {br}-{cy} Criador
  {am}[ 6 ] {br}-{cy} Sair
{ve}┗━━━━━━━━━━━━━━━━━┛
Me ajude a fazer novos scripts apoiando no PIX
{am}PIX: {vd}5c194b33-b6bf-4bab-91e4-26756c013560
''')
        menu = str(input(f'{am}//: {br}'))
        if not usr:
            print(f'{cy}~Lursy: {vd}Boa escolha!')
            sleep(1)
            usr = True

        """
        It's implemented a Object Literal rigjt down that has made for remove all unuseful conditionais. It also removes the boring task to change the code in two place when we wanna add a new funcionality in the future

        First we define the principal functions that will toggle among the possible imports, and later, we put them into a dict where for each key there's a lambda function that calls the functions declarated above
        """

        def importar_letra():
            from data.letra import letra
            letra()

        def importar_banner():
            from data.banner import banner
            banner()

        def importar_senha():
            from data.senha import senha
            senha()

        def importar_nome():
            from data.nome import nome_letra
            nome_letra()

        def open_url():
            os.system(f'termux-open-url https://www.youtube.com/channel/UCwmkiKIZHL1wscYHfIINZKw')
            clear()

        def sair():
            print(f'\n{vd}Saindo...')
            sleep(1)
            clear()
            exit()

        import_handler = {
            "1": lambda: importar_letra,
            "2": lambda: importar_banner,
            "3": lambda: importar_senha,
            "4": lambda: importar_nome,
            "5": lambda: open_url,
            "6": lambda: sair
                }
        try:
            import_handler[menu]()()
        except KeyError:
            print(f'{ve}Comando não reconhecido')
            sleep(1)

except KeyboardInterrupt: sair()
