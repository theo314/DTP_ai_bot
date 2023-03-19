import os
import discord
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up Discord bot client
client = discord.Client()

# Define a function to generate a response using the ChatGPT API
def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=200,  # Increase max_tokens for longer responses
            top_p=1,
            best_of=2,
            frequency_penalty=1,  # Lower frequency_penalty for more informative answers
            presence_penalty=1,  # Lower presence_penalty for more informative answers
            n=1,
            stop=None,
            temperature=0.7,  # Decrease temperature for more focused responses
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response."

# Define an event listener that responds to messages mentioning the bot
@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Check if the bot is mentioned in the message
    if client.user.mentioned_in(message):

        # Generate a response using the ChatGPT API
        prompt = f"Discord chatbot conversation:\nUser: {message.content}\nAI:"
        response = generate_response(prompt)

        # Send the response back to the Discord server
        await message.channel.send(response)

# Start the Discord bot client
client.run(os.getenv("DISCORD_BOT_TOKEN"))
