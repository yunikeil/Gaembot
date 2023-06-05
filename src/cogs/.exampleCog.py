import nextcord
from nextcord.ext.commands import Bot, Cog, command


class ExampleCog(Cog):
    def __init__(self, bot: Bot) -> None:
        bot.sync_all_application_commands()
        self.bot = bot

    def __del__(self):
        ...

    async def on_init(self):
        pass

    @command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {self.bot.latency * 1000:.2f}ms")

    @nextcord.slash_command(guild_ids=[], description="A simple ping command.")
    async def ping(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"Pong! {self.bot.latency * 1000:.2f}ms")


def setup(bot: Bot) -> None:
    print(".exampleCog.py loaded")
    bot.add_cog(ExampleCog(bot))
