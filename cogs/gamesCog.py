import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import Cog

import io

from ..configuration import test_guilds
from ..games.ticTacToe import TicTacToe, TicTacToeStartView
from ..games.gameCirulli import GameCirulliView, GameCirulliStartView


class GamesView(nextcord.ui.View):
    def __init__():
        ...
    # need code here
    ...


class GamesCog(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def __del__(self):
        ...

    @commands.command()
    async def games_msg(self, ctx):
        # need code here
        ...

def setup(bot: Bot) -> None:
    print("gamesGog.py loaded")
    bot.add_cog(GamesCog(bot))
