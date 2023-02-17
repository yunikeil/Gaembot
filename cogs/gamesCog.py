import discord
from discord.ext import commands
from discord.ext.commands import Bot, Cog, slash_command

from gameCirulli import GameCirulli


class GamesCog(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def __del__(self):
        ...

    games = discord.SlashCommandGroup(name="games",
                                          description="Games group comand!",
                                          guild_ids=[1075733298371899433])

        

    @commands.Cog.listener()
    async def on_application_command_error(
        self, ctx: discord.ApplicationContext, error: discord.DiscordException
    ):
        if isinstance(error, commands.NotOwner):
            await ctx.respond("You can't use that command!")
        else:
            await ctx.respond(f"```\n{error}\n```")


def setup(bot: Bot) -> None:
    print("gamesGog.py loaded")
    bot.add_cog(GamesCog(bot))
