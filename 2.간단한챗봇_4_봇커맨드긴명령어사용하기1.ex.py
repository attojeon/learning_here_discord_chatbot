'''
- 봇커맨드 사용하기 
- 커맨드 긴 명령법
  $ 아토봇 주사위 3 => 주사위수: 5, 6, 4,
- 미션:
  - 가위바위보 대결하기 
  - 두 칸 띄워쓰기의 에러 방지하기 
  - 사칙연산하는 봇 만들기 
'''

import discord
from discord.ext import commands
from datetime import datetime

# 봇명령객체와 접두어 설정하기
intents = discord.Intents.default()
intents.message_content = True
##################################################
# 커맨드와 접두어를 사용하기 위한 코드를 작성하시오. 
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
# 입력이 여러 개를 할 수 있는 명령어 만들기
# 사용법 : /아토봇 주사위 3 
# 아래에 코드를 작성하시오.
##################################################




TOKEN = ''  
bot.run( TOKEN)

