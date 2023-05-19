import discord
import json
import logging
import commands

# loading client info
file = open('config.json')
info = json.load(file)
config = info['token']

# logging handler
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# enabling intents
intents = discord.Intents.default()
intents.message_content = True
prefix = 'coderbot'

client = discord.Client(intents=intents)

# Startup log
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Message event
@client.event
async def on_message(message):

    # TODO: Can we make a dictionary associating these message
    # contents with their specific functions instead of brute
    # force code?

    if message.content.lower().startswith(prefix):
    
        if message.author == client.user:
            return

        if 'hello' in message.content.lower() or 'hi' in message.content.lower()or 'hey' in message.content.lower():
            await message.channel.send('Hello!')

        if 'codinglang' in message.content.lower():
            await message.channel.send(commands.random_lang())

        if 'bye' in message.content.lower():
            await message.channel.send('Bye bye!')
            print('Shutting down!')
            await client.close()

        if 'coinflip' in message.content.lower():
            result = commands.coinflip()
            await message.channel.send(result)

        if 'purge50' in message.content.lower():
            for i in range(0, 50):
                await discord.Message.delete()

        # TODO: Fix this, not printing commands
        if 'help' in message.content.lower():
            for command, description in commands.commandList:
                await message.channel.send(f'{prefix} {command} - {description}\n')
        
# Initiates bot, log handler, and debugs unexpected errors
client.run(config, log_handler=handler, log_level=logging.DEBUG)
