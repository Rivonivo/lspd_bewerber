from datetime import datetime

import discord, json
from discord.ext import commands, pages



class offene(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(integration_types={discord.IntegrationType.guild_install}, name="bewerbungsphase",
                           description="Sende die Bewerbungsphase")
    async def _phase(self, ctx: discord.ApplicationContext, ping: bool):
        if ctx.author.id == 701025570695282739 or ctx.author.guild_permissions.administrator:
            return await ctx.response.send_message("Du hast keine Berechtigung, diesen Befehl auszuführen.", ephemeral=True)
        embed = discord.Embed(title="Das LSPD eröffnet die reguläre Bewerbungsphase",
                              colour=0x0031f5)

        embed.set_author(name="LSPD x Eröffnung der regulären Bewerbung")

        embed.add_field(name="Was sind die Mindestanforderungen?",
                        value="Du musst folgende Anforderungen erfüllen\n- Visum 10\n- Eine Straffreie Akte\n- OOC Alter 16\n- Kenntnisse über die Gesetze\n- Waffenschein + Führerschein",
                        inline=False)
        embed.add_field(name="Wie?",
                        value="Eröffne ein Ticket im Channel <#1244243748414820352> und folge den Anweisungen.",
                        inline=False)

        embed.set_image(url="https://i.ibb.co/pQkWG2r/ersteinstellung.png")

        embed.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")

        embed.set_footer(text="Created and coded by rivonivo")

        await ctx.respond(f"Sehr geehrte/r {'<@&1264670715718926346>' if ping else 'Bewerber'}", embed=embed,
                          ephemeral=False)


def setup(bot):
    bot.add_cog(offene(bot))
