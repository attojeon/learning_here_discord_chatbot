'''
- 봇커맨드-이모지 보내기
- 이모지피디아 https://blog.emojipedia.org/
- 서버주소 http://learnsteam.kr/cdn/   
- 미션
  - 동물 이모지 사용해 보기 
  - 사람/로봇 이모지 사용해 보기 
'''
import discord
from discord.ext import commands
from datetime import datetime
import random, config

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
# 이모지를 사용하는 커맨드를 만들어보세요.
# 사용법 : 아토봇 주사위
# 아래에 코드를 작성하시오.
##################################################





def dice_info():
    d = random.randint(1, 6)
    d_img = 'dice' + str(d) + '.png'
    d_url= 'http://learnsteam.kr/cdn/' + d_img
    print(d_url)

    return (d, d_url)


# TOKEN을 config.py 파일에 저장하고, import config 를 하여 사용합니다.
bot.run( config.TOKEN)