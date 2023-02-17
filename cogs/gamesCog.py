import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands
from discord.ext.commands import Bot, Cog, slash_command

from gameCirulli import GameCirulli


class GamesCog(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def __del__(self):
        ...

    games = SlashCommandGroup(
        name="games",
        description="Games group command!",
        guild_ids=[1075733298371899433])

    @games.command()  # Create a slash command under the math group
    @discord.option("size", description="Enter your size of game", choices=["4x4 game", "5x5 game", "6x6 game"])
    async def game(self, ctx: discord.ApplicationContext):
        await ctx.respond("123")

    @Cog.listener()
    async def on_application_command_error(
        self, ctx: discord.ApplicationContext, error: discord.DiscordException
    ):
        if isinstance(error, commands.NotOwner):
            await ctx.respond("You can't use that command!")
        else:
            raise error


def setup(bot: Bot) -> None:
    print("gamesGog.py loaded")
    bot.add_cog(GamesCog(bot))
