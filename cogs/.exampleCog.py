from discord.ext.commands import Bot, Cog, slash_command


class Ping(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def __del__(self):
        ...

    @slash_command(name="ping", description="A simple ping command.")
    async def ping(self, inter) -> None:
        await inter.respond(f"Pong! {self.bot.latency * 1000:.2f}ms")


def setup(bot: Bot) -> None:
    print("ping.py loaded")
    bot.add_cog(Ping(bot))
