from random import randint

import nextcord
from PIL import Image, ImageDraw, ImageFont


class GameCirulliStartView(nextcord.ui.View):
    """
    Класс, отвечающий за создание представления для старта игры в 2048.
    Содержит стартовый Embed, кнопку и селектор.
    """


class GameCirulliView(nextcord.ui.View):
    """
    Класс для игры в 2048.

    Атрибуты:
        size (int): размер поля игры.

    Методы:
        drow_matrix: отрисовка матрицы игры.
        generate_points: генерация новой точки в матрице.
        move_up_button: кнопка для движения вверх.
        move_down_button: кнопка для движения вниз.
        move_left_button: кнопка для движения влево.
        move_right_button: кнопка для движения вправо.
    """

    def __init__(self, size: int):
        """
        Создает новую игру в 2048.

        :param size: размер поля игры.
        :type size: int
        """
        super().__init__()
        self.size = size
        self.data: list[
            list[int]] = [
            [0 for x in range(size)] for y in range(size)
        ]

    def __del__(self):
        """
        Используется для сохранения результатов игры.
        В разработке.
        """

        ...

    def drow_matrix(self):
        """
        Отрисовка матрицы игры.
        """

        ...

    def generate_points(self):
        """
        Генерация новой точки в матрице.
        """

        ...

    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, label="\u200b", row=1, disabled=True)
    async def puff_left_button(self, button: nextcord.ui.Button):      
        """
        Вспомогательная кнопка для движения влево.

        :param button: Кнопка.
        :type button: nextcord.ui.Button
        """
        button.disabled = True
        pass

    @nextcord.ui.button(label="⬆", style=nextcord.ButtonStyle.green, row=1)
    async def move_up_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        """
        Кнопка для движения вверх.

        :param button: кнопка.
        :type button: nextcord.ui.Button
        :param interaction: объект взаимодействия с дискордом.
        :type interaction: nextcord.Interaction
        """

        ...

    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, label="\u200b", row=1, disabled=True)
    async def puff_right_button(self, button: nextcord.ui.Button):
        """
        Вспомогательная кнопка для движения вправо.

        :param button: кнопка.
        :type button: nextcord.ui.Button
        """
        button.disabled = True
        pass

    @nextcord.ui.button(label="⬅", style=nextcord.ButtonStyle.green, row=2)
    async def move_left_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        """
        Кнопка для движения влево.

        :param button: кнопка.
        :type button: nextcord.ui.Button
        :param interaction: объект взаимодействия с дискордом.
        :type interaction: nextcord.Interaction
        """

        ...

    @nextcord.ui.button(label="⬇", style=nextcord.ButtonStyle.green, row=2)
    async def move_down_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        """
        Кнопка для движения вниз.

        :param button: кнопка.
        :type button: nextcord.ui.Button
        :param interaction: объект взаимодействия с дискордом.
        :type interaction: nextcord.Interaction
        """

        ...

    @nextcord.ui.button(label="➡", style=nextcord.ButtonStyle.green, row=2)
    async def move_right_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        """
        Кнопка для движения вправо.

        :param button: кнопка.
        :type button: nextcord.ui.Button
        :param interaction: объект взаимодействия с дискордом.
        :type interaction: nextcord.Interaction
        """

        ...
