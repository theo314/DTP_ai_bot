# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . .

# Expose a port for the Discord bot to communicate through
EXPOSE #####

# Set the environment variable for running the bot
ENV DISCORD_BOT_TOKEN ##########
ENV OPENAI_API_KEY ##########

# Start the bot
CMD ["python", "bot.py"]
