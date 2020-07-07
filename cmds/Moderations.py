import discord
from discord.ext import commands
import time


class Moderations(commands.Cog):
	def __init__(self, bot):
		self.bot=bot


	@commands.Cog.listener()
	async def on_ready(self):
		print(f'loaded cog: {__name__}')

	@commands.command()
	async def kick(self, ctx, member: discord.Member, *, reason = None):
		await member.kick(reason=reason)
		await ctx.send(f'已踢出{member}\n理由：{reason}')

	@kick.error
	async def kick_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('無法使用kick指令\n理由：缺少相關權限(管理員)')

	@commands.command()
	@commands.has_permissions(administrator = True)
	async def ban(self, ctx, member: discord.Member, *, reason = None):
		await member.ban(reason=reason)
		await ctx.send(f'已封鎖{member}\n理由：{reason}')

	@ban.error
	async def ban_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('無法使用ban指令\n理由：缺少相關權限(管理員)')
	
	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def clean(self, ctx, num : int):
		await ctx.channel.purge(limit = num+1)
		await ctx.send(f'已刪除{num}條訊息')
		time.sleep(5)
		await ctx.channel.purge(limit = 1)

	@clean.error
	async def clean_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(f"無法使用clean指令\n理由：缺少相關權限(管理訊息)")

def setup(bot):
	bot.add_cog(Moderations(bot))