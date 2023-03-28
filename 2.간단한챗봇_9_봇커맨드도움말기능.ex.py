'''
- 봇커맨드-도움말 기능
  - 이모지 여러 개 생산 함수 추가
- 이모지피디아 https://blog.emojipedia.org/
- 서버주소 http://132.226.233.146/cdn/   
- 미션
'''
import discord
from discord.ext import commands
from datetime import datetime
import random 

# 봇명령객체와 접두어 설정하기
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='아토봇 ', intents=intents) 

@bot.event
async def on_ready():
    print('#'*80)
    print(f"{bot.user.name}의 서비스가 시작됩니다. ---")
    print(f"봇 정보: {bot.user.name}(id:{bot.user.id})")
    print(f"서비스 시작시간:{ datetime.now()}")
    print('#'*80)

# 사용법 : 아토봇 hello
@bot.command()
async def hello(ctx):
    author = ctx.author.name
    await ctx.send(f"안녕하세요. {author}님")


##################################################
# 챗봇의 도움말을 출력하는 기능 만들기
# 사용법 : 아토봇 도움말
# 아래에 코드를 작성하시오.
##################################################




import config 
bot.run( config.TOKEN)