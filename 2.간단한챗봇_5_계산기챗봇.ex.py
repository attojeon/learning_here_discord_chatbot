import discord
from discord.ext import commands
from datetime import datetime

# 봇명령객체와 접두어 설정하기
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents) 

@bot.event
async def on_ready():
    print('#'*80)
    print(f"{bot.user.name}의 서비스가 시작됩니다. ---")
    print(f"봇 정보: {bot.user.name}(id:{bot.user.id})")
    print(f"서비스 시작시간:{ datetime.now()}")
    print('#'*80)


##################################################
# 유저에게 간단하게 인사를 하는 커맨드 
# 사용법 : /add 10 20 =>두 수의 합을 말해줌
# 아래에 코드를 작성하시오.
##################################################


##################################################
# 유저에게 간단하게 인사를 하는 커맨드 
# 사용법 : /sub 10 20 =>두 수의 차를 말해줌
# 아래에 코드를 작성하시오.
##################################################


TOKEN = ''  
bot.run( TOKEN)