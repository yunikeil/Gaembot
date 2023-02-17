from discord.ext.commands import Bot, Cog, slash_command

from gameCirulli import GameCirulli


class GamesCog(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def __del__(self):
        ...

    @slash_command(name="2048", description="A simple GameCirulli command.")
    async def ping(self, inter) -> None:
        game = GameCirulli(5)
        await inter.respond(content=game.data)


def setup(bot: Bot) -> None:
    print("gamesGog.py loaded")
    bot.add_cog(GamesCog(bot))
