import discord
from discord.ext import commands
from datetime import datetime
import config

# 봇명령객체와 접두어 설정하기
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='아토봇 ', intents=intents) 

clicked = 0

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
# 1. 명령어를 입력하면 버튼이 출력됩니다.
# 2. 버튼을 클릭할 때마다 '안녕1', '안녕2'... 이라는 메시지가 출력
# 사용법 : 아토봇 버튼
# 버튼은 반드시 콜백함수를 가지고 있어야 합니다.
#   - 콜백함수는 사용자가 버튼을 누르면 실행됩니다.
#   - 콜백함수는 async def 로 정의되어야 합니다.
#   - 콜백함수는 interaction 이라는 인자를 받아야 합니다.
#   - 콜백함수는 interaction.response.send_message() 를 사용하여 메시지를 출력합니다.
##################################################


bot.run( config.TOKEN)