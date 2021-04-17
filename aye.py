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
                        if event.message.text.startswith("/пост "): # С чего начинается команда
                            post = event.message.text[6:]
                            idrand = user_id
                            user = vk.method("users.get", {"user_ids": f"{idrand}"}) # вместо 1 подставляете айди нужного юзера
                            fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']
                            t = datetime.datetime.now()
                            s = t.strftime('%H:%M:%S.%f %m.%d.%Y')
                            curtime = s[:-10]

                            bar = open('forum.html', 'a', encoding='utf-8')
                            bar.write('\n<div class="title">')
                            bar.write(f"\n<div>Автор: {fullname}. Выложено в: {curtime}</div>")
                            bar.write(f"\n<h5>{post}</h5> \n</div>")
                            bar.close()

                            user = 'Nikoscocos'
                            password = 'fursiNik0819'

                            cmd = "cd C:\\Users\\User\\Desktop\\NikoBot\\NikoSite\\nikosite.github.io\\nikosite.github.io"
                            returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix

                            cmd = "git add ." 
                            subprocess.call(cmd, shell=True)

                            cmd = 'git commit -m "Added Posts"'
                            subprocess.call(cmd, shell=True)
                            send_msg(peer_id, message=(f"Публикую ваш пост..."))
                            cmd = "git remote set-url origin https://github.com/Nikoscocos/nikosite.github.io"
                            subprocess.call(cmd, shell=True)

                            cmd = "git push "
                            child_process = popen_spawn.PopenSpawn(cmd)
                            child_process.sendline(user)
                            child_process.sendline(password)
                            print('returned value:', returned_value)
                            send_msg(peer_id, message=(f"Ваш пост опубликован! \nНе забывайте, что оскорбления на сайте караются баном в боте! \nВаш пост размещён на: https://nikoscocos.github.io/nikosite.github.io/forum.html"))
                            print('end of commands')
    except Exception as e:
        print(repr(e)) # Спаситель бота