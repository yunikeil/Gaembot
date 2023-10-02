from datetime import datetime as dt

from nextcord.ext import commands


class ServerTestsCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    def __del__(self):
        ...

    @commands.command()
    async def runtest(self, ctx: commands.Context, autosend=0, info=0):
        import tests
        t = dt.now()
        thread = await ctx.message.create_thread(
            name=f"all_tests {t.hour}:{t.minute}:{t.second}"[-100:]
        )
        await tests.start_all(
            bot=self.bot,
            thread=thread,
            autosend=int(autosend),
            info=int(info),
        )
        await thread.edit(archived=True)



def setup(bot: commands.Bot) -> None:
    print("ServerTestsCog.py loaded")
    bot.add_cog(ServerTestsCog(bot))
