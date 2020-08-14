import discord
from discord.ext import commands
from datetime import datetime
from pytz import timezone
from pytz import all_timezones

fmt = "%Y-%m-%d %H:%M:%S %Z%z"


# Cogs - Ignore
class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    # ================================

    @commands.command()
    async def timein(self, ctx, arg):
    # Convert to timezone of choice
        now_utc = datetime.now(timezone('UTC'))
        # Change US/Alaska to {arg} later.
        user_tz = now_utc.astimezone(timezone('US/Alaska'))
            await channel.send_message(f'It is currently {user_tz} at that timezone')

# Cogs - Ignore
def setup(client):
    client.add_cog(Example(client))
# ================================
