import discord
from discord.ext import commands
import json
import os
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
	await ctx.send('請到此處查看唷')
	await ctx.send(config['help'])

@bot.command()
async def prefix(ctx):
	await ctx.send(f'在這個Server的Prefix是`{bot.command_prefix}`唷')

for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
		bot.load_extension(f'cmds.{filename[:-3]}')

keep_alive.keep_alive()
bot.run(config['token'])