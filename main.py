import discord
from discord.ext import commands
from flask import Flask
import threading
import os

# 1. 가짜 웹 서버 설정 (Render의 포트 체크 통과용)
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    # Render가 주는 포트 번호를 자동으로 읽어옵니다.
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# 웹 서버를 백그라운드에서 실행
threading.Thread(target=run).start()

# 2. 디스코드 봇 설정
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'성공: {bot.user.name} 봇이 켜졌습니다!')

@bot.command()
async def 안녕(ctx):
    await ctx.send('반가워요!')

# Render 환경변수에 넣은 토큰 불러오기
TOKEN = os.environ.get('DISCORD_TOKEN')

if TOKEN:
    bot.run(TOKEN)
else:
    print("에러: DISCORD_TOKEN 환경 변수가 설정되지 않았습니다.")
