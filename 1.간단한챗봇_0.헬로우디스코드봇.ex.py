'''
- 디스코드 최신버전 설치, 1.X와 2.X의 차이가 큼.
$ pip install -U discord.py 

- 디스코드봇을 사용해 보기 
'''
import discord
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
# 디스코드봇 생산하기 
# client == 디스코드봇 
client = discord.Client(intents=intents)



async def on_ready():
    pass


TOKEN = ''  
client.run( TOKEN)