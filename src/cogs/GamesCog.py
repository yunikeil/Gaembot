import nextcord
from nextcord.ext.commands import Cog
from nextcord.ext import commands, tasks
from nextcord.ext.commands import Bot, Cog, Context

from configuration import test_guilds
from games.ticTacToeGame import TicTacToeStartView
from games.CirulliGame import GameCirulliStartView
from games.CheckersGame import GameCheckersStartView


class GamesSelect(nextcord.ui.Select):
    """
    Класс представляющий из себя item GamesSelectView.
    Служит выпадающим меню с выбором игр.
    (Для внутреннего использования в коде)
    """

    def __init__(self, bot: Bot):
        self.bot = bot
        options = [
            nextcord.SelectOption(label="2048", description="Create solo game"),
            nextcord.SelectOption(label="Tic-Tac-Toe", description="Create duo game"),
            nextcord.SelectOption(label="Checkers", description="Create duo game"),
            nextcord.SelectOption(
                label="Очистить выбор", description="Для очистики выбора"
            ),
        ]
        super().__init__(
            placeholder="Выберите интересующую вас игру...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: nextcord.Interaction):
        games = {
            "2048": [GameCirulliStartView, 1093504817260929054],
            "Tic-Tac-Toe": [TicTacToeStartView, 1093504589736726528],
            "Checkers": [GameCheckersStartView, 1093504876056682630],
        }
        if self.values[0] != "Очистить выбор":
            guild = interaction.guild
            creator = interaction.user.name
            role = guild.get_role(games[self.values[0]][1])
            if role in interaction.user.roles:
                game_start_view = games[self.values[0]][0]()
                category = nextcord.utils.get(
                    guild.categories, id=game_start_view.category_id
                )
                channel = await guild.create_text_channel(
                    f"{creator} создал {self.values[0]} игру", category=category
                )
                await interaction.response.send_message(
                    f"Создана команата <#{channel.id}>\nПриятной игры!", ephemeral=True
                )
                await channel.send(view=game_start_view)
            else:
                await interaction.response.send_message(
                    f"У вас нет данной роли: <@&{games[self.values[0]][1]}>",
                    ephemeral=True
                )

class GamesSelectView(nextcord.ui.View):
    """
    Класс представляющий из себя обёртку для GamesSelect.
    Служит выпадающим меню с выбором игр.
    (Для внутреннего использования в коде)
    """

    def __init__(self, bot):
        super().__init__(prevent_update=False)
        self.timeout = None
        self.add_item(GamesSelect(bot=bot))


class GamesCog(Cog):
    """
    Класс-команда, предоставляющий возможность выбора игр из выпадающего меню.
    Создаёт сообщение, поддерживает его рабочее состояние а также обрабатывает входящие запросы.
    (Для внутреннего использования в коде)
    """

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def __del__(self):
        pass

    def cog_unload(self):
        self.bot.remove_view(GamesSelectView())

    @commands.command()
    async def games_select_message(self, ctx: Context):
        """
        Команда, которая отправляет сообщение с выпадающим меню выбора игры.

        :param ctx: объект класса Context
        :type ctx: nextcord.ext.commands.Context
        """

        await ctx.message.delete()
        await ctx.channel.send("Выберите игру:", view=GamesSelectView(bot=self.bot))
        ...


def setup(bot: Bot) -> None:
    """Функция для добавления команды GamesCog в бота.
    (используется внутри библиотеки)

    :param bot: объект класса Bot
    :type bot: nextcord.ext.commands.Bot
    """

    print("GamesCog.py loaded")
    bot.add_view(GamesSelectView())
    bot.add_cog(GamesCog(bot))
