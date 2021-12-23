import threading
from threading import Thread
import os
import sys
import time
from colored import fg, bg, attr
import requests
import json
import random

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



os.system("cls")

def main():

    print(f"{fggreen_3b} ENTER NAME")
    name = input(fgblue_violet + " >" + fglight_red + " ")

    print(f"{fggreen_3b} ENTER ICON_URL")
    icon = input(fgblue_violet + " >" + fglight_red + " ")

    print(f"{fggreen_3b} ENTER SPAM")
    spam = input(fgblue_violet + " >" + fglight_red + " ")

    print(f"{fggreen_3b} ENTER MESSAGE")
    message = input(fgblue_violet + " >" + fglight_red + " ")

    os.system("cls")

    print(f"""
     {fggreen_3b}webhook {fglight_red}| {fgwhite}{webhook}
     {fggreen_3b}name        {fglight_red}| {fgwhite}{name}
     {fggreen_3b}icon        {fglight_red}| {fgwhite}{icon}
     {fggreen_3b}spam        {fglight_red}| {fgwhite}{spam}
     {fggreen_3b}message     {fglight_red}| {fgwhite}{message}
     {fggreen_3b}proxies     {fglight_red}| {fgwhite}{json_data["proxies"]}
     {fgplum}start?
    
     {fggreen_3b}1 {fglight_red}- {fgwhite}yes
     {fggreen_3b}2 {fglight_red}- {fgwhite}no
        """)

    ok2 = input(fgblue_violet + " >" + fglight_red + " ")
    if ok2 == "1":
        def webhook_spam(num):
            main_content = {
                "username": name ,
                "avatar_url":icon ,
                "content":f"{message} {random1}"
            }
            PROXIES = {'https': json_data["proxies"]}
            a = requests.post(webhook, main_content ,proxies=PROXIES)
            if a.ok:
                print (f'{fggreen_3b}OK')
            else:
                print (f'{fglight_red}NO')
        thread = []
        for i in range(int(spam)):
            random1 = random.seed()
            random1 = random.randint(100, 1000)
            Thread2 = threading.Thread(target=webhook_spam, args=(i,))
            Thread2.setDaemon(True)
            Thread2.start()
            time.sleep(0.5)


    elif ok2 == "2":
        os.system('cls')
        main()

    else:
        os.system('cls')
        main()

main()