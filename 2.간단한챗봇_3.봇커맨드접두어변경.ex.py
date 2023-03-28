'''
- 봇커맨드 사용하기 
- 접두어 변경하기 
- 미션
  - hello의 별명 추가하기 
'''

import discord
from discord.ext import commands
from datetime import datetime

# 봇명령객체와 접두어 설정하기
intents = discord.Intents.default()
intents.message_content = True

##################################################
# 커맨드의 접두어를 변경하기 위한 코드를 작성하시오. 
# 아래에 코드를 작성하시오.
##################################################


@bot.event
async def on_ready():
    print('#'*80)
    print(f"{bot.user.name}의 서비스가 시작됩니다. ---")
    print(f"봇 정보: {bot.user.name}(id:{bot.user.id})")
    print(f"서비스 시작시간:{ datetime.now()}")
    print('#'*80)


##################################################
# 유저에게 간단하게 인사를 하는 커맨드 
# 사용법 : /hello   /pladydice /playsci   /주사위   
#          /dice   /가위바위보
# 아래에 자기가 작성한 코드를 복붙해도 됩니다. 
##################################################



TOKEN = ''  
bot.run( TOKEN)