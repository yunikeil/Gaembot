import nextcord
from nextcord.ext.commands import Bot, Cog

from gameCirulli import GameCirulli


class GamesCog(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def __del__(self):
        ...

    @nextcord.slash_command(name="ping", description="A simple ping command.", guild_ids=[1075733298371899433])
    async def ping(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"Pong! {self.bot.latency * 1000:.2f}ms")
 

def setup(bot: Bot) -> None:
    print("gamesGog.py loaded")
    bot.add_cog(GamesCog(bot))
