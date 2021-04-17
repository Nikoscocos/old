import random
from random import randint
import asyncio

file = open('pizda.html', 'w', encoding='utf-8')
file.write('<!DOCTYPE html> \n<html> \n<head> \n<title>Posts</title> \n<style type="text/css"> \nbody { \n  background: url(wall4.png); \n}') 
style = open('pizda.html', 'a', encoding='utf-8')
style.write("\n.nav { \n   background-color:rgb(26, 84, 170); \n   margin-bottom: 10px; \n   height: 50px; \n   font-size:30px; \n   font-family: 'Segoe UI'; \n   font-weight: bold; \n} \n</style> \n</head> \n")
bar = open('pizda.html', 'a', encoding='utf-8')
bar.write('\n<body> \n<div class="nav"> \n<a href="index.html"><img src="иконка.jpg" style="padding-left: 0px; padding-top: 0px;" border="0" height="37" width="42"/></a> \n<a href="updates.html">Updates</a> \n<a href="about.html">NikoBot</a> \n<a href="http://vk.com/nikoscocos_api">VK</a> \n<a href="https://discord.com/oauth2/authorize?client_id=807540667294154763&scope=bot&permissions=0">Discord</a> \n</div>')