import discord
import os
from discord.ext import commands

# Render 환경 변수에서 토큰 가져오기
TOKEN = os.environ.get('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'봇 로그인 성공: {bot.user.name}')

@bot.command()
async def 안녕(ctx):
    await ctx.send('정상 작동 중입니다!')

if TOKEN:
    bot.run(TOKEN)
else:
    print("에러: DISCORD_TOKEN을 찾을 수 없습니다.")
