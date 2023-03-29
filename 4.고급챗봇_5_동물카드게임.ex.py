import discord
from discord.ext import commands
from datetime import datetime
import config, random

# 봇명령객체와 접두어 설정하기
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='아토봇 ', intents=intents) 

# animals = ["cat.png", "mouse.png", "hippo.png", "monkey.png", "elephant.png", "giraffe.png"] 

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


##################################################
# 버튼이 여러 개인 경우를 구현해서 사용자와 암산게임을 만듭니다. 
# 사용법 : 아토봇 암산게임
# 아래에 코드를 작성하시오.
#   - 콜백함수의 interaction 매개변수를 사용하면,
#   - interaction.data['custom_id'] 를 사용해서 사용자가 선택한 버튼의 custom_id를 알 수 있습니다.
#   - interaction.data['values'] 를 사용해서 사용자가 선택한 버튼의 value를 알 수 있습니다.
#   - interaction.data['component_type'] 를 사용해서 사용자가 선택한 버튼의 component_type을 알 수 있습니다.
#   - interaction.data['label'] 를 사용해서 사용자가 선택한 버튼의 label을 알 수 있습니다.
##################################################


@bot.command(aliases=['동물카드','animalcard'])
async def playbutton(ctx):
    animals = ["cat.png", "mouse.png", "hippo.png", "monkey.png", "elephant.png", "giraffe.png"] 
    def pick_animal():
        picked_animal = random.choice(animals)
        return picked_animal

    def build_4_animals(picked):
        others = animals.copy()
        others.remove(picked)
        animals_4 = random.sample(others, 3)
        animals_4.append(picked)

        return animals_4

    def convert_q_to_embed(picked):
        embed = discord.Embed(title="동물사진", description="그림에 보이는 동물의 이름을 고르시오.", color=0x00ff00)
        embed.set_image(url=f"http://learnsteam.kr/cdn/{picked}")
        return embed

    # 파일이름을 한글라벨로 변환하기
    def display_label(animal):
        pass


    # 버튼을 눌렀을 때의 콜백함수
    async def check_answer(interaction):
        user_ans = interaction.data['custom_id']
        if user_ans == picked_animal:
            await interaction.response.send_message("정답입니다", ephemeral=True)
        else:
            await interaction.response.send_message("오답입니다", ephemeral=True)


    # 동물카드문제를 위한 자료구조 정리하기 
    picked_animal = pick_animal()
    suggestions = build_4_animals(picked_animal)
    random.shuffle(suggestions)
    # 동물카드문제를 embed로 변환하기
    embeding_msg = convert_q_to_embed(picked_animal)
    # 동물카드문제를 유저에게 보내기
    await ctx.send(embed = embeding_msg, ephemeral=True)

    #############################################
    # 버튼을 만들어서 view에 추가하는 코드를 작성하시오. 
    #############################################
    view = discord.ui.View() 

    
    # 유저에게 문제 제출하기 
    await ctx.send("동물카드에 보이는 동물의 이름을 고르시오.", view=view, ephemeral=True)  


bot.run( config.TOKEN)