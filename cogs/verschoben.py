from datetime import datetime

import discord, json
from discord.ext import commands, pages



class verschoben(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="grundausbildung", description="Sendet die GA Nachricht an alle Kanäle in einer Kategorie")
    async def send_to_category(self, ctx: discord.ApplicationContext, category_id: str, wochentag: discord.Option(str, choices=["Mittwoch", "Samstag"], description="Wähle den Wochentag")):
        if ctx.author.id == 701025570695282739 or ctx.author.guild_permissions.administrator:
            return await ctx.response.send_message("Du hast keine Berechtigung, diesen Befehl auszuführen.",
                                                   ephemeral=True)
        category_id = int(category_id)
        category = discord.utils.get(ctx.guild.categories, id=category_id)
        if not category:
            await ctx.response.send_message("Kategorie nicht gefunden.", ephemeral=True)
            return

        for channel in category.text_channels:
            embed = discord.Embed(title="Heute ist Grundausbildung",
                                  description=f"Am {wochentag} findet unsere Grundausbildung statt.\nBitte finden sie sich um **18.30** in der LSPD Lobby ein.\n\nMit freundlichen Grüßen\n\nHuman Resources",
                                  colour=discord.Colour.blurple())

            embed.set_author(name="Grundausbildung")

            embed.set_image(url="https://i.ibb.co/ZHr2Q4s/hr.png")

            embed.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")
            await channel.send(embed=embed)

        await ctx.respond("Nachricht an alle Kanäle in der Kategorie gesendet.", ephemeral=True)

def setup(bot):
    bot.add_cog(verschoben(bot))
