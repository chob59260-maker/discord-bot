import discord
import os
from discord.ext import commands

# Render에서 설정한 환경 변수 가져오기
TOKEN = os.environ.get('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'로그인 성공: {bot.user.name}')

@bot.command()
async def 안녕(ctx):
    await ctx.send('반가워요! 봇이 온라인입니다.')

if TOKEN:
    bot.run(TOKEN)
else:
    print("토큰을 찾을 수 없습니다. 환경 변수를 확인하세요.")
