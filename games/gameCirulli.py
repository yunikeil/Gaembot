
from PIL import Image, ImageDraw, ImageFont

class GameCirulli:
    def __init__(self, size: int):
        """
        Конструктор
        На вход, при создании объекта передаётся размер квадрата
        Также тут объявляются все глобальные для класса поля,
         которые будут использоваться в последующих методах.
        """
        # Переменная data отвечает за хранение информации.
        self.data: list[list[int]] = [
            [0 for x in range(size)] for y in range(size)
        ]
        ...

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
        arr = GameCirulli.data
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
        font = ImageFont.truetype("arial.ttf", size=40)
        fontlittle = ImageFont.truetype("arial.ttf", size=35)
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

        img.save('rectangle.png')
        img.show()

        return print("image")

    def generate_points(self):
        """
        Используется внутри класса
        Генерация рандомных точек в матрице
        Нет входных значений, кроме самого объекта (self)
        Возвращает фолс если генерация невозможна, тру если всё ок, меняет self.data)
        """
        # Тут код
        
        return 
        ...

    def move_right(self):
        """
        Используется вне класса
        Движеное вправо
        Нет входных значений, кроме самого объекта (self)
        Возвращает результат выполнения drow_matrix
        """

        if self.generate_points():
            return self.drow_matrix()
        else: return False

    def move_left(self):
        """
        Используется вне класса
        Движение влево
        Нет входных значений, кроме самого объекта (self)
        Возвращает результат выполнения drow_matrix
        """

        if self.generate_points():
            return self.drow_matrix()
        else: return False

    def move_up(self):
        """
        Используется вне класса
        Движеное вверх
        Нет входных значений, кроме самого объекта (self)
        Возвращает результат выполнения drow_matrix
        """

        if self.generate_points():
            return self.drow_matrix()
        else: return False

    def move_down(self):
        """
        Используется вне класса
        Движение вниз
        Нет входных значений, кроме самого объекта (self)
        Возвращает результат выполнения drow_matrix
        """

        if self.generate_points():
            return self.drow_matrix()
        else: return False
    ...
