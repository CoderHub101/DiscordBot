import discord
import json

# loading client info
file = open('config.json')
info = json.load(file)
config = info['token']

# enabling intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Startup log
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Message event
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('hello') or message.content.lower().startswith('hi') or message.content.lower().startswith('hey'):
        await message.channel.send('Hello!')
        
# Initiates bot
client.run(config)