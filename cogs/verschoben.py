from datetime import datetime

import discord, json
from discord.ext import commands, pages



class verschoben(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="send_to_category", description="Sendet eine Nachricht an alle Kanäle in einer Kategorie")
    async def send_to_category(ctx: discord.ApplicationContext, category_id: str):
        category_id = int(category_id)
        category = discord.utils.get(ctx.guild.categories, id=category_id)
        if not category:
            await ctx.response.send_message("Kategorie nicht gefunden.", ephemeral=True)
            return

        for channel in category.text_channels:
            embed = discord.Embed(title="Grundausbildung verschoben",
                                  description="Aufgrund der bevorstehenden Purge, verschieben wir die Grundausbildung auf den <t:1723998600:F>.\nDas wäre <t:1723998600:R>\n\nWir bitten um Verständnis.\n\nHuman Resources",
                                  colour=0xffff00)

            embed.set_author(name="Grundausbildung")

            embed.set_image(url="https://i.ibb.co/ZHr2Q4s/hr.png")

            embed.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")
            await channel.send(embed=embed)

        await ctx.respond("Nachricht an alle Kanäle in der Kategorie gesendet.", ephemeral=True)

def setup(bot):
    bot.add_cog(verschoben(bot))
