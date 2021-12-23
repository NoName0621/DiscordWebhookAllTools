#coding: UTF-8
import requests
import json
from colored import fg, bg
import os 

os.system("cls")

#color
white = fg("white") 
red = fg("red")
green = fg("green")
orchid = fg("orchid")



while True:
    print(red + """

▒█░░▒█ █▀▀ █▀▀▄ █░░█ █▀▀█ █▀▀█ █░█ 
▒█▒█▒█ █▀▀ █▀▀▄ █▀▀█ █░░█ █░░█ █▀▄ 
▒█▄▀▄█ ▀▀▀ ▀▀▀░ ▀░░▀ ▀▀▀▀ ▀▀▀▀ ▀░▀                                
    """ + white)

    message = input(orchid +"MESSAGE TO BE SENT = " + green)
    icon = input(orchid +"ICON TO BE SENT = " + green)
    username = input(orchid +"NAME TO BE SENT = " + green)


    webhook_url = webhook
 
    main_content = {
       "username":  username,
       "avatar_url": icon,
       "content": message
       }
    requests.post(webhook_url,main_content)
    os.system("cls")
