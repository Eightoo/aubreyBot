from discord.ext import commands
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer globally
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Store recent user messages for context, limited to last 3 messages
user_history = {}

class AIChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chat(self, ctx, *, prompt):
        """
        Chat with AI. Uses only the last 3 messages for context.
        Usage: !chat Hello AI
        """
        user_id = ctx.author.id

        # Initialize history
        if user_id not in user_history:
            user_history[user_id] = []

        # Append new user message
        user_history[user_id].append(prompt)

        # Keep only last 3 messages
        recent_messages = user_history[user_id][-3:]

        # Prepare model input: only last message (or concatenate short context)
        input_text = " ".join(recent_messages[-1:])

        # Tokenize and generate response
        inputs = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
        outputs = model.generate(
            max_length=150,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_p=0.9,
            top_k=50
        )
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        await ctx.send(answer)

    @commands.command()
    async def reset(self, ctx):
        """
        Clear your AI conversation memory.
        Usage: !reset
        """
        user_id = ctx.author.id
        user_history[user_id] = []
        await ctx.send("Your AI conversation memory has been cleared.")

async def setup(bot):
    await bot.add_cog(AIChat(bot))
