import discord
from discord.ext import commands


class Moderations(commands.Cog):
	def __init__(self, bot):
		self.bot=bot


	@commands.Cog.listener()
	async def on_ready(self):
		print(f'loaded cog: {__name__}')


def setup(bot):
	bot.add_cog(Moderations(bot))