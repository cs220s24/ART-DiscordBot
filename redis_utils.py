import redis
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('REDIS_HOST')

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
    redis_client = redis.StrictRedis(host=host, port=6379, db=0)
    # Clear existing data
    redis_client.flushdb()
    # Add new URLs
    for image_url in cat_image_urls:
        redis_client.sadd('cats', image_url)
    for image_url in dog_image_urls:
        redis_client.sadd('dogs', image_url)

