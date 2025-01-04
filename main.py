import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import time

# 載入 .env (or configs)
load_dotenv()

TOKEN = os.getenv('TOKEN')
online_text = os.getenv('ONLINE_TEXT')

# 預設Bot權限
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='[', intents=intents)

#上線通知
@bot.event
async def on_ready():
    now = time.strftime("%Y/%m/%d %H:%M:%S")
    game = discord.Game(f"{online_text}\n上線時間: {now}")
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.online, activity=game)
    try:
        synced_bot = await bot.tree.sync()
        print(f'Synced {len(synced_bot)} commands.')
    except Exception as e:
        print("出錯 when synced: ", e)
    print(f'Bot名稱: 「{bot.user}」\n上線時間: 「{now}」\n')
    print('我上線了窩\n')


async def load():
    for filename in os.listdir('./cmds'):
        try:
            if filename.endswith('.py'):
                await bot.load_extension(f'cmds.{filename[:-3]}')
                print(f'嘗試載入cmds.{filename}')
        except Exception as e:
            print(f'出錯 When loading extension: {e}')
    
        
async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)

asyncio.run(main())