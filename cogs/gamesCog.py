import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext.commands import Cog

from main import Bot
from configuration import test_guilds
from games.ticTacToe import TicTacToe
from games.gameCirulli import GameCirulli


class GamesCog(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def __del__(self):
        ...

    @nextcord.slash_command(name="start", description="Group start command!", guild_ids=test_guilds)
    async def create_game(self, interaction: Interaction):
        pass

    @create_game.subcommand(name="play", description="Create a new game!")
    async def cirulli_game(
        self,
        interaction: Interaction,
        game_name: int = SlashOption(
            name="game",
            description="The game you want",
            choices={"2048": 1, "Checkers": 2, "Tic Tac Toe": 3}
        ),
    ):

        """
        Тут будет отправка сообщений о настройках игры и общая логика сообщений дискорда
        """

        if game_name == 3:
            await interaction.response.send_message(f"Tic Tac Toe: X goes first", view=TicTacToe())
        else:
            await interaction.response.send_message(f"This is {game_name}!")


def setup(bot: Bot) -> None:
    print("gamesGog.py loaded")
    bot.add_cog(GamesCog(bot))
