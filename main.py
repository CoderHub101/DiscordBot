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

    msg = message.content.lower()

    if msg.startswith(prefix):
    
        if message.author == client.user:
            return

        if 'hello' in msg or 'hi' in msg or 'hey' in msg:
            await message.channel.send('Hello!')

        if 'codinglang' in msg:
            await message.channel.send(commands.random_lang())

        if 'bye' in msg:
            await message.channel.send('Bye bye!')
            print('Shutting down!')
            await client.close()

        if 'coinflip' in msg:
            result = commands.coinflip()
            await message.channel.send(result)

        if 'help' in msg:
            await message.channel.send(commands.help())
        
        if 'todolist' in msg:
            output = ''

            for item in commands.todo:
                output += item
                output += '\n'

            if 'add' in msg:
                parts = msg.split(' ', 4)
                # coderhub todolist add stuff june 1
                item = parts[3]
                due_date = parts[4]
                commands.todo_list(item, due_date)

                await message.channel.send('Todo list item added!')
                await message.channel.send(f'Current List: {output}')
            if 'show' in msg:
                await message.channel.send(output)


# Initiates bot, log handler, and debugs unexpected errors
client.run(config, log_handler=handler, log_level=logging.DEBUG)
