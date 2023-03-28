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

@client.event
async def on_ready():
    print('#'*80)
    print(f"{client.user.name}의 서비스가 시작됩니다. ---")
    print(f"봇 정보: {client.user.name}(id:{client.user.id})")
    print(f"서비스 시작시간:{ datetime.now()}")
    print('#'*80)



async def on_message(message):
    pass

TOKEN = ''  
client.run( TOKEN)