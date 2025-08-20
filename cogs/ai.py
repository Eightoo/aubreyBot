import discord
from discord.ext import commands
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Load DistilGPT-2 tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
        self.model = AutoModelForCausalLM.from_pretrained("distilgpt2")

    @commands.command(name="ai")
    async def ai_chat(self, ctx, *, prompt: str):
        """Chat with Aubrey using local AI (DistilGPT-2)."""
        await ctx.send("Thinking... 🤔")

        try:
            # Encode the prompt
            inputs = self.tokenizer.encode(prompt + self.tokenizer.eos_token, return_tensors="pt")
            # Generate a response
            outputs = self.model.generate(
                inputs,
                max_length=150,
                pad_token_id=self.tokenizer.eos_token_id,
                do_sample=True,
                top_k=50,
                top_p=0.95,
                temperature=0.8
            )
            # Decode and clean up response
            reply = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            # Remove the prompt from the reply
            reply = reply[len(prompt):].strip()
            await ctx.send(reply)

        except Exception as e:
            await ctx.send(f"⚠️ Error: {e}")

async def setup(bot):
    await bot.add_cog(AI(bot))
