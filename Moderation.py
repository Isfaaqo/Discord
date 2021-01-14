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
                if (user.name, user.discriminator) == (member_name, member_discriminator):
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


# Bot setup.
def setup(bot):
    bot.add_cog(Basic(bot))