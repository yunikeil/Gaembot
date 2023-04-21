import nextcord
from PIL import Image, ImageDraw, ImageFont


from random import randint


class GameCirulliStartView(nextcord.ui.View):
    # need code here
    ...


class GameCirulliView(nextcord.ui.View):
    def __init__(self, size: int):
        """
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
        # need code here
        ...

    def generate_points(self):
        # need code here
        ...

    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, label="\u200b", row=1, disabled=True)
    async def puff_left_button(self, button: nextcord.ui.Button):
        button.disabled = True
        pass

    @nextcord.ui.button(label="⬆", style=nextcord.ButtonStyle.green, row=1)
    async def move_up_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        # need code here
        ...
         
    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, label="\u200b", row=1, disabled=True)
    async def puff_right_button(self, button: nextcord.ui.Button):
        button.disabled = True
        pass

    @nextcord.ui.button(label="⬅", style=nextcord.ButtonStyle.green, row=2)
    async def move_left_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        # need code here
        ...

    @nextcord.ui.button(label="⬇", style=nextcord.ButtonStyle.green, row = 2)
    async def move_down_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        # need code here
        ...

    @nextcord.ui.button(label="➡", style=nextcord.ButtonStyle.green, row=2)
    async def move_right_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        # need code here
        ...
