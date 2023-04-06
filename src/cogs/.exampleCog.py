import nextcord
from nextcord.ext.commands import Bot, Cog


class Ping(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def __del__(self):
        ...

    @nextcord.slash_command(guild_ids=[], description="A simple ping command.")
    async def ping(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"Pong! {self.bot.latency * 1000:.2f}ms")


def setup(bot: Bot) -> None:
    print("ping.py loaded")
    bot.add_cog(Ping(bot))
