# 幫你寫好預設的class架構了

import discord
from discord.ext import commands
from core.classes import Cog_Extension

class PUTNAMEHERE(Cog_Extension):
    pass


async def setup(bot):
    await bot.add_cog(PUTNAMEHERE(bot))