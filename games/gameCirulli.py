from random import randint


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
        size = 4

        # Создаем холст
        img = Image.new('RGBA', (size * 100, size * 100), 'beige')  # холст
        idraw = ImageDraw.Draw(img)

        # Созданем линии холста
        idraw.rectangle((0, 0, size, size * 100), fill='gray')  # левая граница
        idraw.rectangle((size*100-size, 0, size*100, size*100), fill='gray')  # Правая граница
        idraw.rectangle((0, 0, size*100, size), fill='gray')  # отступ слева, отступ сверху, размер, размер
        idraw.rectangle((0, size*100-size, size*100, size*100), fill='gray')  # отступ слева, отступ сверху, размер, размер

        img.save('GamePicture.png')
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
                if self.data[i][j] == self.data[i][j-1] or self.data[i][j] == self.data[i-1][j] or self.data[i][j] == self.data[i][j+1] or self.data[i][j] == self.data[i+1][j]:
                    result = True
                    break
            if result:
                break
        if not result:
            for i in range(1, self.size-1):
                if self.data[0][i] == self.data[0][i-1] or self.data[0][i] == self.data[0][i+1] or self.data[self.size-1][i] == self.data[self.size-1][i-1] or self.data[self.size-1][i] == self.data[self.size-1][i+1]:
                    result = True
                    break
                if self.data[i][0] == self.data[i-1][0] or self.data[i][0] == self.data[i+1][0] or self.data[i][self.size-1] == self.data[i-1][self.size-1] or self.data[i][self.size-1] == self.data[i+1][self.size-1]:
                    result = True
                    break
        return result
        ...

    def move_right(self):
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
        if not done or self.generate_points():
            return self.drow_matrix()
        else:
            return False

    def move_left(self):
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
        if not done or self.generate_points():
            return self.drow_matrix()
        else:
            return False

    def move_up(self):
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
        if not done or self.generate_points():
            return self.drow_matrix()
        else:
            return False

    def move_down(self):
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
        if not done or self.generate_points():
            return self.drow_matrix()
        else:
            return False
    ...
