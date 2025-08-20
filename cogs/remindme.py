# cogs/remindme.py
import discord
from discord.ext import commands
import asyncio

class RemindMe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="remindme")
    async def remindme(self, ctx, time: int, *, reminder: str):
        """
        Usage: !remindme <seconds> <reminder>
        Example: !remindme 60 Take out the trash
        """
        await ctx.send(f"⏰ Okay {ctx.author.mention}, I'll remind you in {time} seconds to: {reminder}")

        # Wait for the specified time
        await asyncio.sleep(time)

        await ctx.send(f"🔔 Reminder for {ctx.author.mention}: {reminder}")

async def setup(bot):
    await bot.add_cog(RemindMe(bot))
