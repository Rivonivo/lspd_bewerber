from datetime import datetime

import discord, json
from discord.ext import commands, pages



class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Example(bot))
