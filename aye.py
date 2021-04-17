import subprocess
from pexpect import popen_spawn
import datetime
import requests
import random
from typing import Any, Text
import os
import vk_api
from random import choice
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk = vk_api.VkApi(token="ac9d7b06c80596084a3d26b4e64954a03a227aaeae0e0fee0e5f71886d57d8dfe53c2d85877d6239d1292")  # Токен твоего бота
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, 202656188) # ID Сообщества

def send_msg(peer_id: int, message: str = "", attachment: str = ""):
    return vk.method("messages.send", {**locals(), "random_id": 0})


while True:        
    try:        
        for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:     
                        peer_id = event.message.peer_id
                        user_id = event.message.from_id
                        text = event.message.text
                        if event.message.text == "/сайт_рестарт": # С чего начинается команда
                            send_msg(peer_id, message=(f"Перезапускаю NikoSite"))
                            user = 'Nikoscocos'
                            password = 'fursiNik0819'

                            cmd = "cd C:\\Users\\User\\Desktop\\NikoBot\\NikoSite\\nikosite.github.io\\nikosite.github.io"
                            returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix

                            cmd = "git add ." 
                            subprocess.call(cmd, shell=True)

                            cmd = 'git commit -m "Added Posts"'
                            subprocess.call(cmd, shell=True)
                            send_msg(peer_id, message=(f"Перезагрузка постов"))
                            cmd = "git remote set-url origin https://github.com/Nikoscocos/nikosite.github.io"
                            subprocess.call(cmd, shell=True)

                            cmd = "git push "
                            child_process = popen_spawn.PopenSpawn(cmd)
                            child_process.sendline(user)
                            child_process.sendline(password)
                            print('returned value:', returned_value)
                            send_msg(peer_id, message=(f"Сайт перезагружен! Обновления установлены."))
                            print('end of commands')

    except Exception as e:
        print(repr(e)) # Спаситель бота