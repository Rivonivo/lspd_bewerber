import os, discord
import ezcord, aiohttp

from dotenv import load_dotenv
activity = discord.CustomActivity(name="LSPD x Human Resources")
load_dotenv()
bot = ezcord.Bot(intents=discord.Intents.all(), help_command=None, activity=activity,
                 error_webhook_url="https://discord.com/api/webhooks/1275829346325626911/HoXYN_f3BqJ9DCstk7Albp-S4Ssd-0bdWHeTbdQwmL1LAnWj8DhVbrg2K0ehTBWR2sfO",
                 owner_id=701025570695282739,
                 description="LSPD x HR")



if __name__ == "__main__":
    bot.load_cogs("cogs")
    bot.run(os.getenv('TOKEN'))