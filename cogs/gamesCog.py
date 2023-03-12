import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext.commands import Cog

import io

from main import Bot
from ..configuration import test_guilds
from games.ticTacToe import TicTacToe
from games.gameCirulli import GameCirulli, GameCirulliView


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
        game_name: str = SlashOption(
            name="game",
            description="The game you want",
            choices=["2048", "Tic Tac Toe", "Checkers"]
        ),
    ):

        """
        Тут будет отправка сообщений о настройках игры и подключение новых кнопок (от классов игры)
        """
        if game_name == "2048":
            game = GameCirulli(4)
            data = '\n'.join('\t'.join(map(str, row)) for row in game.data)
            e = nextcord.Embed()
            e.set_image(url=)
            #byte_im = buf.getvalue()
            """
            Во первых можно изменить всё 
            СОздаётся сообщение с настройкой после кидает на новый канал игры определённого пользователя
            и там работа идёт с сообщениями а не командами приложений.
            Также есть вариант временного сохранения картинки и чтения его после
            """
            await interaction.response.send_message(f"2048\n{data}", view=GameCirulliView(game))
        elif game_name == "Tic Tac Toe":
            await interaction.response.send_message(f"Tic Tac Toe: X goes first", view=TicTacToe())
        else:
            """
            @nextcord.ui.button(label="0", style=nextcord.ButtonStyle.red)
            async def count(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                number = int(button.label) if button.label else 0
                if number >= 10:
                    button.style = nextcord.ButtonStyle.green
                    button.disabled = True
                button.label = str(number + 1)
                await interaction.response.edit_message(view=self)
            """
            await interaction.response.send_message(f"This is {game_name}!")


def setup(bot: Bot) -> None:
    print("gamesGog.py loaded")
    bot.add_cog(GamesCog(bot))
