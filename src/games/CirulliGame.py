import os
import random
import string
import asyncio
from random import randint
from contextlib import contextmanager

import nextcord
from PIL import Image, ImageDraw, ImageFont


class Dropdown(nextcord.ui.Select):
    def __init__(self, ViewParrent):
        self.ViewParrent = ViewParrent
        # Set the options that will be presented inside the dropdown
        options = [
            nextcord.SelectOption(label="4", description="4x4"),
            nextcord.SelectOption(label="6", description="6x6"),
            nextcord.SelectOption(label="8", description="8x8"),
        ]

        super().__init__(
            placeholder="Choose your size 2048...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: nextcord.Interaction):
        self.ViewParrent.remove_item(self)
        self.ViewParrent.add_item(self.ViewParrent.button_saved)
        await interaction.message.edit(view=self.ViewParrent)
        game = GameCirulliView(size=int(self.values[0]))
        await interaction.response.send_message(view=game, file=game.drow_matrix())


class GameCirulliStartView(nextcord.ui.View):
    """
    Класс, отвечающий за создание представления для старта игры в 2048.
    Содержит стартовый Embed, кнопку и селектор.
    """

    def __init__(self, *, timeout: float | None = 180, auto_defer: bool = True) -> None:
        super().__init__(timeout=timeout, auto_defer=auto_defer)
        self.category_id: int = 1093504405149601875
        self.button_saved = None

    @nextcord.ui.button(label="Начать игру!", style=nextcord.ButtonStyle.green)
    async def start(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        button.disabled = True
        self.button_saved = button
        self.add_item(Dropdown(self))
        self.remove_item(button)
        await interaction.message.edit(view=self)


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
        file_dir = os.path.dirname(os.path.abspath(__file__))
        self.temp_path = os.path.join(file_dir, "temp")
        self.temp_files = []
        self.size = size
        self.buttons = [
            self.move_up_button,
            self.move_left_button,
            self.move_down_button,
            self.move_right_button,
        ]
        self.data: list[list[int]] = [[0 for x in range(size)] for y in range(size)]
        number = randint(1, 100)
        position1 = randint(1, size**2)
        position2 = randint(1, size**2)
        while position1 == position2:
            position2 = randint(1, size**2)
        if number < 79:
            self.data[(position1 - 1) // size][position1 % 4 - 1] = 2
            self.data[(position2 - 1) // size][position2 % 4 - 1] = 2
        elif number == 80:
            self.data[(position1 - 1) // size][position1 % 4 - 1] = 4
            self.data[(position2 - 1) // size][position2 % 4 - 1] = 4
        else:
            self.data[(position1 - 1) // size][position1 % 4 - 1] = 2
            self.data[(position2 - 1) // size][position2 % 4 - 1] = 4

    def __del__(self):
        """
        Используется для сохранения результатов игры.
        В разработке.
        """
        for filename in self.temp_files:
            os.remove(filename)

    def drow_matrix(self):
        """
        Отрисовка матрицы игры.
        """

        # Тут код
        arr = self.data
        size = len(arr)

        # Создаем холст
        img = Image.new("RGBA", (size * 100, size * 100), "beige")  # холст
        idraw = ImageDraw.Draw(img)

        # Созданем линии холста
        idraw.rectangle((0, 0, size, size * 100), fill="gray")
        idraw.rectangle((size * 100 - (size), 0, size * 100, size * 100), fill="gray")
        idraw.rectangle((0, 0, size * 100, size), fill="gray")
        idraw.rectangle((0, size * 100 - (size), size * 100, size * 100), fill="gray")

        i = 1

        # Рисуем поле
        while i <= size:
            idraw.line((i * 100, 0, i * 100, size * 100), fill=("gray"), width=10)
            i = i + 1

        i = 1
        while i <= size:
            idraw.line((0, i * 100, size * 100, i * 100), fill=("gray"), width=10)
            i = i + 1

        # Рисуем квадраты для чисел
        font = ImageFont.truetype("arial.ttf", size=40)
        fontlittle = ImageFont.truetype("arial.ttf", size=35)
        # font = ImageFont.load_default()
        # fontlittle = ImageFont.load_default()
        """
        ⠀⠀⠀⠀⡀⠄⠠⠀⠠⠀⢀⠪No switches?⡐⡅⡇⢇⠕⡌⡢⢑⠌⡢⢑⠌⡆⢕⢌⢢⠱⡨⢢⢑⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⠢⡑⢌⢂⠪⡐⢌⢂⠪⡐⢅⢪⠨⡢⡃⡪.
        ⠀⠐⠈⠀⠀⡀⠐⢈⠠⠐⡀⢇⢕⠕⢅⠣⡑⠔⢌⠢⠡⡊⢔⢑⠌⡆⢕⢔⠱⡨⢢⠱⡨⢪⢘⢌⢪⠸⡨⡪⡘⡌⡪⡘⢔⢑⢌⠢⡡⡑⢌⠢⡡⡑⢌⢢⢑⠕⡌⢆⠕⡅⢕⠌⡆⢕⠅⡂⡂..
        ⠀⡁⠀⠄⠁⠀⡈⠠⠀⡂⢜⢌⠢⡑⢅⠕⢌⠪⡐⠅⢕⠐⢅⠢⠱⡘⡔⢅⠣⡊⢆⠣⡪⢢⠱⡨⡂⢇⠕⢜⢸⢘⢜⢜⢜⢌⢆⢣⠪⡨⢢⠱⡐⡅⡕⢌⢆⢣⢱⠡⡃⢎⠢⡃⡎⡪⢂⠂⡂..
        ⠀⢂⠐⠀⡀⠁⠄⠂⡁⢌⢆⠢⡑⡌⡢⡑⢔⠡⠊⠌⡐⢈⠢⡑⠅⢕⠸⡨⡊⡪⠪⡘⢌⢢⠱⡨⡨⡂⡣⡑⡅⡣⡱⢱⠸⡘⡜⡔⡕⢜⢰⢡⢱⠨⡊⡆⡣⡱⡡⢣⢑⢅⢣⢱⢸⢘⠠⠨⢐..
        ⠐⠠⠈⠄⡀⠡⠀⠡⠀⢂⠂⡑⠨⠐⠀⠂⠠⠀⠂⠠⢀⠢⠡⡊⢜⠠⠈⠢⡑⠜⡌⡪⡨⠢⡑⢔⢌⢢⠱⡨⢢⠱⡘⡌⢎⢎⢪⢸⢨⠪⡢⡣⡱⡱⡱⡸⡨⡢⢣⢑⠕⡌⢆⢣⠕⠠⠨⢐⠐..
        ⠀⠡⠈⠄⠂⡐⠈⠀⠅⠀⠠⠀⠐⠈⠀⢁⠠⠐⡈⠔⡡⢊⢌⠢⡑⢌⠢⡀⠨⠈⠢⡊⢌⠪⡨⠢⡑⢔⢑⠌⢆⠣⡑⡌⢆⠕⢅⢣⠱⡱⡱⡸⡸⡰⡱⡸⡨⡊⢆⢕⢑⠜⡜⠌⢄⠑⡈⠄⠌..
        ⠈⠄⢁⠂⡁⠄⠂⡈⢀⠂⠀⠄⢂⠨⡐⢔⠨⡂⡪⠨⡂⢕⢐⢅⠪⡐⢅⠪⡐⡈⡀⠐⠀⠅⠂⠡⠈⠐⠀⠅⢁⠑⠨⠨⠢⡑⢅⢕⠱⡱⡸⡸⡸⡸⡨⡢⠣⡊⢆⠪⡂⡇⡃⠅⡂⠌⠄⢁⢀..
        ⠀⠌⠠⠐⠀⢂⠁⠄⠂⠠⠁⠄⠂⡑⢌⠢⡑⡐⢌⢌⠢⡑⢔⢐⢅⠪⡐⢅⠪⡐⢌⠢⡐⡀⠂⠐⠈⠀⠁⠀⠄⠐⠈⠀⢂⠨⠐⠔⢅⠇⡇⡇⡇⡇⢇⢪⢑⠌⢆⢣⠣⢁⢐⠐⠐⠀⡐⠠⠂..
        ⠀⠌⠐⢈⠈⠠⠐⢀⠁⠂⡁⠐⢀⠈⠂⢕⢐⢌⠢⠢⡑⢌⠢⡑⡐⡑⢌⠢⠨⡂⢅⠕⡐⢌⠪⠨⡐⡐⢄⢂⠀⠐⠀⢁⠠⠀⠡⠡⡑⢕⢕⢕⢕⢕⢕⢑⠔⡑⡅⢃⠐⡀⠂⢀⢐⠐⠄⠅⠡..
        ⠀⠌⠐⡀⠌⠠⠈⠠⢀⠁⠄⠈⡀⠄⠁⠄⠂⠢⠡⠁⠂⠂⠅⡂⠪⡨⠢⡡⡑⠌⡂⠕⡨⢂⠅⡣⠨⡂⢅⠢⡡⡑⡐⡠⢀⠄⢁⠨⢈⢎⢪⢪⢪⠢⡑⡐⡑⠨⠀⠂⠐⢀⠐⡀⠂⠌⠄⠅⡁..
        ⠀⠂⢁⠠⠐⢀⠡⠐⠀⠄⠂⠁⡀⠄⠂⠀⠂⢀⢰⢸⠐⡀⠀⠈⠐⢌⠪⡐⡐⠅⡊⠔⡨⢐⠨⢐⠡⡈⠢⢑⢐⠔⡡⢊⠔⡨⠠⡐⠠⡱⡱⡱⡡⡑⠌⠀⡀⠐⠀⢀⠂⡐⢀⠂⠡⠈⠄⠡⠐...
        ⠀⡁⠄⠐⠀⠂⡀⠂⢁⠀⠂⠁⢀⠠⠀⠁⠐⢀⡏⡎⠆⠀⠠⡢⠈⠰⡑⡐⠌⠌⠔⡁⠂⠂⠈⠀⠀⠀⠑⠐⠄⡑⠌⡂⢕⠨⠨⡐⠡⡪⡪⡪⠢⡑⠠⡂⡪⠂⢈⠀⠄⠐⠠⠈⠄⠡⢁⠡⠈ ..
        ⠀⠠⠐⠈⡀⢁⠠⠐⠀⠀⠂⠁⠀⢀⠠⠈⢀⠔⠹⡌⡐⠄⠠⠈⠀⡸⢐⠌⢌⠪⢐⢀⢪⢸⡨⠈⡐⠀⠄⢀⠀⠈⠌⡐⡡⠊⠌⢌⠜⡜⡜⡈⡐⠄⠅⠂⠄⠁⠀⠄⢈⠠⠁⠨⠀⠅⡀⢂⠁⡁.
        ⠀⠂⠐⠀⠄⠀⠄⠠⠈⠀⠐⠀⠁⠀⠀⠀⢢⢑⢐⠨⢐⠀⠅⢂⠰⡘⢄⠕⡠⢑⠠⢐⢕⢕⠄⠁⠀⡌⠆⠀⡐⠠⠀⢂⠢⡡⢡⢡⢱⠱⢐⠐⠨⠈⠄⠁⠀⠀⢁⠠⠀⠄⠈⠄⠈⠄⠐⡀⠂⠄..
        ⠀⢈⠀⠂⠐⠀⠐⢀⠠⠈⠀⠁⠀⠀⠀⠀⢱⠨⡂⠌⠄⢌⢐⢔⠱⡡⢑⢐⠌⠔⡈⠐⡕⡕⡀⢂⢀⢀⠀⠄⡸⡨⢀⢪⢸⢸⢸⢸⡸⠨⡐⠨⠈⠀⠀⠀⠀⠀⠀⠀⠠⠀⡁⠄⠁⠄⠁⠄⠂  ..
        ⠀⠀⠄⠂⢀⠡⠨⠀⠄⢀⠀⠀⠀⡀⠀⠄⡐⠕⢌⢊⠪⡪⡘⡌⡪⢐⢁⠢⡈⡂⡂⠡⢀⠑⡑⠢⠐⡀⠅⢂⠅⢔⢸⢸⢸⢪⢎⢇⠇⠁⠀⢀⠀⠂⠁⠀⢀⠀⠀⠀⠀⠀⠀⠐⠀⠂⢁⠐⠈⡀..
        ⠀⠠⠐⠀⠀⠀⠀⠈⠈⠄⡈⢀⠡⠐⡈⠠⠀⡣⢑⠌⡜⢔⠅⢕⢐⢁⢂⠅⡢⠢⡈⡂⡂⡁⡂⠌⡐⡐⠨⢐⢌⢪⢪⢪⢪⢣⢳⠑⠁⢀⠈⠀⠀⡀⠠⠀⠀⡀⠀⠂⠀⠀⠀⠀⠀⠁⠠⠐⠀⠠..
        ⠀⠀⠀⠀⠀⠀⠀⡀⠄⠀⠀⠐⠀⠂⠀⠁⠐⠨⡢⢱⢸⠨⡊⢔⢐⠔⡠⢑⠄⢕⠐⢔⠰⡐⡐⢅⠢⡨⠨⡂⢎⠢⠣⡱⠱⡑⡁⠄⠠⢀⠠⠈⠀⢀⠀⠠⠀⠀⡀⠄⠀⠈⠀⢀⠀⠀⠀⠈⠀⠂...
        ⠀⠀⠀⠁⠀⠁⠀⠀⢀⠀⠄⠂⠈⠄⡈⠄⢂⢕⢜⢌⢆⢃⠪⡢⡑⡌⡢⡑⢌⢂⢅⢑⠌⡂⠪⠠⡑⠨⡈⠢⡁⡪⠨⢌⠪⡂⠐⠀⡌⠠⠠⢀⠈⠀⡀⠄⠀⠅⠀⠀⢀⠈⠀⠀⠀⢀⠀⠀⠀⠀...
        ⠀⠀⠀⠄⠀⠄⠂⠈⠀⠀⢀⠀⠐⡀⢂⠐⡌⡆⡣⡊⡢⡱⡱⡱⡸⡸⡨⡊⢆⢒⢔⢐⠡⠨⡨⢂⠊⢔⠨⢂⠪⡐⢍⢜⠌⢢⠅⠢⠐⡈⡐⡀⢂⠁⡀⠄⠁⡉⠀⠈⠀⠀⠀⠂⠈⠀⠀⠀⠠⠀..
        ⠀⠀⠀⡀⠀⡀⠀⠠⠐⠈⠀⠀⡀⠂⢐⢰⠱⡸⡨⡪⡪⡪⣎⢞⡜⡎⡎⡎⡎⡪⡂⠢⠡⢑⢐⠐⢅⢂⠪⡐⡑⡜⡸⠀⠀⠂⠅⠡⢁⠂⠄⢂⠐⠠⢀⠀⢂⠁⡀⠁⢀⠈⠀⢀⠠⠀⠀⠐⠀⠀..
        ⠀⠀⠀⡀⠀⡀⠀⠂⠀⠄⠂⠁⠀⢨⢐⢕⢕⢕⢕⡕⣕⢧⢳⢳⢹⢸⢸⠸⡨⢂⠊⠌⢌⢐⠐⢅⠢⠢⡑⢌⢪⠸⠀⠀⠀⠂⠁⠀⠂⡈⠈⠄⠨⠐⠀⠌⡀⠂⠄⢂⠀⡀⠄⠀⠀⠀⠐⠀⠀⠠...
        ⠀⠀⢀⠀⢀⠀⠄⠂⠁⠀⠄⠂⠁⠜⢌⢎⢎⢎⢇⡏⡮⡎⡗⡝⢜⢌⢢⢑⢌⢢⠡⡑⡐⠄⠅⢕⠨⡘⡌⡎⡎⠅⠀⠀⠀⠀⠀⠀⠀⠀⠁⡈⠠⠈⠀⠂⡀⠡⠈⠄⢐⠀⠄⠐⠈⠀⠀⠠⠀⠀...
        ⠀⠀⠀⠀⡀⠀⡀⠄⠂⠁⡀⠐⠀⠈⡢⢂⠕⡱⡑⢕⠕⢕⠱⡘⡜⡜⡜⣜⢼⢸⢸⠰⡨⠨⠨⡂⢕⢅⢇⢎⠀⠀⠀⢀⠀⠁⠀⠀⠈⠀⠀⠀⠀⠀⠈⠀⡀⠀⠂⠁⠄⠐⢈⠠⠀⠁⠂⠀⠀⠐....
        ⠀⠀⠀⠁⠀⢀⠀⠠⠐⠀⡀⠂⠀⠁⠀⠂⠌⢐⠌⡂⡑⡀⡃⠕⡑⠕⡍⡪⠪⠪⡣⡓⡌⡊⠔⢌⢆⢣⠱⠁⠀⠀⠄⠀⠀⠀⠄⠀⢀⠀⠀⡀⠠⠀⠀⠀⠀⠂⠈⠀⢀⠁⠀⠄⠂⢀⠈⠀⠁⡀....
        ⠀⠀⠐⠀⠁⠀⠠⠐⠀⠄⠀⠂⠀⠁⡀⠂⠠⢐⠡⢂⠀⠂⠄⠅⡊⠜⠌⢎⢎⢖⢌⠪⠪⡐⢡⢑⠜⠌⠂⠀⠂⠁⠀⢀⠐⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠐⠀⠀⠀⠂⠀⠂⠀⠀⠀⠀⠀⠀....
        ⠀⠀⠀⠀⠐⠈⡀⠀⠂⠀⠁⠀⠂⢀⠀⡀⠂⡐⠅⢂⠀⠂⠠⢁⠂⢅⢑⢐⠔⡐⢅⠣⡑⠨⡐⢅⠅⠡⠁⠌⠀⠂⠈⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⢀⠀⠀⡀⠄⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀.....
        """
        for i in range(size):
            for j in range(size):
                number = arr[i][j]
                if arr[i][j] == 2:
                    idraw.rectangle(
                        (20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80),
                        fill="#FAEBA7",
                    )
                    idraw.text(
                        (40 + (j * 100), (27 + i * 100)), "2", font=font, fill="grey"
                    )
                elif arr[i][j] == 4:
                    idraw.rectangle(
                        (20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80),
                        fill="#FFE4C4",
                    )
                    idraw.text(
                        (40 + (j * 100), (27 + i * 100)), "4", font=font, fill="grey"
                    )
                elif arr[i][j] == 8:
                    idraw.rectangle(
                        (20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80),
                        fill="orange",
                    )
                    idraw.text(
                        (40 + (j * 100), (27 + i * 100)),
                        str(number),
                        font=font,
                        fill="white",
                    )
                elif arr[i][j] == 16:
                    idraw.rectangle(
                        (20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80),
                        fill="orange",
                    )
                    idraw.text(
                        (27 + (j * 100), (27 + i * 100)),
                        str(number),
                        font=font,
                        fill="white",
                    )
                elif arr[i][j] == 32:
                    idraw.rectangle(
                        (20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80),
                        fill="orange",
                    )
                    idraw.text(
                        (27 + (j * 100), (27 + i * 100)),
                        str(number),
                        font=font,
                        fill="white",
                    )
                elif arr[i][j] == 64:
                    idraw.rectangle(
                        (20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80),
                        fill="RED",
                    )
                    idraw.text(
                        (27 + (j * 100), (27 + i * 100)),
                        str(number),
                        font=font,
                        fill="white",
                    )
                elif arr[i][j] == 128:
                    idraw.rectangle(
                        (20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80),
                        fill="YELLOW",
                    )
                    idraw.text(
                        (20 + (j * 100), (30 + i * 100)),
                        str(number),
                        font=fontlittle,
                        fill="white",
                    )
                elif arr[i][j] == 256:
                    idraw.rectangle(
                        (20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80),
                        fill="YELLOW",
                    )
                    idraw.text(
                        (22 + (j * 100), (30 + i * 100)),
                        str(number),
                        font=fontlittle,
                        fill="white",
                    )
                elif arr[i][j] == 512:
                    idraw.rectangle(
                        (20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80),
                        fill="YELLOW",
                    )
                    idraw.text(
                        (22 + (j * 100), (30 + i * 100)),
                        str(number),
                        font=fontlittle,
                        fill="white",
                    )
                elif arr[i][j] == 1024:
                    idraw.rectangle(
                        (20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80),
                        fill="YELLOW",
                    )
                    idraw.text(
                        (23 + (j * 100), (35 + i * 100)),
                        str(number),
                        font=ImageFont.truetype("arial.ttf", size=25),
                        fill="white",
                    )
                elif arr[i][j] == 2048:
                    idraw.rectangle(
                        (20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80),
                        fill="YELLOW",
                    )
                    idraw.text(
                        (23 + (j * 100), (35 + i * 100)),
                        str(number),
                        font=ImageFont.truetype("arial.ttf", size=25),
                        fill="white",
                    )
        filename = os.path.join(
            f"{self.temp_path}",
            f"{''.join(random.choice(string.ascii_lowercase) for _ in range(20))}.png",
        )
        img.save(filename)
        self.temp_files.append(filename)
        return nextcord.File(filename)

    def generate_points(self):
        """
        Используется внутри класса
        Генерация рандомных точек в матрице
        Нет входных значений, кроме самого объекта (self)
        Возвращает фолс если генерация невозможна, тру если всё ок, меняет self.data)
        """
        # Тут код
        countZeros = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.data[i][j] == 0:
                    countZeros += 1
        ZeroNumber = randint(1, countZeros)
        number = 0
        if randint(1, 8) == 8:
            newNumeric = 4
        else:
            newNumeric = 2
        for i in range(self.size):
            for j in range(self.size):
                if self.data[i][j] == 0:
                    number += 1
                    if number == ZeroNumber:
                        self.data[i][j] = newNumeric
                        break
            if number == ZeroNumber:
                break
        if countZeros > 1:
            return True
        result = False
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                if (
                    self.data[i][j] == self.data[i][j - 1]
                    or self.data[i][j] == self.data[i - 1][j]
                    or self.data[i][j] == self.data[i][j + 1]
                    or self.data[i][j] == self.data[i + 1][j]
                ):
                    result = True
                    break
            if result:
                break
        if not result:
            for i in range(1, self.size - 1):
                if (
                    self.data[0][i] == self.data[0][i - 1]
                    or self.data[0][i] == self.data[0][i + 1]
                    or self.data[self.size - 1][i] == self.data[self.size - 1][i - 1]
                    or self.data[self.size - 1][i] == self.data[self.size - 1][i + 1]
                ):
                    result = True
                    break
                if (
                    self.data[i][0] == self.data[i - 1][0]
                    or self.data[i][0] == self.data[i + 1][0]
                    or self.data[i][self.size - 1] == self.data[i - 1][self.size - 1]
                    or self.data[i][self.size - 1] == self.data[i + 1][self.size - 1]
                ):
                    result = True
                    break
        return result

    @nextcord.ui.button(
        style=nextcord.ButtonStyle.secondary, label="\u200b", row=1, disabled=True
    )
    async def puff_left_button(self, button: nextcord.ui.Button):
        """
        Вспомогательная кнопка для движения влево.

        :param button: Кнопка.
        :type button: nextcord.ui.Button
        """
        button.disabled = True
        pass

    @nextcord.ui.button(label="⬆", style=nextcord.ButtonStyle.green, row=1)
    async def move_up_button(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        """
        Кнопка для движения вверх.

        :param button: кнопка.
        :type button: nextcord.ui.Button
        :param interaction: объект взаимодействия с дискордом.
        :type interaction: nextcord.Interaction
        """
        done = False
        i = 0
        while i < self.size:
            j = 1
            afterUnion = False
            while j < self.size:
                if j != 0 and self.data[j][i] != 0:
                    if self.data[j - 1][i] == 0:
                        done = True
                        self.data[j - 1][i] = self.data[j][i]
                        self.data[j][i] = 0
                        j -= 2
                    elif self.data[j - 1][i] == self.data[j][i] and not afterUnion:
                        done = True
                        self.data[j - 1][i] *= 2
                        self.data[j][i] = 0
                        afterUnion = True
                    else:
                        afterUnion = False
                j += 1
            i += 1
        if not done or self.generate_points():
            await interaction.message.edit(file=self.drow_matrix())
        else:
            for child in self.buttons:
                child.disabled = True
            await interaction.message.edit(file=self.drow_matrix(), view=self)
            await interaction.response.send_message("игра окончена")

    @nextcord.ui.button(
        style=nextcord.ButtonStyle.secondary, label="\u200b" * 8, row=1, disabled=True
    )
    async def puff_right_button(self, button: nextcord.ui.Button):
        """
        Вспомогательная кнопка для движения вправо.

        :param button: кнопка.
        :type button: nextcord.ui.Button
        """
        button.disabled = True
        pass

    @nextcord.ui.button(label="⬅", style=nextcord.ButtonStyle.green, row=2)
    async def move_left_button(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        """
        Кнопка для движения влево.

        :param button: кнопка.
        :type button: nextcord.ui.Button
        :param interaction: объект взаимодействия с дискордом.
        :type interaction: nextcord.Interaction
        """
        done = False
        i = 0
        while i < self.size:
            j = 1
            afterUnion = False
            while j < self.size:
                if j != 0 and self.data[i][j] != 0:
                    if self.data[i][j - 1] == 0:
                        done = True
                        self.data[i][j - 1] = self.data[i][j]
                        self.data[i][j] = 0
                        j -= 2
                    elif self.data[i][j - 1] == self.data[i][j] and not afterUnion:
                        done = True
                        self.data[i][j - 1] *= 2
                        self.data[i][j] = 0
                        afterUnion = True
                    else:
                        afterUnion = False
                j += 1
            i += 1
        if not done or self.generate_points():
            await interaction.message.edit(file=self.drow_matrix())
        else:
            for child in self.buttons:
                child.disabled = True
            await interaction.message.edit(file=self.drow_matrix(), view=self)
            await interaction.response.send_message("игра окончена")

    @nextcord.ui.button(label="⬇", style=nextcord.ButtonStyle.green, row=2)
    async def move_down_button(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        """
        Кнопка для движения вниз.

        :param button: кнопка.
        :type button: nextcord.ui.Button
        :param interaction: объект взаимодействия с дискордом.
        :type interaction: nextcord.Interaction
        """
        done = False
        i = 0
        while i < self.size:
            j = self.size - 2
            afterUnion = False
            while j > -1:
                if j != self.size - 1 and self.data[j][i] != 0:
                    if self.data[j + 1][i] == 0:
                        done = True
                        self.data[j + 1][i] = self.data[j][i]
                        self.data[j][i] = 0
                        j += 2
                    elif self.data[j + 1][i] == self.data[j][i] and not afterUnion:
                        done = True
                        self.data[j + 1][i] *= 2
                        self.data[j][i] = 0
                        afterUnion = True
                    else:
                        afterUnion = False
                j -= 1
            i += 1
        if not done or self.generate_points():
            await interaction.message.edit(file=self.drow_matrix())
        else:
            for child in self.buttons:
                child.disabled = True
            await interaction.message.edit(file=self.drow_matrix(), view=self)
            await interaction.response.send_message("игра окончена")

    @nextcord.ui.button(label="➡", style=nextcord.ButtonStyle.green, row=2)
    async def move_right_button(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        """
        Кнопка для движения вправо.

        :param button: кнопка.
        :type button: nextcord.ui.Button
        :param interaction: объект взаимодействия с дискордом.
        :type interaction: nextcord.Interaction
        """
        done = False
        i = 0
        while i < self.size:
            j = self.size - 2
            afterUnion = False
            while j > -1:
                if j != self.size - 1 and self.data[i][j] != 0:
                    if self.data[i][j + 1] == 0:
                        done = True
                        self.data[i][j + 1] = self.data[i][j]
                        self.data[i][j] = 0
                        j += 2
                    elif self.data[i][j + 1] == self.data[i][j] and not afterUnion:
                        done = True
                        self.data[i][j + 1] *= 2
                        self.data[i][j] = 0
                        afterUnion = True
                    else:
                        afterUnion = False
                j -= 1
            i += 1
        if not done or self.generate_points():
            await interaction.message.edit(file=self.drow_matrix())
        else:
            for child in self.buttons:
                child.disabled = True
            await interaction.message.edit(file=self.drow_matrix(), view=self)
            await interaction.response.send_message("игра окончена")
