#coding: UTF-8
import requests
import json
from colored import fg, bg
import os
import sys
import json
import random
import threading
from threading import Thread
import time


os.system("cls")

json_file = open('config.json', 'r')
json_data = json.load(json_file)

#color
white = fg("white")
red = fg("red")
green = fg("green")
orchid = fg("orchid")

fgwhite = fg("white")
fgred = fg("red")
fggreen = fg("green")
fgblack = fg("black")
fgplum = fg("plum_3")
fggreen_3b = fg("green_3b")
fgblue_violet = fg("blue_violet")
fglight_red = fg("light_red")
fgcyan = fg("cyan")
light_yellow = fg("light_yellow")
pink_3 = fg("pink_3")

bgwhite = bg("white")
bgred = bg("red")
bggreen = bg("green")
bgblack = bg("black")




os.system("mode con cols=100 lines=25")



proxies = json_data["proxies"]
proxy = {
    "https":proxies,
    "http":proxies
    }



webhook = input(green +"WebHook PLZ > ")




title = (green + """
                             __    __     _                       _    
                            / / /\ \ \___| |__   /\  /\___   ___ | | __
                            \ \/  \/ / _ \ '_ \ / /_/ / _ \ / _ \| |/ /
                             \  /\  /  __/ |_) / __  / (_) | (_) |   < 
                              \/  \/ \___|_.__/\/ /_/ \___/ \___/|_|\_\
""" + white)




def main():
    os.system('cls')
    print(title)
    print(f"""
                    {green}________________________________________________________{green}
                    {green}|                                                       {green}|
                    {green}|     {red}[01]{orchid}WebHook Spam         {red}[02]{orchid}WebHook Messege      {green}|
                    {green}|                                                       {green}|
                    {green}|     {red}[03]{orchid}WebHook Remove                                {green}|
                    {green}|                                                       {green}|
                    {green}|                                                       {green}|
                    {green}|                                                       {green}|
                    {green}|_______________________________________________________{green}|
        """)

    global choice
    choice = input(">")
    
    if choice == '1' or choice == '01':
        os.system('cls')
        exec(open('File/1_webhook/webhook.py').read())

    elif choice == '2' or choice == '02':
        os.system('cls')
        exec(open('File/2_Messege/Messege.py').read())

    elif choice == '3' or choice == '03':
        os.system('cls')
        global choice3
        print(f'''{green}Are you sure you want me to delete it?

{fggreen_3b}yes [1]
{red}No  [2]
              ''')
        choice3 = input(f"{green}>")
        if choice3 == '1':
            Del = requests.delete(webhook,proxies=proxy)
            if Del.ok:
                print(f'''{green}Deleted.
Close the software after three seconds.''')
                time.sleep(3)
                sys.exit
            else:
                print(f'''{green}I couldn't delete it.
Close the software after three seconds.''')
                time.sleep(3)
                sys.exit
        elif choice3 == '2':
            main()
    else:
        os.system('cls')
        main()


main()