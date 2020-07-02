import discord
from discord.ext import commands
import json

with open('config.json', 'r', encoding='utf8') as bot:
	config = json.load(bot)

bot = commands.Bot(command_prefix=config['prefix'])


@bot.event
async def on_ready():
	print(f'Logged in as: {bot.user.name}')
	print(f'With ID: {bot.user.id}')
	print(f'Prefix: {bot.get_prefix}')

bot.run(config['token'])