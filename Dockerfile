FROM amazonlinux

# Set the working directory
WORKDIR /bot

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN python3 -m venv .venv
RUN .venv/bin/pip3 install -r requirements.txt

# Copy bot.py
COPY bot.py .
COPY redis_utils.py .

# Run the bot
CMD .venv/bin/python3 bot.py


