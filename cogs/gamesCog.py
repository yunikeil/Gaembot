import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext.commands import Cog

import io

from main import Bot
from ..configuration import test_guilds
from ..games.ticTacToe import TicTacToe
from ..games.gameCirulli import GameCirulli, GameCirulliView


class GamesCog(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def __del__(self):
        ...

    @nextcord.slash_command(name="start", description="Group start command!", guild_ids=test_guilds)
    async def create_game(self, interaction: Interaction):
        """
        Корень группы команд для создания игр. Нигде не используется.
        """
        pass

    @create_game.subcommand(name="play", description="Create a new game!")
    async def cirulli_game(
        self,
        interaction: Interaction,
        game_name: str = SlashOption(
            name="game",
            description="The game you want",
            choices=[
                "2048",
                "Tic Tac Toe",
                "Checkers"
            ]
        ),
    ):

        """
        Тут будет отправка сообщений о настройках игры и подключение новых кнопок (от классов игры)
        """
        if game_name == "2048":
            await interaction.response.send_message(
                f"2048"
            )
        elif game_name == "Tic Tac Toe":
            await interaction.response.send_message(
                f"Tic Tac Toe: X goes first", view=TicTacToe()
            )
        elif game_name == "Checkers":
            await interaction.response.send_message(f"This is Checkers!")


def setup(bot: Bot) -> None:
    print("gamesGog.py loaded")
    bot.add_cog(GamesCog(bot))
