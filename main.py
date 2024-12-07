import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands
import json
import os
import asyncio
import time

#setting.json aka config
with open('config.json', 'r', encoding = 'utf8') as jfile:
        #(檔名，mode=read)
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='[', intents=discord.Intents.all())

#上線通知
@bot.event
async def on_ready():
    now = time.strftime("%Y/%m/%d/ %H:%M:%S")
    game = discord.Game(f"{jdata["online_text"]}\n上線時間: {now}")
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.online, activity=game)
    try:
        synced_bot = await bot.tree.sync()
        print(f'Synced {len(synced_bot)} commands.')
    except Exception as e:
        print("出錯 when synced: ", e)
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
        await bot.start(jdata['TOKEN'])

asyncio.run(main())