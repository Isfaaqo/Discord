import discord
import random
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

    # When a member joins.
    @bot.event
    async def on_member_join(self, member):
        print(f'{member} has joined the nerd gang!')

    # When a member leaves.
    @bot.event
    async def on_member_remove(self, member):
        print(f'{member} has left, Fair enough.')

    # For Yuki.
    @commands.command(hidden=True, aliases = 'nh')
    async def nhentai(self, ctx, code):
        await ctx.send(f'https://nhentai.net/g/{code}')

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


    # Clear / Purge Chat * Amount.
    @commands.command(aliases=['purge'])
    async def clear(self, ctx, amount=5):
        if ctx.author.guild_permissions.manage_messages:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f'{amount} messages were cleared.')


    # Kicking someone * reason.
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.guild_permissions.kick_members:
            await member.kick(reason=reason)
            if reason != None:
                await ctx.send(f'{member} was kicked due to :{reason}.')
                print(f'{member} was kicked due to: {reason}')


    # Banning someone * reason.
    @commands.command()
    async def ban(self, ctx, *, member: discord.Member = None):
        if ctx.author.guild_permissions.administrator:
            if member:
                await member.ban()
                await ctx.send(f"{member} has been banned!")
            else:
                await ctx.send("Please specify a user to ban!")
        else:
            await ctx.send("You know, banning isn't always the right way.")


    # Restoring a banned user.
    @commands.command()
    async def unban(self, ctx, *, member):
        # Pulling ban list.
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        # Checking all banned users.
        for ban_entry in banned_users:
            if ctx.author.guild_permissions.administrator:
                user = ban_entry.user
                # Verifying banned user.
                if (user.name, user.discriminator) == (member_name,                                   member_discriminator):
                    await ctx.guild.unban(user)
                    print(f'{user.name}#{user.discriminator} has been unbanned.')
                    await ctx.send(f'{user.mention} has been unbanned.')
                    invite_link = await ctx.channel.create_invite(unique=True)
                    await user.send(
                        f' You have been unbanned {user}, join back through {invite_link}.'
                    )
                    return
            else:
                await ctx.send(f'Fuck outta here')


    # Rick roll
    @commands.command()
    async def dm(self, ctx, user: discord.User, *, message=None):
        if not message:
            await user.send(
                'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO'
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