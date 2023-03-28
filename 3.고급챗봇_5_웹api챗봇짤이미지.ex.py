'''
- 봇커맨드-웹api 사용-짤 이미지업로드
- 미션
  - 다른 종류의 짤 이미지를 추가해 보시오. 
'''
import discord
from discord.ext import commands
import json
import random
import datetime

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



##################################################
# 위의 json파일에서 가져온 links를 사용하여 
# 짤 이미지를 보여주는 아래의 커맨드를 완성하시오.
# 사용법 : 아토봇 짤 먹기, 아토봇 짤 놀기, 아토봇 짤 잠자기
# 아래에 코드를 작성하시오.
##################################################




import config 
bot.run(config.TOKEN)
