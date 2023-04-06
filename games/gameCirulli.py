import nextcord
from PIL import Image, ImageDraw, ImageFont


from random import randint


class GameCirulliStartView(nextcord.ui.View):
    """
    Зависит от решения в будущем.
    Данный класс будет развиваться, в случае если базового функционала слэш команд не хватит для 
     реализации настройки одной из игр...
    """
    pass


class GameCirulliView(nextcord.ui.View):
    def __init__(self, game):
        raise "Данный класс ни где не используется!"
        super().__init__()
        self.game = game


    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, label="\u200b", row=1, disabled=True)
    async def puff_left(self, button: nextcord.ui.Button):
        button.disabled = True
        pass

    @nextcord.ui.button(label="⬆", style=nextcord.ButtonStyle.green, row=1)
    async def move_up_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        ...
        self.game.move_up()
        data = '\n'.join('\t'.join(map(str, row)) for row in self.game.data)
        await interaction.response.edit_message(content=f"2048\n{data}", view=self)

    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, label="\u200b", row=1, disabled=True)
    async def puff_right(self, button: nextcord.ui.Button):
        pass

    @nextcord.ui.button(label="⬅", style=nextcord.ButtonStyle.green, row=2)
    async def move_left_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        ...
        self.game.move_left()
        data = '\n'.join('\t'.join(map(str, row)) for row in self.game.data)
        await interaction.response.edit_message(content=f"2048\n{data}", view=self)

    @nextcord.ui.button(label="⬇", style=nextcord.ButtonStyle.green, row = 2)
    async def move_down_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        ...
        self.game.move_down()
        data = '\n'.join('\t'.join(map(str, row)) for row in self.game.data)
        await interaction.response.edit_message(content=f"2048\n{data}", view=self)
    
    @nextcord.ui.button(label="➡", style=nextcord.ButtonStyle.green, row=2)
    async def move_right_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        ...
        self.game.move_right()
        data = '\n'.join('\t'.join(map(str, row)) for row in self.game.data)
        await interaction.response.edit_message(content=f"2048\n{data}", view=self)

    ...


class GameCirulli(nextcord.ui.View):
    def __init__(self, size: int):
        """
        Конструктор
        На вход, при создании объекта передаётся размер квадрата
        Также тут объявляются все глобальные для класса поля,
         которые будут использоваться в последующих методах.
        """
        super().__init__()
        self.size = size
        self.data: list[list[int]] = [
            [0 for x in range(size)] for y in range(size)
        ]

    def __del__(self):
        """
        Деконструктор
        Можно использоавть для сохранения результатов и тд и тп..
        Пока не трогаем.
        """
        ...

    def drow_matrix(self):
        ...

    def generate_points(self):
        ...

    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, label="\u200b", row=1, disabled=True)
    async def puff_left_button(self, button: nextcord.ui.Button):
        button.disabled = True
        pass

    @nextcord.ui.button(label="⬆", style=nextcord.ButtonStyle.green, row=1)
    async def move_up_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        ...
         
    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, label="\u200b", row=1, disabled=True)
    async def puff_right_button(self, button: nextcord.ui.Button):
        button.disabled = True
        pass

    @nextcord.ui.button(label="⬅", style=nextcord.ButtonStyle.green, row=2)
    async def move_left_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
       ...

    @nextcord.ui.button(label="⬇", style=nextcord.ButtonStyle.green, row = 2)
    async def move_down_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        ...

    @nextcord.ui.button(label="➡", style=nextcord.ButtonStyle.green, row=2)
    async def move_right_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
       ...
