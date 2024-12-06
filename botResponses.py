import discord
from discord.ext import commands
from botFunc import handle_response

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said: '{user_message}' ({channel})")
    response = await handle_response(message)
    await bot.process_commands(message)
    if response:
        await message.channel.send(response)

def run_discord_bot():
    TOKEN = ''
    bot.run(TOKEN)

if __name__ == "__main__":
    run_discord_bot()
