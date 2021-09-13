from data.ferramentas import figlet, sleep
from data.cores_persux import *


def cor():
    print(f'{ve}┏━━━━━━━━━━━━━━━━━━━┓')
    tools_cor = ['Vermelho', 'Verde', 'Amarelo', 'Azul', 'Rosa', 'Ciano', 'Branco', 'Voltar']
    sleep(0.01)
    for c, item in enumerate(tools_cor):
        print(f' {am}[ {c+1} ] {br}-{cy} {item}')
        sleep(0.01)
    print(f'{ve}┗━━━━━━━━━━━━━━━━━━━┛')


def styles():
    print(f'{ve}┏━━━━━━━━━━━━━━━━━━━┓')
    sleep(0.01)
    tools_style = ['comum', 'poison', 'lean', 'block', 'alligator', 'cosmic', 'rozzo', 'sblood', 'larry3d']
    for c, item in enumerate(tools_style):
        print(f' {am}[ {c+1} ] {br}-{cy} {item}')
        sleep(0.01)
    print(f'{ve}┗━━━━━━━━━━━━━━━━━━━┛')


ban_sen = f'''{ve}┏━━━━━━━━━━━━━━━━━┓
  {am}[ 1 ] {br}-{cy} alterar
  {am}[ 2 ] {br}-{cy} remover
  {am}[ 3 ] {br}-{cy} voltar
{ve}┗━━━━━━━━━━━━━━━━━┛'''

menu_nome = f'''{ve}┏━━━━━━━━━━━━━━━━━━━━━━┓
  {am}[ 1 ] {br}-{cy} alterar nome
  {am}[ 2 ] {br}-{cy} voltar
{ve}┗━━━━━━━━━━━━━━━━━━━━━━┛'''

# Figlet
persuxf = f"{rx}{figlet.renderText('Persux')}"
coresf = f"{az}{figlet.renderText('Cores')}"
bannerf = f"{ve}{figlet.renderText('Banner')}"
senhaf = f"{vd}{figlet.renderText('Senha')}"
