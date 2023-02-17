from enum import Enum


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

game = GameCirulli(4)
print(game.data)