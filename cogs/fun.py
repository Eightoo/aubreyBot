import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, sides: int = 6):
        """Rolls a dice with the given number of sides (default 6)."""
        result = random.randint(1, sides)
        await ctx.send(f"🎲 You rolled a {result}!")

    @commands.command()
    async def choose(self, ctx, *options):
        """Randomly choose from provided options."""
        if not options:
            await ctx.send("Please provide some options!")
        else:
            choice = random.choice(options)
            await ctx.send(f"I choose: {choice}")

async def setup(bot):
    await bot.add_cog(Fun(bot))
