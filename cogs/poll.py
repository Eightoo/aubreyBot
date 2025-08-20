# cogs/poll.py
import discord
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="poll")
    async def poll(self, ctx, *, question_and_options: str):
        """
        Usage: !poll Question | Option1 | Option2 | Option3
        """
        parts = [p.strip() for p in question_and_options.split("|")]

        if len(parts) < 2:
            await ctx.send("❌ You need at least a question and one option.")
            return

        question = parts[0]
        options = parts[1:]

        emoji_numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
        if len(options) > len(emoji_numbers):
            await ctx.send("❌ Too many options! Max 6.")
            return

        description = ""
        for i, option in enumerate(options):
            description += f"{emoji_numbers[i]} {option}\n"

        embed = discord.Embed(
            title=f"📊 {question}",
            description=description,
            color=discord.Color.blurple()
        )

        poll_message = await ctx.send(embed=embed)

        # React with emojis
        for i in range(len(options)):
            await poll_message.add_reaction(emoji_numbers[i])

async def setup(bot):
    await bot.add_cog(Poll(bot))
