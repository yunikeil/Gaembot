import nextcord
from nextcord.ext import commands

import datetime


bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.all())


@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.command()
async def fullembed(ctx):

    embed = nextcord.Embed(
        title="Embed Title",
        description="Embed Description",
        color=nextcord.Colour.yellow(),
        url="https://awesomereviews.ru/wp-content/uploads/2016/06/Holo1.jpg",
        timestamp=datetime.datetime.now(),
    )

    embed.set_author(
        name="Embed Author",
        url="https://awesomereviews.ru/wp-content/uploads/2016/06/Holo1.jpg",
        icon_url="https://awesomereviews.ru/wp-content/uploads/2016/06/Holo1.jpg",
    )

    embed.set_thumbnail(url="https://awesomereviews.ru/wp-content/uploads/2016/06/Holo1.jpg")

    embed.set_image(url="https://awesomereviews.ru/wp-content/uploads/2016/06/Holo1.jpg")

    embed.add_field(name="Regular Title", value="Regular Value", inline=False)

    embed.add_field(name="Inline Title", value="Inline Value", inline=True)
    embed.add_field(name="Inline Title", value="Inline Value", inline=True)
    embed.add_field(name="Inline Title", value="Inline Value", inline=True)

    embed.set_footer(
        text="Embed Footer",
        icon_url="https://awesomereviews.ru/wp-content/uploads/2016/06/Holo1.jpg",
    )

    await ctx.send(embed=embed)


bot.run('MTA3NTcyMzg4MzEzNjY4NDEwMw.GePhqJ.cCZcO4ztwCvJn-Bn3j2QXJjDhCVP7cqwgYHC3o')
