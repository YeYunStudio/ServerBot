import discord
from discord.ext import commands


class Moderations(commands.Cog):
	def __init__(self, bot):
		self.bot=bot


	@commands.Cog.listener()
	async def on_ready(self):
		print(f'loaded cog: {__name__}')

	@commands.command()
	async def kick(self, ctx, member: discord.Member, *, reason = None):
		pass

	@kick.error
	async def kick_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send("Kick failed\nReason:Missing Administrator Permissions")

	@commands.command()
	@commands.has_permissions(administrator = True)
	async def ban(self, ctx, member: discord.Member, *, reason = None):
		await member.ban(reason=reason)
		await ctx.send(f'Ban {member} complete\nReason:{reason}')

	@ban.error
	async def ban_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send("Ban failed\nReason:Missing Administrator Permissions")


def setup(bot):
	bot.add_cog(Moderations(bot))