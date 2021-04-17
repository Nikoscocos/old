import datetime
import random
from random import randint
import asyncio

t = datetime.datetime.now()
s = t.strftime('%m.%d.%Y в %H:%M:%S.%f')
curtime =  s[:-10]

bar = open('forum.html', 'a', encoding='utf-8')
bar.write('\n<div class="title">')
bar.write(f"\n<div>Автор: Никита Фурсенко. Выложено: {curtime}</div>")
bar.write(f"\n<h5>привет</h5> \n</div>")
bar.close()

