import discord
from discord.ext import commands
import random

quotes_db = {}

class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        content = message.content.strip()

        if content.startswith(".. "):  # Save quote
            data = content[3:].strip()
            parts = data.split(' ', 1)
            if len(parts) < 2:
                await message.channel.send("Please provide a name and a quote. Example:\n.. inspiration Keep going!")
            else:
                name, quote = parts[0], parts[1]
                quotes_db.setdefault(name, []).append(quote)
                await message.channel.send(f'Quote saved under "{name}".')

        elif content.startswith("... "):  # Retrieve quote
            name = content[4:].strip()
            if not name:
                await message.channel.send("Please provide a name. Example:\n... inspiration")
            elif name not in quotes_db:
                await message.channel.send(f'No quotes found for "{name}".')
            else:
                selected = random.choice(quotes_db[name])
                await message.channel.send(f'{selected}')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong! 🏓")


async def setup(bot):
    await bot.add_cog(Quotes(bot))
