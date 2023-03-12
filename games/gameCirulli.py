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
    raise "Данный класс ни где не используется!"
    
    def __init__(self, game):
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
        number = randint(1, 100)
        position1 = randint(1, size ** 2)
        position2 = randint(1, size ** 2)
        while position1 == position2:
            position2 = randint(1, size ** 2)
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
        Деконструктор
        Можно использоавть для сохранения результатов и тд и тп..
        Пока не трогаем.
        """
        ...

    def drow_matrix(self):
        """
        Используется внутри класса
        Рисует картинку по двумерному массиву
        Нет входных значений, кроме самого объекта (self)
        Возвращает объект картинки.
        """
        # Тут код
        arr = self.data
        size = len(arr)

        # Создаем холст
        img = Image.new('RGBA', (size * 100, size * 100), 'beige')  # холст
        idraw = ImageDraw.Draw(img)

        # Созданем линии холста
        idraw.rectangle((0, 0, size, size * 100), fill='gray')
        idraw.rectangle((size * 100 - (size), 0, size * 100, size * 100), fill='gray')
        idraw.rectangle((0, 0, size * 100, size), fill='gray')
        idraw.rectangle((0, size * 100 - (size), size * 100, size * 100),
                        fill='gray')

        i = 1
        # Рисуем поле
        while i <= size:
            idraw.line((i * 100, 0, i * 100, size * 100), fill=('gray'), width=10)
            i = i + 1

        i = 1
        while i <= size:
            idraw.line((0, i * 100, size * 100, i * 100), fill=('gray'), width=10)
            i = i + 1

        # Рисуем квадраты для чисел
        #font = ImageFont.truetype("arial.ttf", size=40)
        #fontlittle = ImageFont.truetype("arial.ttf", size=35)
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
        font = ImageFont.load_default()
        fontlittle = ImageFont.load_default()
        for i in range(size):
            for j in range(size):
                number = arr[i][j]
                if arr[i][j] == 2:
                    idraw.rectangle((20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80), fill= "#FAEBA7")
                    idraw.text((40 + (j * 100), (27 + i * 100)), "2", font=font, fill='grey')
                elif arr[i][j] == 4:
                    idraw.rectangle((20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80), fill='#FFE4C4')
                    idraw.text((40 + (j * 100), (27 + i * 100)), "4", font=font, fill='grey')
                elif arr[i][j] == 8:
                    idraw.rectangle((20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80), fill='orange')
                    idraw.text((40 + (j * 100), (27 + i * 100)), str(number), font=font, fill='white')
                elif arr[i][j] == 16:
                    idraw.rectangle((20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80), fill='orange')
                    idraw.text((27 + (j * 100), (27 + i * 100)), str(number), font=font, fill='white')
                elif arr[i][j] == 32:
                    idraw.rectangle((20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80), fill='orange')
                    idraw.text((27 + (j * 100), (27 + i * 100)), str(number), font=font, fill='white')
                elif arr[i][j] == 64:
                    idraw.rectangle((20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80), fill='RED')
                    idraw.text((27 + (j * 100), (27 + i * 100)), str(number), font=font, fill='white')
                elif arr[i][j] == 128:
                    idraw.rectangle((20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80), fill='YELLOW')
                    idraw.text((20 + (j * 100), (30 + i * 100)), str(number), font=fontlittle, fill='white')
                elif arr[i][j] == 256:
                    idraw.rectangle((20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80), fill='YELLOW')
                    idraw.text((22 + (j * 100), (30 + i * 100)), str(number), font=fontlittle, fill='white')
                elif arr[i][j] == 512:
                    idraw.rectangle((20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80), fill='YELLOW')
                    idraw.text((22 + (j * 100), (30 + i * 100)), str(number), font=fontlittle, fill='white')
                elif arr[i][j] == 1024:
                    idraw.rectangle((20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80), fill='YELLOW')
                    idraw.text((23 + (j * 100), (35 + i * 100)), str(number), font=ImageFont.truetype("arial.ttf", size=25), fill='white')
                elif arr[i][j] == 2048:
                    idraw.rectangle((20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80), fill='YELLOW')
                    idraw.text((23 + (j * 100), (35 + i * 100)), str(number), font=ImageFont.truetype("arial.ttf", size=25), fill='white')
                else:
                    idraw.rectangle((20 + j * 100, 20 + i * 100, j * 100 + 80, i * 100 + 80), fill='YELLOW')
                    idraw.text((23 + (j * 100), (35 + i * 100)), str(number), font=ImageFont.truetype("arial.ttf", size=25), fill='white')
        return img

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
        for i in range(1, self.size-1):
            for j in range(1, self.size-1):
                if self.data[i][j] == self.data[i][j-1] or \
                        self.data[i][j] == self.data[i-1][j] or \
                        self.data[i][j] == self.data[i][j+1] or \
                        self.data[i][j] == self.data[i+1][j]:
                    result = True
                    break
            if result:
                break
        if not result:
            for i in range(1, self.size-1):
                if self.data[0][i] == self.data[0][i-1] or \
                        self.data[0][i] == self.data[0][i+1] or \
                        self.data[self.size-1][i] == self.data[self.size-1][i-1] or \
                        self.data[self.size-1][i] == self.data[self.size-1][i+1]:
                    result = True
                    break
                if self.data[i][0] == self.data[i-1][0] or \
                        self.data[i][0] == self.data[i+1][0] or \
                        self.data[i][self.size-1] == self.data[i-1][self.siz
                        self.data[i][self.size-1] == self.data[i+1][self.size-1]:e-1] or \
                    result = True
                    break
        return result

    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, label="\u200b", row=1, disabled=True)
    async def puff_left_button(self, button: nextcord.ui.Button):
        button.disabled = True
        pass

    @nextcord.ui.button(label="⬆", style=nextcord.ButtonStyle.green, row=1)
    async def move_up_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        """
        Используется вне класса
        Движеное вверх
        Нет входных значений, кроме самого объекта (self)
        Возвращает результат выполнения drow_matrix
        """
        done = False
        i = 0
        while i < self.size:
            j = 1
            afterUnion = False
            while j < self.size:
                if j != 0 and self.data[j][i] != 0:
                    if self.data[j-1][i] == 0:
                        done = True
                        self.data[j-1][i] = self.data[j][i]
                        self.data[j][i] = 0
                        j -= 2
                    elif self.data[j-1][i] == self.data[j][i] and not afterUnion:
                        done = True
                        self.data[j-1][i] *= 2
                        self.data[j][i] = 0
                        afterUnion = True
                    else:
                        afterUnion = False
                j += 1
            i += 1
        """
        Тут должна быть логика отправки сообщений о следующем шаге и завершении игры.
        """
        if not done or self.generate_points():
            return self.drow_matrix()
        else:
            return False
         
    @nextcord.ui.button(style=nextcord.ButtonStyle.secondary, label="\u200b", row=1, disabled=True)
    async def puff_right_button(self, button: nextcord.ui.Button):
        pass

    @nextcord.ui.button(label="⬅", style=nextcord.ButtonStyle.green, row=2)
    async def move_left_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        """
        Используется вне класса
        Движение влево
        Нет входных значений, кроме самого объекта (self)
        Возвращает результат выполнения drow_matrix
        """
        done = False
        i = 0
        while i < self.size:
            j = 1
            afterUnion = False
            while j < self.size:
                if j != 0 and self.data[i][j] != 0:
                    if self.data[i][j-1] == 0:
                        done = True
                        self.data[i][j-1] = self.data[i][j]
                        self.data[i][j] = 0
                        j -= 2
                    elif self.data[i][j-1] == self.data[i][j] and not afterUnion:
                        done = True
                        self.data[i][j-1] *= 2
                        self.data[i][j] = 0
                        afterUnion = True
                    else:
                        afterUnion = False
                j += 1
            i += 1
        """
        Тут должна быть логика отправки сообщений о следующем шаге и завершении игры.
        """
        if not done or self.generate_points():
            return self.drow_matrix()
        else:
            return False

    @nextcord.ui.button(label="⬇", style=nextcord.ButtonStyle.green, row = 2)
    async def move_down_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        """
        Используется вне класса
        Движение вниз
        Нет входных значений, кроме самого объекта (self)
        Возвращает результат выполнения drow_matrix
        """
        done = False
        i = 0
        while i < self.size:
            j = self.size - 2
            afterUnion = False
            while j > -1:
                if j != self.size - 1 and self.data[j][i] != 0:
                    if self.data[j+1][i] == 0:
                        done = True
                        self.data[j+1][i] = self.data[j][i]
                        self.data[j][i] = 0
                        j += 2
                    elif self.data[j+1][i] == self.data[j][i] and not afterUnion:
                        done = True
                        self.data[j+1][i] *= 2
                        self.data[j][i] = 0
                        afterUnion = True
                    else:
                        afterUnion = False
                j -= 1
            i += 1
        """
        Тут должна быть логика отправки сообщений о следующем шаге и завершении игры.
        """
        if not done or self.generate_points():
            return self.drow_matrix()
        else:
            return False

    @nextcord.ui.button(label="➡", style=nextcord.ButtonStyle.green, row=2)
    async def move_right_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        """
        Используется вне класса
        Движеное вправо
        Нет входных значений, кроме самого объекта (self)
        Возвращает результат выполнения drow_matrix
        """
        done = False
        i = 0
        while i < self.size:
            j = self.size-2
            afterUnion = False
            while j > -1:
                if j != self.size - 1  and self.data[i][j] != 0:
                    if self.data[i][j+1] == 0:
                        done = True
                        self.data[i][j+1] = self.data[i][j]
                        self.data[i][j] = 0
                        j += 2
                    elif self.data[i][j+1] == self.data[i][j] and not afterUnion:
                        done = True
                        self.data[i][j+1] *= 2
                        self.data[i][j] = 0
                        afterUnion = True
                    else:
                        afterUnion = False
                j -= 1
            i += 1
        """
        Тут должна быть логика отправки сообщений о следующем шаге и завершении игры.
        """
        if not done or self.generate_points():
            return self.drow_matrix()
        else:
            return False
