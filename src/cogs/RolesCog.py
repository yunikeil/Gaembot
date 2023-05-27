import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Cog, Context


class RolesSelectView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.timeout = None

    @nextcord.ui.button(label="2048", style=nextcord.ButtonStyle.green)
    async def first_game(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        member, guild = interaction.user, interaction.guild
        role = guild.get_role(1093504817260929054)
        if role in member.roles:
            await member.remove_roles(role)
            await interaction.response.send_message("Удалена 2048 роль", ephemeral=True)
        else:
            await member.add_roles(role)
            await interaction.response.send_message("Добавлена 2048 роль", ephemeral=True)
    
    @nextcord.ui.button(label="Tic-Tac-Toe", style=nextcord.ButtonStyle.green)
    async def second_game(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        member, guild = interaction.user, interaction.guild
        role = guild.get_role(1093504589736726528)
        if role in member.roles:
            await member.remove_roles(role)
            await interaction.response.send_message("Удалена Tic-Tac-Toe роль", ephemeral=True)
        else:
            await member.add_roles(role)
            await interaction.response.send_message("Добавлена Tic-Tac-Toe роль", ephemeral=True)
    
    @nextcord.ui.button(label="Checkers", style=nextcord.ButtonStyle.green)
    async def third_game(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        member, guild = interaction.user, interaction.guild
        role = guild.get_role(1093504876056682630)
        if role in member.roles:
            await member.remove_roles(role)
            await interaction.response.send_message("Удалена Checkers роль", ephemeral=True)
        else:
            await member.add_roles(role)
            await interaction.response.send_message("Добавлена Checkers роль", ephemeral=True)


class RolesCog(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def __del__(self):
        ...
    
    @commands.command()
    async def role_select_message(self, ctx: Context):
        await ctx.message.delete()
        await ctx.channel.send("Выберите роль:", view=RolesSelectView())


def setup(bot: Bot) -> None:
    print("RolesCog.py loaded")
    bot.add_cog(RolesCog(bot))
