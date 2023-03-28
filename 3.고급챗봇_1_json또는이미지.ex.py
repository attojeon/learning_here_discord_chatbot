import discord
from discord.ext import commands
import requests
import config

# 봇명령객체와 접두어 설정하기
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='아토봇 ', intents=intents)


url="https://picsum.photos/seed/picsum/300/200"
##################################################
# 위의 url에서 이미지를 다운로드 받아서 디스코드에 출력하는 기능 만들기
# 사용법 : 아토봇 pic, 아토봇 사진, 아토봇 이미지
# 아래에 코드를 작성하시오.
##################################################




# 디스코드 봇 토큰을 config.py 파일에 저장해두고 불러오기
TOKEN = config.TOKEN 
bot.run(TOKEN)
