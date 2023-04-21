import asyncio
from abc import ABC
from traceback import format_exception

import nextcord
from nextcord.ext import commands
import aeval

import configuration


class Bot(commands.Bot, ABC):
    def __init__(self, **options):
        super().__init__(command_prefix='>',
                         help_command=None,
                         intents=nextcord.Intents.all(),
                         **options)

        self.DATA: dict = {
            'bot-started': False
        }
        self.OWNERS: list[int] = []
        self.EVAL_OWNER: list[int] = []
        self.config: object = configuration

    async def on_ready(self):
        if not self.DATA['bot-started']:
            application_info = await self.application_info()
            self.OWNERS.append(application_info.owner.id)
            self.EVAL_OWNER.append(application_info.owner.id)
            self.DATA['bot-started'] = True
        print(f"Logged in as {self.user} (ID: {self.user.id})\n------")
        cogs_add_on_start: list[str] = ["gamesCog"]
        if cogs_add_on_start:
            [bot.load_extension(f"cogs.{cog}") for cog in cogs_add_on_start]
        

    async def on_command_error(self, ctx, error):
        if isinstance(error, nextcord.ext.commands.CommandNotFound):
            return
        raise error

    
    ...


bot = Bot()


@bot.command()
async def cog_load(ctx: commands.Context, cog: str):
    if ctx.author.id not in bot.OWNERS:
        return
    try:
        bot.load_extension(f"cogs.{cog}")
    except BaseException as ex:
        await ctx.channel.send(f"Exception:\n```bash\n{ex}\n```")
    else:
        await ctx.channel.send(f"```cog.{cog} loaded!```")


@bot.command()
async def cog_unload(ctx: commands.Context, cog: str):
    if ctx.author.id not in bot.OWNERS:
        return
    try:
        bot.unload_extension(f"cogs.{cog}")
    except BaseException as ex:
        await ctx.channel.send(f"Exception:\n```bash\n{ex}\n```")
    else:
        await ctx.channel.send(f"```Cog cog.{cog} unloaded!```")


@bot.command()
async def cog_reload(ctx: commands.Context, cog: str):
    if ctx.author.id not in bot.OWNERS:
        return
    try:
        bot.unload_extension(f"cogs.{cog}")
        await asyncio.sleep(1)
        bot.load_extension(f"cogs.{cog}")
    except BaseException as ex:
        await ctx.channel.send(f"Exception:\n```bash\n{ex}\n```")
    else:
        await ctx.channel.send(f"```Cog cog.{cog} reloaded!```")


@bot.command()
async def eval(ctx, *, content):
    if ctx.author.id not in bot.EVAL_OWNER:
        return
    standart_args = {
        "nextcord": nextcord,
        "commands": commands,
        "bot": bot,
        "ctx": ctx,
        "asyncio": asyncio,
    }
    
    try:
        await aeval.aeval(content, standart_args, {})
    except Exception as ex:
        result = "".join(format_exception(ex, ex, ex.__traceback__))
        await ctx.channel.send(f"Exception:\n```bash\n{result.replace('```', '`')}\n```")


if __name__ == "__main__":
    bot.run(bot.config.token_dis)
