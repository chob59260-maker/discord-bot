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

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'성공적으로 로그인했습니다: {bot.user.name}')
    game = discord.Game("정상 작동 중!")
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

if __name__ == "__main__":
    keep_alive()
    token = os.environ.get('DISCORD_TOKEN')
    if token:
        bot.run(token)
    else:
        print("에러: DISCORD_TOKEN 환경 변수를 찾을 수 없습니다.")
