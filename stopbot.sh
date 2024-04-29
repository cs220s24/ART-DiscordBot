# Stop the Discord bot container
docker stop discordbot

# Stop the Redis container
docker stop redis

# Remove the Discord bot container
docker rm discordbot

# Remove the Redis container
docker rm redis

# Remove the bot network
docker network rm bot

