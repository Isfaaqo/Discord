import discord
import random
from discord.ext import commands, tasks
bot = commands.Bot(command_prefix='/')

insults = {
    "linux": "https://www.youtube.com/watch?v=QXUSvSUsx80",
    "fat": "You're fat",
    "library": "Fucking nerds"
}


# Cogs class.
class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.latency

    # On initialisation.
    @commands.Cog.listener()
    async def on_ready(self):
      await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="hentai"))
      print('Oreo is ready to be dunked!')

    # You know what?
    @commands.command()
    async def ykw(self, ctx):
        await ctx.send(f'You know what, fair enough.')

    # Latency Check.
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Latency is {round(self.bot.latency * 1000)}ms ')

    # Random 8 Ball.
    @commands.command(aliases=[
        '8ball',
    ])
    async def _8ball(self, ctx, *, question):
        responses = [
            "It is certain.", "It is decidedly so.", "Without a doubt.",
            "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
            "Reply hazy, try again.", "Ask again later.", "Don't count on it.",
            "My sources say no.", "Outlook not so good.", "Very doubtful."
        ]

        await ctx.send(
            f'Question: {question}\nAnswer: {random.choice(responses)}')

    # Rick roll
    @commands.command(aliases=['DM', 'Dm'])
    async def dm(self, ctx, user: discord.User, *, message=None):
        if not message:
            await user.send('https://i.gifer.com/4KL.gif')
        else:
            await user.send(message)

    # For our lord, Gary.
    @commands.command()
    async def gary(self, ctx):
        await ctx.send(
            'All praise the supreme Chad, Gary Sun, the mentor from UNSW that knows how to code and bone. The ladies fall for him day and night, even if he still lives with his parents. Gary our lord and savior shall redeem us of our sins and make sure we do not stray into economics, the topic of hell, like he did. Gary is a cool dude, even if he went to baulko. He looks like he is 5 feet tall but that does not matter as we praise him for his charisma and athletic skills. All hail Lord Gary'
        )

    @commands.command(aliases=['Help', 'HELP'])
    async def help(self, ctx, page=0):
        if not page:
            await ctx.send(
                "```Basic Commands : \n ykw - For Angela :) \n ping - To check latency \n 8ball - Ask a question \n dm - Make the bot message someone \n gary - For the Supreme Chad \n Page 1 of 3 - /help 2 and /help 3 to move.```"
            )
        elif page == 2:
            await ctx.send(
                "```Moderation Commands - Require Perms : \n clear/purge - Remove messages in format /clear amount \n kick - Kick someone off the server \n ban - Ban someone \n unban - Unban someone.```"
            )
        elif page == 3:
            await ctx.send(
                "```NSFW Commands : \n nhentai or nh with code afterwards provide specified hentai, if unspecified it will return a random one```"
            )

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        else:
            for word in insults:
                if word in message.content.lower():
                    await message.channel.send(insults[word])


# Bot setup.
def setup(bot):
    bot.add_cog(Basic(bot))
