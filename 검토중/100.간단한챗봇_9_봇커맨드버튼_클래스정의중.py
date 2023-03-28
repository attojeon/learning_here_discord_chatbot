'''
- 봇커맨드-버튼
- 미션
'''
import discord
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


@bot.command(aliases=['버튼','button'])
async def playbutton(ctx):
    view=Buttons()
    # view.add_item(discord.ui.Button(label="URL Button",style=discord.ButtonStyle.link,url="https://github.com/lykn",emoji="<a:kannaWink:909791444661850132>"))
    await ctx.send("This message has buttons!",view=view)


TOKEN = 'ODQxMjQ0MDU0NTc0NTk2MTI4.GEPkvq.DrX8DUkJ7p2GB1Muuk6E9qrPk2HS-MfAVEor58'  
bot.run( TOKEN)