import os, discord
import ezcord, aiohttp

from dotenv import load_dotenv
activity = discord.CustomActivity(name="LSPD x Human Resources")
load_dotenv()
bot = ezcord.Bot(intents=discord.Intents.all(), help_command=None, activity=activity,
                 error_webhook_url="https://discord.com/api/webhooks/1275829346325626911/HoXYN_f3BqJ9DCstk7Albp-S4Ssd-0bdWHeTbdQwmL1LAnWj8DhVbrg2K0ehTBWR2sfO",
                 owner_id=701025570695282739,
                 description="LSPD x HR")






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