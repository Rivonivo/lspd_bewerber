import os, discord
import ezcord, aiohttp

from dotenv import load_dotenv
activity = discord.CustomActivity(name="LSPD x Human Resources")
load_dotenv()
bot = ezcord.Bot(intents=discord.Intents.all(), help_command=None, activity=activity,
                 error_webhook_url="https://discord.com/api/webhooks/1275829346325626911/HoXYN_f3BqJ9DCstk7Albp-S4Ssd-0bdWHeTbdQwmL1LAnWj8DhVbrg2K0ehTBWR2sfO",
                 owner_id=701025570695282739,
                 description="LSPD x HR")


@bot.slash_command(integration_types={discord.IntegrationType.user_install}, name="q_and_a", description="Sende den Q&A Webhook")
async def _faq(ctx: discord.ApplicationContext, webhook_url: str):
    role_id = 1264670715718926346
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(
            webhook_url,
            session=session,
            bot_token=os.getenv('TOKEN'),
        )
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
        await webhook.send(f"Sehr geehrte/r Bewerber", embed=embed, username="LSPD Bewerbungshelfer", avatar_url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png", file=file)
        await ctx.respond("Webhook gesendet", ephemeral=False, delete_after=5)





@bot.slash_command(integration_types={discord.IntegrationType.user_install}, name="bewerbungsinfo", description="Sende die Bewerbungsinfo")
async def _fragenueberfragen(ctx: discord.ApplicationContext):
    embed1 = discord.Embed(title="Reguläre Bewerbung",
                           description="Du möchtest für Recht und Ordnung auf den Straßen von Los Santos sorgen?\nBewerbe dich als Officer beim Los Santos Police Department!",
                           colour=0x00ff00)

    embed1.set_author(name="Geöffnet")

    embed1.set_image(url="https://i.ibb.co/pQkWG2r/ersteinstellung.png")

    embed1.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")
    await ctx.send_response(f" ", embed=embed1)
    embed2 = discord.Embed(title="Wiedereinstellung",
                           description="Du warst schon mal bei uns? Mache eine Wiedereinstellung und sorge für Recht und Ordnung",
                           colour=0x00ff00)

    embed2.set_author(name="Geöffnet")

    embed2.set_image(url="https://i.ibb.co/0sS2BXx/wiedereinstellung.png")

    embed2.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")
    await ctx.send_followup(f" ", embed=embed2)
    embed3 = discord.Embed(title="Orgawechsel",
                           description="Du bist z.B. in der Regierung tätig und möchtest was neues probieren. Frage einen Orgawechsel bei deiner HR an und erstelle eine Bewerbung!",
                           colour=0x00ff00)

    embed3.set_author(name="Geöffnet")

    embed3.set_image(url="https://i.ibb.co/L0Fq0hj/orgawechsel.png")

    embed3.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")
    await ctx.send_followup(f" ", embed=embed3)
    embed4 = discord.Embed(title="Beschleunigtes Verfahren",
                           description="DU wurdest vom LSPD empfohlen? Dann eröffne eine Bewerbung beim LSPD!",
                           colour=0x00ff00)

    embed4.set_author(name="Geöffnet")

    embed4.set_image(url="https://i.ibb.co/NsBCHvs/beschleunigt.png")

    embed4.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")
    await ctx.send_followup(f" ", embed=embed4)
    embed5 = discord.Embed(title="TOW Division",
                           description="Die Straßenverkehrsordnung ist deine Abendlektüre und du hast es satt Falschparker im Straßenverkehr zu sehen? Bewerbe dich als TOW Officer.",
                           colour=0xff0000)

    embed5.set_author(name="Geschlossen")
    embed5.set_image(url="https://i.ibb.co/NSsSfqR/tow.png")

    embed5.set_thumbnail(url="https://i.ibb.co/TrBtV18/Bild-2024-08-15-180318116.png")
    await ctx.send_followup(f" ", embed=embed5)
    return






if __name__ == "__main__":
    bot.load_cogs("cogs")
    bot.run(os.getenv('TOKEN'))