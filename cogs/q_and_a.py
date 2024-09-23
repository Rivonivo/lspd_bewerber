from datetime import datetime

import discord, json
from discord.ext import commands, pages



class q_and_a(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(integration_types={discord.IntegrationType.user_install}, name="q_and_a",
                       description="Sende den Q&A Announce")

    async def _faq(self, ctx: discord.ApplicationContext, ping: bool):
        if ctx.user.guild_permissions.administrator is not True or ctx.user.id == 701025570695282739:
            return await ctx.response.send_message("Du hast keine Berechtigung, diesen Befehl auszuführen.", ephemeral=True)
        embed = discord.Embed(title="Q&A - Bewerbung beim Los Santos Police Department",
                              colour=0x001cf0)

        embed.set_author(name="LSPD Human Resources")

        embed.add_field(name="Wie bewerbe ich mich beim LSPD?",
                        value="Gehe in den Kanal <#1244243748414820352> und öffne ein Bewerbungsticket.\nOb unsere Bewerbungsphase geöffnet ist findest du im Kanal <#1254188340731707534> heraus.",
                        inline=False)
        embed.add_field(name="Welche Anforderungen muss ich erfüllen?",
                        value="- Visum 10\n- Straffreie Akte - Wenn du dir unsicher bist, ob du eine straffreie Akte hast, komme zum LSPD. Wir gewähren dir Akteneinsicht.\n- OOC Alter 16\n- Kenntnisse über die Gesetze\n- Waffenschein + Führerschein",
                        inline=False)
        embed.add_field(name="Ich bin bei der Organisation X. Wie kann ich zum LSPD wechseln?",
                        value="Frage bei deiner Personalabteilung(HR) nach einem Orgawechsel. Wenn deine HR diese bei uns anfragt und wir diesen genehmigen.",
                        inline=False)
        embed.add_field(name="Mein Ticket wurde abgelehnt! - Warum?",
                        value="Warum du abgelehnt wurdest, siehst du im Ticket.\nFolgende Gründe könnten es sein:\n- Du konntest uns nicht überzeugen.\n- Wir haben kein Interesse an einer Zusammenarbeit.\n- Du hast den Theorietest nicht bestanden.\n- Du hast 24h nicht auf unseren Nachrichten reagiert.\n- Du hast nicht alle Voraussetzungen erfüllt.\n-# Das sind ausgewählte Gründe. Du kannst auch wegen etwas anderes abgelehnt worden sein, sofern es nicht in deinem Ticket steht\n**WICHTIG** zu beachten ist, dass wir Tickets nicht einfach so schließen.",
                        inline=False)
        embed.add_field(name="Mir antwortet keiner!",
                        value="Du bist nicht der einzige Bewerber. Bitte gedulde dich. Eine Antwort kann bis zu 48 Stunden dauern.\nAchte bitte darauf uns nicht mit deinen Nachrichten zu überschütten. Das kann zu einer Ablehnung führen.",
                        inline=False)

        embed.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")

        file = discord.File("LSPD.png")
        embed.set_image(url="attachment://LSPD.png")
        await ctx.respond(f"Sehr geehrte/r {"" if ping else "Bewerber"}", embed=embed, file=file, ephemeral=False)


def setup(bot):
    bot.add_cog(q_and_a(bot))
