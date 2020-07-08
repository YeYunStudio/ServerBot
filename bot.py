import discord
from discord.ext import commands
import json
import os
import keep_alive

with open ('config.json', 'r', encoding='utf8') as data:
	config = json.load(data)
with open ('aliases.json', 'r', encoding='utf8') as aliases:
	aliases = json.load(aliases)

bot = commands.Bot(command_prefix=config['prefix'])

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name=">>Release Mode<<"))
	print(f'Logged in as: {bot.user.name}')
	print(f'With ID: {bot.user.id}')
	print(f'Prefix: {bot.command_prefix}')

bot.remove_command('help')
@bot.command(aliases = aliases['help'])
async def help(ctx):
	await ctx.send('請到此處查看唷')
	await ctx.send(config['help'])

@bot.command()
async def prefix(ctx):
	await ctx.send(f'在這個Server的Prefix是`{bot.command_prefix}`唷')

@bot.command()
@commands.is_owner()
async def enable(ctx, extension):
	bot.load_extension(f'cmds.{extension}')
	await ctx.send(f'已起用{extension}')
	
@enable.error
async def enable_error(ctx, error):
	if isinstance(error, commands.NotOwner):
		await ctx.send("您無法使用這個指令\n原因:不是機器人的擁有者")
	raise error

@bot.command()
@commands.is_owner()
async def disable(ctx, extension):
	bot.disable_extension(f'cmds.{extension}')
	await ctx.send(f'已禁用{extension}')

@disable.error
async def disable_error(ctx, error):
	if isinstance(error, commands.NotOwner):
		await ctx.send('您無法使用這個指令\n原因:不是機器人的擁有者')
	raise error

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
	bot.reload_extension(f'cmds.{extension}')
	await ctx.send(f'已重新載入{extension}')

@reload.error
async def reload_error(ctx, error):
	if isinstance(error, commands.NotOwner):
		await ctx.send('您無法使用這個指令\n原因:不是機器人的擁有者')
	raise error

@bot.command()
async def invite(ctx):
	await ctx.send(config['invite'])

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
	await ctx.send('正在關機')
	await bot.close()

@shutdown.error
async def shutdown_error(ctx, error):
	if isinstance(error, commands.NotOwner):
		await ctx.send('您無法使用這個指令\n原因:不是機器人的擁有者')

@bot.command()
@commands.is_owner()
async def reboot(ctx):
	await ctx.send('正在重啟')
	await bot.close()
	await bot.login(token=config['token'], bot=True)

@reboot.error
async def reboot_error(ctx, error):
	if isinstance(error, commands.NotOwner):
		await ctx.send('您無法使用這個指令\n原因:不是機器人的擁有者')

@bot.command()
async def aliases(ctx):
	await ctx.send('請到此處查看唷～')
	await ctx.send(config['aliases'])

for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
		bot.load_extension(f'cmds.{filename[:-3]}')

keep_alive.keep_alive()
bot.run(config['token'])