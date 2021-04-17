import datetime
import random
from random import randint
import asyncio

t = datetime.datetime.now()
s = t.strftime('%m.%d.%Y %H:%M:%S.%f')
curtime =  s[:-10]
print(curtime)