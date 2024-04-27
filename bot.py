import os
from discord import Intents, Client
from dotenv import load_dotenv
from redis_utils import initialize_database

load_dotenv()

host = os.getenv('REDIS_HOST')

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # Initialize the database when the bot is ready
    await client.get_channel(YOUR_CHANNEL_ID).send("Message either 'cats' or 'dogs' to see a random image")
    initialize_database()
    print('Database initialized with cat and dog image URLs.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()
    if content == 'cats':
        from redis import StrictRedis
        redis_client = StrictRedis(host=host, port=6379, db=0)
        image_url = redis_client.srandmember('cats')
        if image_url:
            await message.channel.send(image_url.decode('utf-8'))
        else:
            await message.channel.send("No cat images available.")
    elif content == 'dogs':
        from redis import StrictRedis
        redis_client = StrictRedis(host=host, port=6379, db=0)
        image_url = redis_client.srandmember('dogs')
        if image_url:
            await message.channel.send(image_url.decode('utf-8'))
        else:
            await message.channel.send("No dog images available.")

TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)
