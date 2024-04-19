import os
import redis
from discord import Intents, Client

# Import dotenv if you're using environment variables
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Sample cat and dog image URLs from Imgur
cat_image_urls = [
    'https://imgur.com/SpCbHBI',
    'https://imgur.com/b9T47yP',
    'https://imgur.com/8dF73nu'
]

dog_image_urls = [
    'https://imgur.com/sjpa0Gg',
    'https://imgur.com/Cpr6QEu',
    'https://imgur.com/Dg5tv0L'
]

# Function to initialize the Redis database with cat and dog image URLs
def initialize_database():
    # Clear existing data
    redis_client.flushdb()
    # Add new URLs
    for image_url in cat_image_urls:
        redis_client.sadd('cats', image_url)
    for image_url in dog_image_urls:
        redis_client.sadd('dogs', image_url)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # Initialize the database when the bot is ready
    initialize_database()
    print('Database initialized with cat and dog image URLs.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'Cats':
        image_url = redis_client.srandmember('cats')
        if image_url:
            await message.channel.send(image_url.decode('utf-8'))
        else:
            await message.channel.send("No cat images available.")
    elif message.content == 'Dogs':
        image_url = redis_client.srandmember('dogs')
        if image_url:
            await message.channel.send(image_url.decode('utf-8'))
        else:
            await message.channel.send("No dog images available.")

# Retrieve the bot token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)
