import asyncio
from colorama.ansi import set_title
from pystyle import *
import os
import subprocess
from colorama import *
import time
from tkinter import filedialog, Tk
import sys
import webbrowser




os.system('clear' if os.name == 'posix' else 'cls')

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)



w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX

intro = """



 ██████╗███████╗██╗     ███████╗███████╗████████╗██╗ █████╗ ██╗     
██╔════╝██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██║██╔══██╗██║     
██║     █████╗  ██║     █████╗  ███████╗   ██║   ██║███████║██║        -by N0V0
██║     ██╔══╝  ██║     ██╔══╝  ╚════██║   ██║   ██║██╔══██║██║     
╚██████╗███████╗███████╗███████╗███████║   ██║   ██║██║  ██║███████╗
 ╚═════╝╚══════╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝
                                                                    

                                     
 

                > Press Enter                                         

"""

Anime.Fade(Center.Center(intro), Colors.blue_to_purple, Colorate.Vertical, interval=0.035, enter=True)

def main():
    set_title(f"")
    asc = asyncio.get_event_loop()
    clear = lambda: os.system('cls')
    clear()
    print(f"""{Fore.MAGENTA}


 ██████╗███████╗██╗     ███████╗███████╗████████╗██╗ █████╗ ██╗     
██╔════╝██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██║██╔══██╗██║     
██║     █████╗  ██║     █████╗  ███████╗   ██║   ██║███████║██║       -by N0V0
██║     ██╔══╝  ██║     ██╔══╝  ╚════██║   ██║   ██║██╔══██║██║     
╚██████╗███████╗███████╗███████╗███████║   ██║   ██║██║  ██║███████╗
 ╚═════╝╚══════╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝
                                                                    
        Celestial Deobfuscator Ready To Be Used

""")
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_blue, interval=0.000)
    print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
{b}|{Fore.RESET}{m}{m}[{w}1{Fore.RESET}{m}]{Fore.RESET} Grabber deobfuscator   {b}|{Fore.RESET}{m}[{w}3{Fore.RESET}{m}]{Fore.RESET} Info  
{b}|{Fore.RESET}{m}[{w}2{Fore.RESET}{m}]{Fore.RESET} Discord{Fore.RESET}                {b}|{Fore.RESET}{m}[{w}4{Fore.RESET}{m}]{Fore.RESET} Exit{Fore.RESET}''')
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_blue, interval=0.000)

    choice = input(f'{m}[{w}>{m}]{w} Choice?: ')

###################################################################################################################################################################################

    if choice == '1':
        Spinner()
        set_title(f"Deobfuscator")
        filename = input('Input Files name :')
        os.system(f'cmd /k "py deobf.py {filename}"')

    if choice == '2':
        Spinner()
        print('https://discord.gg/4rmtzuHu')
        exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = main()

    if choice == '3':
        webbrowser.open('https://github.com/N0Tpengu/Grabber-Deobfuscator/blob/main/readme.md')
        exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = main()


main()
        
	













