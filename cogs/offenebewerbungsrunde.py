from datetime import datetime

import discord, json
from discord.ext import commands, pages



class offene(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(integration_types={discord.IntegrationType.guild_install}, name="bewerbungsphase",
                           description="Sende die Bewerbungsphase")
    async def _phase(self, ctx: discord.ApplicationContext, ping: bool, datum: discord.Option(str, description="Datum der Bewerbungsphase"), uhrzeit: discord.Option(str, description="Uhrzeit der Bewerbungsphase")):
        role = discord.utils.get(ctx.guild.roles,
                                 id=1244967919247429663)  # Hole die Rolle aus der Liste der Serverrollen
        if role not in ctx.author.roles:
            return await ctx.response.send_message("Du hast keine Berechtigung, diesen Befehl auszuführen.", ephemeral=True)
        embed = discord.Embed(title="Das LSPD veranstaltet eine offene Bewerbungsrunde",
                              description=f"Das LSPD lädt Sie am {datum} zwischen {uhrzeit} zur offenen Bewerbungsrunde ein. Die Bewerbungsrunde findet am Flughafen, im Hangar, statt."
                              colour=0x0031f5)

        embed.set_author(name="LSPD x Offene Bewerbungsrunde")

        embed.add_field(name="Was sind die Mindestanforderungen?",
                        value="Du musst folgende Anforderungen erfüllen\n- Visum 10\n- Eine Straffreie Akte\n- OOC Alter 16\n- Kenntnisse über die Gesetze\n- Waffenschein + Führerschein",
                        inline=False)
        embed.add_field(name="Wann?",
                        value=f"Die offene Bewerbungsrunde findet am {datum} zwischen {uhrzeit} statt.",
                        inline=False)

        embed.set_image(url="https://i.ibb.co/2ZxJSxV/Bild-2024-10-01-173037068.png")

        embed.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")

        embed.set_footer(text=f"Gesendet von {ctx.author.name} und programmiert von rivonivo")

        await ctx.respond(f"Sehr geehrte/r {'<@&1264670715718926346>' if ping else 'Bewerber'}", embed=embed,
                          ephemeral=False)


def setup(bot):
    bot.add_cog(offene(bot))
