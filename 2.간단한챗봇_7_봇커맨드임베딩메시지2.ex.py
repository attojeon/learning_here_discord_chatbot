'''
- 주사위 함수사용연습 추가
- 봇커맨드-임베딩메시지 사용하기 
- 미션
  - 가위바위보 랜덤출력하기 
  - 서버주소 http://learnsteam.kr/cdn/   
  - 파일이름들 kawi.png, bawi.png, bo.png 사용
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
# dice_info() 함수를 만들어서 주사위를 던지고,
# 던진 주사위의 수와 이미지를 리턴하는 함수를 만들어보세요.
# 사용법 : 아토봇 주사위
# 아래에 코드를 작성하시오.
##################################################






def dice_info():
    d = random.randint(1, 6)
    d_img = 'dice' + str(d) + '.png'
    d_url= 'http://learnsteam.kr/cdn/' + d_img
    print(d_url)

    return (d, d_url)


TOKEN = ''  
bot.run( TOKEN)