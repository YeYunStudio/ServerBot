import discord
from discord.ext import commands
import datetime
import json

with open ('aliases.json', 'r', encoding='utf8') as aliases:
	aliases = json.load(aliases)

class Utilities(commands.Cog):
	def __init__(self, bot):
		self.bot=bot


	@commands.Cog.listener()
	async def on_ready(self):
		print(f'loaded cog: {__name__}')

	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'Pong!\n目前延遲是{round(self.bot.latency*1000)}ms唷～')

	@commands.command(aliases = aliases['calculate'])
	async def calculate(self, ctx):
		pass

def setup(bot):
	bot.add_cog(Utilities(bot))