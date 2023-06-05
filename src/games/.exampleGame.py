import nextcord


class ExampletartView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=120)
        self.category_id: int = ...

    @nextcord.ui.button(label="Начать игру!", style=nextcord.ButtonStyle.green)
    async def start(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        button.disabled = True
        ...
        await interaction.message.edit(view=self)
        await interaction.response.send_message(...)


class  ExampleView(nextcord.ui.View):
    def __init__(self, size: int):
        super().__init__()
        ...

    def __del__(self):
        ...

    ...
