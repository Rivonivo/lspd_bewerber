from datetime import datetime

import discord, json
from discord.ext import commands, pages

class bewerbungsstatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="bewerbungsstatus", description="Sende den Status der Bewerbungen")
    async def _status(self, ctx: discord.ApplicationContext, normal: bool = False, wiedereinstellung: bool = False, orgawechsel: bool = False, beschleunigt: bool = False, tow: bool = False):
        role = discord.utils.get(ctx.guild.roles,
                                 id=1244967919247429663)  # Hole die Rolle aus der Liste der Serverrollen
        if role not in ctx.author.roles:
            return await ctx.response.send_message("Du hast keine Berechtigung, diesen Befehl auszuführen.", ephemeral=True)

        embed1 = discord.Embed(title="Reguläre Bewerbung",
                               description="Du möchtest für Recht und Ordnung auf den Straßen von Los Santos sorgen?\nBewerbe dich als Officer beim Los Santos Police Department!",
                               colour=0x00ff00 if normal else 0xff0000)

        embed1.set_author(name=f'{"Geöffnet" if normal else "Geschlossen"}')

        embed1.set_image(url="https://i.ibb.co/pQkWG2r/ersteinstellung.png")

        embed1.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")
        await ctx.send_response(f" ", embed=embed1)
        embed2 = discord.Embed(title="Wiedereinstellung",
                               description="Du warst schon mal bei uns? Mache eine Wiedereinstellung und sorge für Recht und Ordnung",
                               colour=0x00ff00 if wiedereinstellung else 0xff0000)

        embed2.set_author(name=f'{"Geöffnet" if wiedereinstellung else "Geschlossen"}')

        embed2.set_image(url="https://i.ibb.co/0sS2BXx/wiedereinstellung.png")

        embed2.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")
        await ctx.send_followup(f" ", embed=embed2)
        embed3 = discord.Embed(title="Orgawechsel",
                               description="Du bist z.B. in der Regierung tätig und möchtest was neues probieren. Frage einen Orgawechsel bei deiner HR an und erstelle eine Bewerbung!",
                               colour=0x00ff00 if orgawechsel else 0xff0000)

        embed3.set_author(name=f'{"Geöffnet" if orgawechsel else "Geschlossen"}')

        embed3.set_image(url="https://i.ibb.co/L0Fq0hj/orgawechsel.png")

        embed3.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")
        await ctx.send_followup(f" ", embed=embed3)
        embed4 = discord.Embed(title="Beschleunigtes Verfahren",
                               description="DU wurdest vom LSPD empfohlen? Dann eröffne eine Bewerbung beim LSPD!",
                               colour=0x00ff00 if beschleunigt else 0xff0000)

        embed4.set_author(name=f'{"Geöffnet" if beschleunigt else "Geschlossen"}')

        embed4.set_image(url="https://i.ibb.co/NsBCHvs/beschleunigt.png")

        embed4.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")
        await ctx.send_followup(f" ", embed=embed4)
        embed5 = discord.Embed(title="TOW Division",
                               description="Die Straßenverkehrsordnung ist deine Abendlektüre und du hast es satt Falschparker im Straßenverkehr zu sehen? Bewerbe dich als TOW Officer.",
                               colour=0x00ff00 if tow else 0xff0000)

        embed5.set_author(name=f'{"Geöffnet" if tow else "Geschlossen"}')
        embed5.set_image(url="https://i.ibb.co/NSsSfqR/tow.png")

        embed5.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")
        await ctx.send_followup(f" ", embed=embed5)
        return


def setup(bot):
    bot.add_cog(bewerbungsstatus(bot))
