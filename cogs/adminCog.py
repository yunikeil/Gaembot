import nextcord
from nextcord.ext.commands import Bot, Cog


class AdminCog(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def __del__(self):
        ...

    
def setup(bot: Bot) -> None:
    print("adminCog.py loaded")
    bot.add_cog(AdminCog(bot))
