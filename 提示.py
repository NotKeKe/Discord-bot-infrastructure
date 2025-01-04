import discord
from discord.ext import commands
from discord import app_commands

'''
有些時候會用到這些指令
from discord.app_commands import Choice
'''

'''預設的指令狀態'''
# 狀態1 ， 只能使用預設的前綴
@commands.command()
async def PutYourCommandName(self, ctx):
    await ctx.send('MESSAGE')

# 狀態2 ， 只能使用斜線(slash)指令
@app_commands(name='NAME', description='DISCRIPTION')
async def PutYourCommandName(self, interaction: discord.Interaction):
    await interaction.response.send_message('MESSAGE')

# 狀態3 ， 能使用預設前綴和斜線指令
@commands.hybrid_command(name='NAME', description='DESCRIPTION')
async def PutYourCommandName(self, ctx):
    await ctx.send('MESSAGE')



'''embed預設'''
embed=discord.Embed(title="title", description="description", color=0xff0000)
embed.set_author(name="name", url="url", icon_url="icon")
embed.set_thumbnail(url="thumbnail")
embed.add_field(name="field", value="value", inline=False)
embed.set_footer(text="footer")
await ctx.send(embed=embed)

# 載入 .env (or configs)
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv('TOKEN')
online_text = os.getenv('ONLINE_TEXT')