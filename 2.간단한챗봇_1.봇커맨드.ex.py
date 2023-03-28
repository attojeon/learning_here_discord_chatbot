'''
- 봇커맨드 사용하기 
- 접두어로 봇명령 구분하기 
### 메시지 보내기 차이점 ###
- message.channel.send() VS ctx.send()
'''
import discord
from discord.ext import commands
from datetime import datetime

# 봇명령객체와 접두어 설정하기
intents = discord.Intents.default()
intents.message_content = True

##################################################
# 커맨드를 사용하기 위한 코드를 작성하시오. 
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
# 사용법 : /hello
# 아래에 코드를 작성하시오.
##################################################




TOKEN = ''  
bot.run( TOKEN)