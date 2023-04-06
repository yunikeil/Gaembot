import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext.commands import Cog
from nextcord.ext import commands, tasks
from nextcord.ext.commands import Bot, Cog, Context

from configuration import test_guilds
from games.ticTacToe import TicTacToe
from games.gameCirulli import GameCirulliStartView, GameCirulliView
from games.gameCheckers import TempVar


class GamesSelect(nextcord.ui.Select):
    """
    Класс представляющий из себя item GamesSelectView.
    Служит выпадающим меню с выбором игр.
    """
    def __init__(self):
        options = [
            nextcord.SelectOption(label="2048", description="Create solo game"),
            nextcord.SelectOption(label="Tic-Tac-Toe", description="Create duo game"),
            nextcord.SelectOption(label="Checkers", description="Create duo game")
        ]
        super().__init__(
            custom_id="GamesCog:GamesSelect",
            placeholder="Выберите интересующую вас игру...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: nextcord.Interaction):
        await interaction.response.send_message()  # !!!


class GamesSelectView(nextcord.ui.View):
    """
    Класс представляющий из себя обёртку для GamesSelect.
    Служит выпадающим меню с выбором игр.
    """
    def __init__(self):
        super().__init__()
        self.timeout = None 
        self.add_item(GamesSelect())


class GamesCog(Cog):
    """
    Класс-команда, предоставляющий возможность выбора игр из выпадающего меню.
    Создаёт сообщение, поддерживает его рабочее состояние а также обрабатывает входящие запросы.
    """
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def __del__(self):
        ...

    @commands.command()
    async def games_select_message(self, ctx: Context):
        """
        Отправляет сообщение с выпадающим меню выбора игры.

        :param ctx: объект класса Context
        :type ctx: nextcord.ext.commands.Context
        """
        ...


def setup(bot: Bot) -> None:
    """
    Функция для добавления команды GamesCog в бота.

    :param bot: объект класса Bot
    :type bot: nextcord.ext.commands.Bot
    """
    print("GamesCog.py loaded")
    bot.add_cog(GamesCog(bot))
