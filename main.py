import discord
import os
from discord.ext import commands

TOKEN = os.environ.get('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'성공: {bot.user.name} 봇이 켜졌습니다!')

@bot.command()
async def 안녕(ctx):
    await ctx.send('반가워요!')

if TOKEN:
    bot.run(TOKEN)
else:
    print("에러: 토큰 설정이 안 되어 있습니다.")
