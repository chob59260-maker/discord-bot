import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "봇이 정상적으로 작동 중입니다!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'성공적으로 로그인했습니다: {bot.user.name}')
    game = discord.Game("!유저정보 | !유튜브")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def 핑(ctx):
    await ctx.send(f'퐁! 응답 속도: {round(bot.latency * 1000)}ms')

@bot.command()
async def 안녕(ctx):
    await ctx.send(f'{ctx.author.name}님, 안녕하세요! 뉴비 봇입니다.')

@bot.command()
async def 주사위(ctx):
    import random
    result = random.randint(1, 6)
    await ctx.send(f'🎲 주사위를 굴려 {result}이(가) 나왔습니다!')

@bot.command()
async def 유튜브(ctx):
    await ctx.send("📺 유튜브 사이트 바로가기: https://www.youtube.com")

@bot.command()
async def 유저정보(ctx):
    user = ctx.author
    embed = discord.Embed(title=f"👤 {user.name}님의 정보", color=discord.Color.blue())
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.add_field(name="이름", value=user.name, inline=True)
    embed.add_field(name="태그", value=f"#{user.discriminator}", inline=True)
    embed.add_field(name="아이디(ID)", value=user.id, inline=False)
    embed.add_field(name="계정 생성일", value=user.created_at.strftime('%Y-%m-%d'), inline=True)
    await ctx.send(embed=embed)

if __name__ == "__main__":
    keep_alive()
    token = os.environ.get('DISCORD_TOKEN')
    if token:
        bot.run(token)
    else:
        print("에러: DISCORD_TOKEN 환경 변수를 찾을 수 없습니다.")
