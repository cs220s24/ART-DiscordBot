Art Display Discord Bot
------------------------
This project is for running a discord bot that display art using discord.py

Set-Up Locally
---------------
1. Clone Github Repo into the perfered directory
2. Cd into ART-DiscordBot
3. Add .env file with
```
DISCORD_TOKEN={Your Token Here}
REDIS_HOST=localhost
 ```
6. Run ```python3 -m venv .venv```
7. Run ```pip install -r requirements.txt```
8. Run ```redis-server```
9. Run ```python3 bot.py```

Closing Bot
-------------
1. Press control + c to close bot
2. Run "redis-cli shutdown" to shutdown redis database

Set Up on AWS
--------------
1. Run ```Sudo yum install git```
2. Run ```Sudo yum install pip```
3. Clone Github Repo
4. Cd into ART-DiscordBot
5. Add .env file with
```
DISCORD_TOKEN={Your Token Here}
REDIS_HOST=redis
 ```
6. Run ```python3 -m venv .venv```
<<<<<<< HEAD
7. Run ```source .venv/bin/activate```
8. Run ```pip install -r awsrequirements.txt```
9. Run ```Sudo yum install -y redis6```
10. Run ```redis6-server```
11. Run ```python3 bot.py```
=======
7. Run ```pip install -r requirements.txt```
8. Run ```Sudo yum install redis6```
9. Run ```redis6-server```
10. Run ```python3 bot.py```
>>>>>>> 1fed4e6bf4062a41b35cee492d292f0ee933dd1e

Setup on AWS through Docker
-
1. Run ```Sudo yum install -y git```
2. Clone repo
3. CD into ART-DiscordBot
4. Run ```chmod +x setup.sh``` and ```chmod +x startbot.sh``` to add executable permissions
5. Run ```./setup.sh```
6. Add .env with
 ```
DISCORD_TOKEN={Your Token Here}
REDIS_HOST=redis
 ```
5. Log out and log back into EC2 Instance
6. CD into ART-DiscordBot
7. Run ```./startbot.sh```

Resources Used
-----------
* https://www.youtube.com/watch?v=UYJDKSah-Ww&t=356s
* https://realpython.com/how-to-make-a-discord-bot-python/
* https://discordpy.readthedocs.io/en/stable/
* https://discord.com/developers
* https://discord.com
* https://github.com/
* https://redis.io

Project By
------------
* Marena Abboud
* Giovanny Teran
* Vicente Rivera
