import discord
import random
import os
import asyncio
from discord import message
from discord.client import Client
from discord.ext import commands

# Flask for server.
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Oreo has been dunked."

def run():
    app.run(host="0.0.0.0", port=8000)

def keep_alive():
    server = Thread(target=run)
    server.start()

# Keeping Alive.
keep_alive()

# Background Task.
client = discord.Client()

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id='channel_id_here')
    while not client.is_closed:
        counter += 1
        await client.send_message(channel, counter)
        await asyncio.sleep(60)  # task runs every 60 seconds

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(my_background_task())

# Permissions.
intents = discord.Intents(
    messages=True, guilds=True, reactions=True, members=True, presences=True)
# Prefix Set.
bot = commands.Bot(command_prefix='/', intents=intents)

# Loading cogs.
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# Startup * Bot Token.
bot.run('Nzk4MDc5Mzk2MDQ0MzQxMjk4.X_vzWw.nTn1drNi1FkWtnTD4rv0gmEZ3VI')