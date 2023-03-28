'''
- 봇커맨드-반복작업시키기 
- 이미지 가져오기 (animals, architecture, natur, people, tech, grayscale, sepia)
- 미션
'''
import discord
from discord.ext import commands
import requests
import json
import random
import datetime
import asyncio, io
import config 

# 봇명령객체와 접두어 설정하기
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='아토봇 ', intents=intents)
links = json.load(open("gifs.json"))


@bot.event
async def on_ready():
    print('#'*80)
    print(f"{bot.user.name}의 서비스가 시작됩니다. ---")
    print(f"봇 정보: {bot.user.name}(id:{bot.user.id})")
    print(f"서비스 시작시간:{ datetime.datetime.now()}")
    print('#'*80)
    await schedule_daily_message()




##################################################
# 주기적으로 메시지를 보내는 챗봇 커맨드를 만들어 보시오.
# 사용법 : 
# 아래에 코드를 작성하시오.
# 채널ID는 config.py에 있는 CHANNEL_ID를 사용할 수 있게 저장하시오. 
# 디스코드웹의 url 마지막 19자리 숫자가 채널ID이다.
##################################################




bot.run(config.TOKEN)
