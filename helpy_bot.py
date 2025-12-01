# Helpy Fazbear Discord Bot
# This script uses the discord.py library to create a functional Discord bot.

import discord
from discord.ext import commands
import os

# --- Configuration ---
# !!! IMPORTANT: The bot token is now read from the environment variables (for security).
# DO NOT hardcode your token directly in this file! 
# You must set the BOT_TOKEN variable securely on your hosting platform (like Render or Vercel).
BOT_TOKEN = os.getenv("BOT_TOKEN") 

# Define the command prefix (what users type before a command, like !hello)
COMMAND_PREFIX = "!"

# Configure the intents required by Discord.
# We enabled these in the Developer Portal (Message Content, Members, Presence).
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content
intents.members = True          # Required for server member information (good practice)
intents.presences = True        # Required for presence updates (good practice)

# Create the bot instance, passing in the command prefix and intents
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

# --- Bot Events ---

@bot.event
async def on_ready():
    """
    Called when the bot successfully connects to Discord.
    Sets the bot's status and prints a confirmation message.
    """
    # Set the bot's activity/status
    await bot.change_presence(activity=discord.Game(name="Testing for safety"))
    
    print("-----------------------------------------")
    print(f"Logged in as: {bot.user.name} ({bot.user.id})")
    print(f"Bot prefix is: '{COMMAND_PREFIX}'")
    print("Bot is ready to receive commands.")
    print("-----------------------------------------")

# --- Bot Commands ---

@bot.command(name='hello')
async def greet(ctx):
    """
    Responds with a friendly greeting when a user types !hello
    """
    await ctx.send(f"Hey there, {ctx.author.display_name}! I'm Helpy Fazbear, here to assist!")

@bot.command(name='assist')
async def show_help(ctx):
    """
    Provides a simple list of available commands when a user types !assist
    NOTE: Renamed from !help to avoid conflict with Discord's default help command.
    """
    help_message = (
        "**Helpy Fazbear Assistance Protocol:**\n"
        f"`{COMMAND_PREFIX}hello` - I'll greet you!\n"
        f"`{COMMAND_PREFIX}bear` - Hear a fun, classic quote from the Fazbear family.\n"
        f"`{COMMAND_PREFIX}assist` - Shows this list of commands."
    )
    await ctx.send(help_message)

@bot.command(name='bear')
async def quote(ctx):
    """
    Responds with a quote when a user types !bear
    """
    quotes = [
        "Welcome to your new career!",
        "A shocking thing to witness, is it not?",
        "Don't forget to smile; you are the face of Freddy Fazbear's Pizza.",
        "That's one less thing to worry about!",
        "Remember to check your maintenance panels frequently."
    ]
    import random
    await ctx.send(random.choice(quotes))

# --- Run the Bot ---
if not BOT_TOKEN:
    print("\n!!! ERROR: The BOT_TOKEN environment variable was not found. Please set it securely on your hosting platform. !!!\n")
else:
    try:
        bot.run(BOT_TOKEN)
    except discord.HTTPException as e:
        print(f"\n!!! ERROR: Failed to log in. Check your token and ensure all Gateway Intents are enabled in the Developer Portal. !!!")
        print(f"Details: {e}\n")
    except Exception as e:
        print(f"\n!!! An unexpected error occurred: {e} !!!\n")
