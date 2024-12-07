import discord 
from discord.ext import commands
from core.classes import Cog_Extension


class hello(Cog_Extension):

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'已載入「{__name__}」')

    @commands.hybrid_command
    async def hello(self, ctx):
        await ctx.send("Hello", ctx.author)


async def setup(bot):
    await bot.add_cog(hello(bot))