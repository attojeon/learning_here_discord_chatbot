'''
- gif 이미지를 보내기 
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


@client.event 
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'username: {username}, msg: {user_message}, channel: {channel}')

    if message.author == client.user:
        return

    # 코드를 작성하세요. 

    
TOKEN = ''  
client.run( TOKEN)