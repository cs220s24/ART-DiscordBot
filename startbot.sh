docker network create bot

docker run --name redis --network bot -d redis

docker build -t discordbot .

docker run --name discordbot -d --network bot --env-file ./.env discordbot

