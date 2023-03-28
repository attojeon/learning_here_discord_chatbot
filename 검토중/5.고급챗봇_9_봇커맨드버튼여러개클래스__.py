'''
- 봇커맨드-버튼을 클래스로,... 아직 불충분함.
- 미션

- 검토해볼 것 : nextcord 
'''
import discord
from discord import ButtonStyle
from discord.ui import Button 
from discord.ext import commands
from datetime import datetime
import random 

# 봇명령객체와 접두어 설정하기
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='아토봇 ', intents=intents) 

class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="1번",style=discord.ButtonStyle.primary, custom_id='btn1')
    # 아래 입력값의 순서가 중요함. interaction, button의 순서가 바뀌면 작동안함. 
    async def button_1(self, interaction:discord.Interaction, button:discord.ui.Button):
        # await interaction.response.edit_message(content=f"This is an edited button response!")
        await interaction.response.send_message(content=f"btn_id:{button.custom_id}")
    @discord.ui.button(label="2번",style=discord.ButtonStyle.primary, custom_id='btn2')
    async def button_2(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(content=f"btn_id:{button.custom_id}")
    @discord.ui.button(label="3번",style=discord.ButtonStyle.primary, custom_id='btn3')
    async def button_3(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(content=f"btn_id:{button.custom_id}")
    @discord.ui.button(label="4번",style=discord.ButtonStyle.primary, custom_id='btn4')
    async def button_4(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(content=f"btn_id:{button.custom_id}")

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

@bot.command(aliases=['사지선택','button'])
async def playbutton(ctx):
    view=Buttons()
    await ctx.send(":game_die: 번호를 선택하세요.",view=view)


def dice_info():
    d = random.randint(1, 6)
    d_img = 'dice' + str(d) + '.png'
    d_url= 'http://132.226.233.146/cdn/' + d_img
    print(d_url)

    return (d, d_url)
def desc_gen(emoji, cnt):
    msg = ''
    for _ in range(cnt):
        msg += emoji + ' '
    return msg 


TOKEN = 'ODQxMjQ0MDU0NTc0NTk2MTI4.GEPkvq.DrX8DUkJ7p2GB1Muuk6E9qrPk2HS-MfAVEor58'  
bot.run( TOKEN)