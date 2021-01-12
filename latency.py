import discord
from discord import client
from discord.ext import commands

# Cogs class.
class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.latency

    @commands.Cog.listener()
    async def on_ready(self):
        print('Oreo is ready to be dunked!')



# bot setup.
def setup(bot):
    bot.add_cog(Example(bot))