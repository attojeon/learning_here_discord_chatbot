import discord
from discord.ext import commands
from datetime import datetime

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

# 사용법 : /hello
# 간단한 인사와 인사한 작자의 이름을 보여줌 
@bot.command()
async def hello(ctx):
    username = ctx.author.name
    await ctx.send(f"안녕하세요. {username}님")


##################################################
# 유저에게 간단하게 인사를 하는 커맨드 
# 사용법 : 아토봇 주사위 3 
#   주사위 수: 6,
#   주사위 수: 1,
#   주사위 수: 5,
# 
# 아래에 코드를 작성하시오.
##################################################




import random 
def play_dice():
    d = random.randint(1, 6)
    msg = '주사위 수: ' + str(d)
    return msg

def play_sci():
    d = random.choice(['가위','바위','보'])
    return f'가위바위보: {d}'



TOKEN = ''  
bot.run( TOKEN)