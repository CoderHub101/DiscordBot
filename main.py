import discord
import json
import logging

# loading client info
file = open('config.json')
info = json.load(file)
config = info['token']

# logging handler
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# enabling intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Startup log
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Message event
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('hello') or message.content.lower().startswith('hi') or message.content.lower().startswith('hey'):
        await message.channel.send('Hello!')
        
# Initiates bot, log handler, and debugs unexpected errors
client.run(config, log_handler=handler, log_level=logging.DEBUG)