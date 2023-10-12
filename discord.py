import discord

# Initialize the bot
bot = discord.Client()

# Define an event for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Define an event for when the bot receives a message
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN')
