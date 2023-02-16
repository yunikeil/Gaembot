

class GameCirulli:
    def __init__(self, size: int):
        """
        На вход, при создании объекта передаётся размер квадрата
        Также тут объявляются все переменные которые будут использоваться
         в последующих методах.
        """
        self.data: list[list[int]] = [
            [0 for x in range(size)] for y in range(size)
        ]
        print(self.data)
        ...

    def __del__(self):
        ...

    def drow_matrix(self, ):
        """
        Рисует картинку по двумерному массиву
        """

        return image

    def generate_points(self, ):
        """
        Генерация рандомных точек в матрице
        """

        ...

    # Наверное, можно сделать движения одним методом,
    #  в который в качестве аргумента будет приходить одно из значений перечисления
    def move_right(self, ):
        """
        Движеное вправо
        """

        return self.drow_matrix()

    def move_left(self, ):
        """
        Движение влево
        """

        return self.drow_matrix()

    def move_up(self, ):
        """
        Движеное вверх
        """

        return self.drow_matrix()

    def move_down(self, ):
        """
        Движение вниз
        """

        return self.drow_matrix()
    ...


abc = GameCirulli(4)
