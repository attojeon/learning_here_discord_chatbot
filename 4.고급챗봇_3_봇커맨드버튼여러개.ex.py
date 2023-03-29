'''
- 봇커맨드-버튼 여러개
- 미션

- 검토해볼 것 : nextcord 
'''
import discord
from discord.ext import commands
from datetime import datetime
import config

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
# 1. 명령어를 입력하면 버튼1, 버튼2가 출력되도록 하세요.
# 2. 버튼을 누르면 각각 '안녕1', '안녕2' 이라는 메시지가 출력되도록 하세요.
# 사용법 : 아토봇 버튼 
# 아래에 코드를 작성하시오.
##################################################



bot.run( config.TOKEN)