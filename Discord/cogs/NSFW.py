from random import randint
from discord.ext import commands

# Cogs class.
class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # For Yuki.
    @commands.command(aliases = ['nh',])
    @commands.is_nsfw()
    async def nhentai(self, ctx, code=None):
        if not code:
            code = randint(0, 425000)
        await ctx.send(f'https://nhentai.net/g/{code}')

# Bot setup.
def setup(bot):
    bot.add_cog(NSFW(bot))