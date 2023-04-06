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

    


def setup(bot: Bot) -> None:
    print("gamesGog.py loaded")
    bot.add_cog(GamesCog(bot))
