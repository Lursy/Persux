import os
from time import sleep
from pyfiglet import Figlet


inicio = '''shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

PROMPT_DIRTRIM=2'''


alligator = Figlet(font='alligator')
larry3d = Figlet(font='larry3d')
poison = Figlet(font='poison')
sblood = Figlet(font='sblood')
lean = Figlet(font='lean')
block = Figlet(font='block')
cosmic = Figlet(font='cosmic')
rozzo = Figlet(font='rozzo')
figlet = Figlet()


user = open('.usuario', 'r').readline()

cor_letra = f'''PROMPT_DIRTRIM=2
PS1='\[\e[0;31m\]┏(\[\e[0;34m\]{user}\[\e[0;31m\]) [\[\e[0;32m\]\w\[\e[0;31m\]] \\n\[\e[0;31m\]┗► \[\e[1;:corm\]'
'''

final ='''if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
'''


def clear():
    os.system('clear')
