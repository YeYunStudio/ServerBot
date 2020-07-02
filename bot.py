import discord
from discord.ext import commands
import json
import keep_alive

with open('config.json', 'r', encoding='utf8') as data:
	config = json.load(data)

bot = commands.Bot(command_prefix=config['prefix'])

@bot.event
async def on_ready():
	print(f'Logged in as: {bot.user.name}')
	print(f'With ID: {bot.user.id}')
	print(f'Prefix: {bot.command_prefix}')

bot.remove_command('help')
@bot.command()
async def help(ctx):
	await ctx.send(config['help'])

@bot.command()
async def prefix(ctx):
	await ctx.send(f'在這個Server的Prefix是`{bot.command_prefix}`唷')

keep_alive.keep_alive()
bot.run(config['token'])