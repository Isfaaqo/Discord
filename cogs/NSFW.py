import discord
import random
from random import randint
from discord import client
from discord.ext import commands
bot = commands.Bot(command_prefix = '/')

# Cogs class.
class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # For Yuki.
    @commands.is_nsfw().command(aliases = ['nh',])
    async def nhentai(self, ctx, code=None):
        if not code:
            code = randint(0, 425000)
        await ctx.send(f'https://nhentai.net/g/{code}')

# Bot setup.
def setup(bot):
    bot.add_cog(NSFW(bot))