import asyncio
import urllib
import requests
from typing import Literal, Optional

import nextcord
from nextcord.ext import commands, tasks
from nextcord.ext.commands import Bot, Cog, Context

from ..extensions.EXFormatExtension import ex_format


class ServerStatsCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.on_init.start()
        self.online_members.start()

    @tasks.loop(count=1)
    async def on_init(self):
        pass

    def cog_unload(self):
        self.online_members.stop()
        pass

    @tasks.loop(minutes=6) # таск на онлайн на сервере
    async def online_members(self):
        try:
            voice_members = set()
            guild = self.bot.get_guild(1075733298371899433)
            online = len(list(filter(lambda x: x.status == nextcord.Status.online, guild.members)))
            idle = len(list(filter(lambda x: x.status == nextcord.Status.idle, guild.members)))
            dnd = len(list(filter(lambda x: x.status == nextcord.Status.dnd, guild.members)))
            all_online = online+idle+dnd
            for voice in guild.voice_channels:
                for member in voice.members:
                    voice_members.add(member.id)
            voices_online = len(voice_members)
            await self.bot.get_channel(int(1143333689015685120)).edit(name=f'👥〡members-{len(guild.members)}')
            await self.bot.get_channel(int(1143333714437357579)).edit(name=f'🟢〡online-{all_online}')
            await self.bot.get_channel(int(1143592654517575741)).edit(name=f'🔊〡in-voices-{voices_online}')
            await self.bot.get_channel(int(1143333745311617154)).edit(name=f'🎮〡games-{0}')
        except BaseException as ex:
            print(ex_format(ex, "on_voice_helper"))


# on_ready cog!
def setup(bot: Bot):
    print("ServerStatsCog loaded!")
    bot.add_cog(ServerStatsCog(bot))
