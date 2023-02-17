# This example requires the 'members' privileged intent to use the Member converter.

import discord
from discord import SlashCommandGroup
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(debug_guilds=[1075733298371899433],
                  intents=intents, owner_id=286914074422280194)


class Example(commands.Cog):
    def __init__(self, bot_: discord.Bot):
        self.bot = bot_

    greetings = SlashCommandGroup(name="greetings",
                                  description="Various greeting from cogs!",
                                  guild_ids=[1075733298371899433])

    @commands.Cog.listener()
    async def on_application_command_error(
        self, ctx: discord.ApplicationContext, error: discord.DiscordException
    ):
        if isinstance(error, commands.NotOwner):
            await ctx.respond("You can't use that command!")
        else:
            await ctx.respond(f"```\n{error}\n```")


bot.add_cog(Example(bot))  # Put in a setup function for cog files
# Main file
bot.run("MTA3NTcyMzg4MzEzNjY4NDEwMw.GePhqJ.cCZcO4ztwCvJn-Bn3j2QXJjDhCVP7cqwgYHC3o")
