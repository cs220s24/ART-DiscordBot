# bot.py
import os
import random

from discord import Intents, Client, Message
from dotenv import load_dotenv

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    dogImages = ['dog1','dog2','dog3' ]
    catImages = ['cat1','cat2','cat3' ]

    if message.content == 'Cats':
        response = random.choice(catImages)
        await message.channel.send(response)
    if message.content == 'Dogs':
        response = random.choice(dogImages)
        await message.channel.send(response)

client.run(TOKEN)