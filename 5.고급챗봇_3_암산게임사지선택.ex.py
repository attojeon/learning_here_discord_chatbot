'''
- 봇커맨드-버튼 여러개
- 미션

- 검토해볼 것 : nextcord 
'''
import discord
from discord.ext import commands
from datetime import datetime
import config, random

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
async def myhello(ctx):
    author = ctx.author.name
    await ctx.send(f"안녕하세요. {author}님")


##################################################
# 교재를 보고, 버튼이 여러 개인 경우를 구현해서 사용자와 암산게임을 하게 만들어보세요.
# 사용법 : 아토봇 암산게임
# 아래에 코드를 작성하시오.
#   - 콜백함수의 interaction 매개변수를 사용하면,
#   - interaction.data['custom_id'] 를 사용해서 사용자가 선택한 버튼의 custom_id를 알 수 있습니다.
##################################################



bot.run( config.TOKEN)