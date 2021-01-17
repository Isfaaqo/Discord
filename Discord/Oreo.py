import discord
import os
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

# Permissions.
intents = discord.Intents(
    messages=True, guilds=True, reactions=True, members=True, presences=True)

# Prefix Assignment
bot = commands.Bot(command_prefix = '/', help_command=None)

# Loading cogs.
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# Startup * Bot Token.
bot.run('Nzk4MDc5Mzk2MDQ0MzQxMjk4.X_vzWw.CE9pFe64zl6dG98im7T3vtUM_S4')