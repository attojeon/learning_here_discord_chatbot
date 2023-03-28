'''
- 챗봇으로 게임액션 흉내내기
- client와 on_message를 사용하여 채팅하기 
- 접두어로 봇명령 구분하기 
'''
import discord
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('#'*80)
    print(f"{client.user.name}의 서비스가 시작됩니다. ---")
    print(f"봇 정보: {client.user.name}(id:{client.user.id})")
    print(f"서비스 시작시간:{ datetime.now()}")
    print('#'*80)


# 코드를 작성해 보시오. 
async def on_message(message):
    pass 

import random 
def play_dice():
    pass

def play_sci():
    pass 

TOKEN = ''  
client.run( TOKEN)