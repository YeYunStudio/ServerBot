import discord
from discord.ext import commands
import datetime

class Utilities(commands.Cog):
	def __init__(self, bot):
		self.bot=bot


	@commands.Cog.listener()
	async def on_ready(self):
		print(f'loaded cog: {__name__}')

	@commands.command()
	async def ping(self, ctx):
		await ctx.send('Pong!\n目前延遲是{round(self.bot.latency*1000)}ms唷～')

def setup(bot):
	bot.add_cog(Utilities(bot))