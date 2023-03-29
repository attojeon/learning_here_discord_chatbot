'''
- 봇커맨드-웹api 사용
  - requests, response 리뷰
- 미션
  - 이미지플래시 등의 사이트에서 가져오기 
'''
import discord
from discord.ext import commands
import requests
import datetime

# 봇명령객체와 접두어 설정하기
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='아토봇 ', intents=intents)

@bot.event
async def on_ready():
    print('#'*80)
    print(f"{bot.user.name}의 서비스가 시작됩니다. ---")
    print(f"봇 정보: {bot.user.name}(id:{bot.user.id})")
    print(f"서비스 시작시간:{ datetime.datetime.now()}")
    print('#'*80)


url = "https://dog.ceo/api/breeds/image/random"
##################################################
# 위의 api에서 받아온 image link를 챗봇에 전송하는 커맨드
# 사용법 : 아토봇 개, 아토봇 강아지, 아토봇 dog
# 아래에 코드를 작성하시오.
##################################################



import config
bot.run(config.TOKEN)
