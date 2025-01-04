import discord 
from discord.ext import commands
from core.classes import Cog_Extension
from datetime import datetime

'''我現在只在這裡放了hello跟ping指令'''

class hello(Cog_Extension):

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'已載入「{__name__}」')

    @commands.hybrid_command
    async def hello(self, ctx):
        await ctx.send("Hello", ctx.author)

    @commands.hybrid_command
    async def ping(self, ctx):
        embed = discord.Embed(
        color=discord.Color.red(), 
        title="延遲", 
        description=f'**{round(self.bot.latency*1000)}** (ms)', 
        timestamp=datetime.now()
        )

        await ctx.send(embed = embed)


async def setup(bot):
    await bot.add_cog(hello(bot))