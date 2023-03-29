'''
- 봇커맨드-웹api 사용-이미지업로드
  - requests, response 리뷰
  - io.BytesIO( bytes...) 사용법???
- 미션
  - 픽사베이에서 이미지 가져오기(json + api key) 
'''
import discord
from discord.ext import commands
import requests
import datetime
import io, config

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



##################################################
# 사용법 : 아토봇 개, 아토봇 강아지, 아토봇 dog
# 아래에 코드를 작성하시오.
##################################################
@bot.command(aliases=['개', '강아지', 'dog'])
async def dog_image(ctx):
    url = "https://dog.ceo/api/breeds/image/random"
    


##################################################
# 사용법 : 아토봇 고양이, 아토봇 meow, 아토봇 cat
# 아래에 코드를 작성하시오.
##################################################
@bot.command(aliases=['고양이', 'meow'])
async def cat_image(ctx):
    url = "https://aws.random.cat/meow"
    

##################################################
# 사용법 : 아토봇 아무거나, 아토봇 picture
# 아래에 코드를 작성하시오.
# 이미지를 파일로 저장하지 않고, 이미지 바이너리를 챗봇으로 업로드하기
# 난이도가 높은 코드입니다.
##################################################
@bot.command(aliases=['아무거나', 'picture'])
async def any_image(ctx):
    url = "https://picsum.photos/200/300"
    

# 디스코드 봇 토큰을 config.py 파일에 저장해두고 불러오기
TOKEN = config.TOKEN 
bot.run(TOKEN)
