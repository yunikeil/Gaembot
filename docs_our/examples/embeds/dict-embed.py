import nextcord
from nextcord.ext import commands

import datetime

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.all())


@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.command()
async def dictembed(ctx):

    embed_dict = {
        "title": "Embed Title",
        "description": "Embed Description",
        "color": 0xFEE75C,
        "timestamp": datetime.datetime.now().isoformat(),
        "author": {
            "name": "Embed Author",
            "url": "https://awesomereviews.ru/wp-content/uploads/2016/06/Holo1.jpg",
            "icon_url": "https://awesomereviews.ru/wp-content/uploads/2016/06/Holo1.jpg",
        },
        "thumbnail": {"url": "https://awesomereviews.ru/wp-content/uploads/2016/06/Holo1.jpg"},
        "fields": [
            {"name": "Regular Title", "value": "Regular Value", "inline": "false"},
            {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
            {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
            {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
            {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
            {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
            {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
            {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
            {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
            {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
        ],
        "image": {"url": "https://awesomereviews.ru/wp-content/uploads/2016/06/Holo1.jpg"},
        "footer": {
            "text": "Embed Footer",
            "icon_url": "https://awesomereviews.ru/wp-content/uploads/2016/06/Holo1.jpg",
        },
    }

    await ctx.send(embed=nextcord.Embed.from_dict(embed_dict))


bot.run('MTA3NTcyMzg4MzEzNjY4NDEwMw.GePhqJ.cCZcO4ztwCvJn-Bn3j2QXJjDhCVP7cqwgYHC3o')
