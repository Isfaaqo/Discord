import discord
import random
from random import randint
from discord import client
from discord.ext import commands
bot = commands.Bot(command_prefix = '/')

# Cogs class.
class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.latency

    # On initialisation.
    @commands.Cog.listener()
    async def on_ready(self):
        print('Oreo is ready to be dunked!')

    # You know what?
    @commands.command()
    async def ykw(self, ctx):
        await ctx.send(f'You know what, Fair Enough. ')

    # Latency Check.
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Latency is {round(self.bot.latency * 1000)}ms ')

    # Random 8 Ball.
    @commands.command(aliases=['8ball', ])
    async def _8ball(self, ctx, *, question):
        responses = [
            "It is certain.", "It is decidedly so.", "Without a doubt.",
            "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
            "Reply hazy, try again.", "Ask again later.", "Don't count on it.",
            "My sources say no.", "Outlook not so good.", "Very doubtful."
        ]

        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    # Rick roll
    @commands.command()
    async def dm(self, ctx, users: discord.User, *, message=None):
        for user in users:        
            if not message:
                await user.send(
                    'https://i.gifer.com/4KL.gif'
                )
            else:
                await user.send(message)

    # For our lord, Gary.
    @commands.command()
    async def gary(self, ctx):
        await ctx.send(
            'All praise the supreme Chad, Gary Sun, the mentor from UNSW that knows how to code and bone. The ladies fall for him day and night, even if he still lives with his parents. Gary our lord and savior shall redeem us of our sins and make sure we do not stray into economics, the topic of hell, like he did. Gary is a cool dude, even if he went to baulko. He looks like he is 5 feet tall but that does not matter as we praise him for his charisma and athletic skills. All hail Lord Gary'
        )
# Bot setup.
def setup(bot):
    bot.add_cog(Basic(bot))