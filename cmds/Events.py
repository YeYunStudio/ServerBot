import discord
from discord.ext import commands
import json
from discord import Guild

with open ('config.json', 'r', encoding='utf8') as data:
	config = json.load(data)

class Events(commands.Cog):
	def __init__(self, bot):
		self.bot=bot


	@commands.Cog.listener()
	async def on_ready(self):
		print(f'loaded cog: {__name__}')

	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = self.bot.get_channel(int(config['welcome_channel']))
		await channel.send(f'{member.mention}'+ ' 進入了 '+ f'{member.guild.name}!')

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		channel = self.bot.get_channel(int(config['goodbye_channel']))
		await channel.send(f'**{member.name}#{member.discriminator}**'+ ' 離開了 '+ f'{member.guild.name}')

def setup(bot):
	bot.add_cog(Events(bot))