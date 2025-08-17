import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()  # ✅ Only the bot owner can use this
    async def reload(self, ctx, extension: str):
        """
        Reloads a specific cog. Example: !reload quotes
        """
        try:
            await self.bot.unload_extension(f"cogs.{extension}")
            await self.bot.load_extension(f"cogs.{extension}")
            await ctx.send(f"🔄 Reloaded `{extension}` cog successfully!")
        except Exception as e:
            await ctx.send(f"❌ Failed to reload `{extension}`: {e}")

    @commands.command()
    @commands.is_owner()  # ✅ Same protection here
    async def reloadall(self, ctx):
        """
        Reloads all cogs in the cogs/ folder.
        """
        for ext in list(self.bot.extensions.keys()):
            try:
                await self.bot.unload_extension(ext)
                await self.bot.load_extension(ext)
            except Exception as e:
                await ctx.send(f"❌ Failed to reload `{ext}`: {e}")
        await ctx.send("🔄 Reloaded all cogs!")

async def setup(bot):
    await bot.add_cog(Admin(bot))
