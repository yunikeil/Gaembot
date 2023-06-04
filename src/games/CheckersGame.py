import random
import string
import os
from typing import Optional

from PIL import Image, ImageDraw,ImageFont,ImageOps
import nextcord




class GameCheckersStartView(nextcord.ui.View):
    def __init__(self, *, timeout: float | None = 180, auto_defer: bool = True) -> None:
        super().__init__(timeout=timeout, auto_defer=auto_defer)
        self.category_id: int = 1093504561538412654

    @nextcord.ui.button(label="Начать игру!", style=nextcord.ButtonStyle.green)
    async def start(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        button.disabled = True
        game = GameCheckersView()
        await interaction.response.send_message(view=game, file=game.output())
        await interaction.message.edit(view=self)



class NextStep(nextcord.ui.Modal):
    def __init__(self, checkers=None, message=None):
        super().__init__(
            "Ваш ход:",
            timeout=5 * 60,  # 5 minutes
        )
        self.checkers = checkers
        self.message = message

        self.name = nextcord.ui.TextInput(
            label="Начальные ккординаты x1:y1, c:1",
            required=True,
            min_length=1,
            max_length=2,
        )
        self.add_item(self.name)

        self.description = nextcord.ui.TextInput(
            label="Конечные координаты x2:y2, d:2",
            required=True,
            min_length=1,
            max_length=2,
        )
        self.add_item(self.description)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        x1 = self.name.value.split(':')[0]
        y1 = self.name.value.split(':')[1]
        x2 = self.description.value.split(':')[0]
        y2 = self.description.value.split(':')[1]
        ans = self.checkers.logic(x1, int(y1), x2, int(y2))
        image = self.checkers.output(ans)
        await interaction.channel.send(file=image)
        if self.checkers.end():
            await interaction.channel.send("Игра окончена")
            await self.message.edit(view=None)

        


class GameCheckersView(nextcord.ui.View):
    def __init__(self, *, timeout: float | None = 180, auto_defer: bool = True):
        super().__init__(timeout=timeout, auto_defer=auto_defer)
        file_dir = os.path.dirname(os.path.abspath(__file__))
        self.temp_path = os.path.join(file_dir, "temp")
        self.temp_files = []
        self.last_move = 2
        self.last_checker = [-1, -1]
        self.move = 1
        self.end = False
        self.winner = 0
        self.mass = [[1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0], [0, 2, 0, 2, 0, 2, 0, 2]]

    def __del__(self):
        for path in self.temp_files:
            os.remove(path)

    def convert_coords(self, x1, y1, x2, y2):
        # Функция преобразует координаты из координат на игральной доске в координаты,
        # удобные для взаимодействия с матрицей
        diction = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
                'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        y1 = int(y1) - 1
        y2 = int(y2) - 1
        x1 = diction[x1]
        x2 = diction[x2]
        return x1, y1, x2, y2
    

    def logic(self, x1, y1, x2, y2):
        # Главная функция, осуществляющая проверку возможности совершения хода, запрашиваемого пользователем
        # Если ход возможен, он будет выполнен и возможность следующего хода либо перейдёт к сопернику,
        # либо будет предоставлена обоим игрокам в том случае, если игрок, совершивший ход,
        # также может продолжить его, если сам заметит такую возможность
        list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        list2 = ['1', '2', '3', '4', '5', '6', '7', '8']
        if (x1 not in list1) or (y1 not in list2) or (x2 not in list1) or (y2 not in list2):
            return 'Ход невозможен 1'
        x1, y1, x2, y2 = self.convert_coords(x1, y1, x2, y2)
        if self.mass[x1][y1] == 0 or self.mass[x2][y2] != 0 or x1 == x2 or y1 == y2:
            return 'Ход невозможен 2'
        if self.move == 1 and (self.mass[x1][y1] == 2 or self.mass[x1][y1] == 4):
            return 'Сейчас ходят белые'
        if self.move == 2 and (self.mass[x1][y1] == 1 or self.mass[x1][y1] == 3):
            return 'Сейчас ходят чёрные'
        if self.mass[x1][y1] < 3 and abs(x2-x1) == 1 and abs(y2-y1) == 1:
            if not (self.mass[x1][y1] == 1 and x2 - x1 == 1 or self.mass[x1][y1] == 2 and x2 - x1 == -1):
                return "Ход невозможен 8"
            if self.move == 3 and (self.mass[self.last_checker[0]][self.last_checker[1]] == self.mass[x1][y1] or
                                   self.mass[self.last_checker[0]][self.last_checker[1]] == self.mass[x1][y1] + 2):
                return 'Ход невозможен 3'
            self.mass[x2][y2] = self.mass[x1][y1]
            self.mass[x1][y1] = 0
            self.last_move = 2 - self.mass[x2][y2] % 2
            self.move = self.last_move % 2 + 1
            if self.mass[x2][y2] == 1 and x2 == 7 or self.mass[x2][y2] == 2 and x2 == 0:
                self.mass[x2][y2] += 2
            self.end = self.end_check()
            if self.end:
                self.winner = self.last_move
            return 'Ход выполнен 1'
        if self.mass[x1][y1] < 3 and abs(x2-x1) == 2 and abs(y2-y1) == 2 \
                and (self.mass[int((x1+x2)/2)][int((y1+y2)/2)] == self.mass[x1][y1] % 2 + 1
                     or self.mass[int((x1+x2)/2)][int((y1+y2)/2)] == self.mass[x1][y1] % 2 + 3):
            if self.move == 3 and (self.mass[self.last_checker[0]][self.last_checker[1]] == self.mass[x1][y1] or
                                   self.mass[self.last_checker[0]][self.last_checker[1]] == self.mass[x1][y1] + 2) \
                    and self.last_checker != [x1, y1]:
                return 'Ход невозможен 4'
            self.mass[x2][y2] = self.mass[x1][y1]
            self.mass[x1][y1] = 0
            self.mass[int((x1+x2)/2)][int((y1+y2)/2)] = 0
            self.last_move = 2 - self.mass[x2][y2] % 2
            if self.mass[x2][y2] == 1 and x2 == 7 or self.mass[x2][y2] == 2 and x2 == 0:
                self.mass[x2][y2] += 2
            if self.check_next_move(x2, y2):
                self.move = 3
                self.last_checker = [x2, y2]
            else:
                self.move = self.last_move % 2 + 1
            self.end = self.end_check()
            if self.end:
                self.winner = self.last_move
            return 'Ход выполнен 2'
        if self.mass[x1][y1] > 2 and abs(x2-x1) == abs(y2-y1):
            count = 0
            dx = int((x2 - x1)/abs(x2 - x1))
            dy = int((y2 - y1)/abs(y2 - y1))
            x = x1 + dx
            y = y1 + dy
            t = True
            move_ = 0
            x_ = -1
            y_ = -1
            if self.mass[x1][y1] == 1 or self.mass[x1][y1] == 3:
                move_ = 1
            else:
                move_ = 2
            while x != x2:
                if self.mass[x][y] == move_ or self.mass[x][y] == move_ + 2:
                    t = False
                    break
                if self.mass[x][y] == move_ % 2 + 1 or self.mass[x][y] == move_ % 2 + 3:
                    count += 1
                    x_ = x
                    y_ = y
                x += dx
                y += dy
            if not (count == 1 and x_ != -1 or count == 0):
                t = False
            if t and count == 1:
                if self.move == 3 and (self.mass[self.last_checker[0]][self.last_checker[1]] == self.mass[x1][y1] or
                                       self.mass[self.last_checker[0]][self.last_checker[1]] == self.mass[x1][y1] - 2) \
                        and self.last_checker != [x1, y1]:
                    return 'Ход невозможен 5'
                self.mass[x_][y_] = 0
                self.mass[x2][y2] = self.mass[x1][y1]
                self.mass[x1][y1] = 0
                self.last_move = 2 - self.mass[x2][y2] % 2
                if self.check_next_move(x2, y2):
                    self.move = 3
                    self.last_checker = [x2, y2]
                else:
                    self.move = self.last_move % 2 + 1
                self.end = self.end_check()
                if self.end:
                    self.winner = self.last_move
                return 'Ход выполнен 3'
            if t and count == 0:
                if self.move == 3 and (self.mass[self.last_checker[0]][self.last_checker[1]] == self.mass[x1][y1] or
                                       self.mass[self.last_checker[0]][self.last_checker[1]] == self.mass[x1][y1] - 2):
                    return 'Ход невозможен 6'
                self.mass[x2][y2] = self.mass[x1][y1]
                self.mass[x1][y1] = 0
                self.last_move = 2 - self.mass[x2][y2] % 2
                self.move = self.last_move % 2 + 1
                self.end = self.end_check()
                if self.end:
                    self.winner = self.last_move
                return 'Ход выполнен 4'
        return 'Ход невозможен 7'


    def end_check(self):
        # Функция проверяет возможность игрока, который должен ходить следующим, совершить ход
        # Если такой возможности нет, игра завершается победой игрока, который совершил ход последним
        check_side = self.last_move % 2 + 1
        t = False
        for i in range(8):
            for j in range(8):
                if self.mass[i][j] == check_side or self.mass[i][j] == check_side + 2:
                    t = self.check_one(i, j)
                if t:
                    break
            if t:
                break
        return not t

    def check_one(self, x, y):
        # Функция проверяет возможность хода конкретной шашки игрока
        # Вызывается для каждой шашки игрока, проверяемого в функции end_check
        if (x > 0 and y > 0 and self.mass[x-1][y-1] == 0) or (x > 0 and y < 7 and self.mass[x-1][y+1] == 0):
            return True
        if (x < 7 and y > 0 and self.mass[x+1][y-1] == 0) or (x < 7 and y < 7 and self.mass[x+1][y+1] == 0):
            return True
        if (x > 1 and y > 1 and self.mass[x-1][y-1] == self.last_move and self.mass[x-2][y-2] == 0) \
                or (x > 1 and y < 6 and self.mass[x-1][y+1] == self.last_move and self.mass[x-2][y+2] == 0) \
                or (x < 6 and y > 1 and self.mass[x+1][y-1] == self.last_move and self.mass[x+2][y-2] == 0) \
                or (x < 6 and y < 6 and self.mass[x+1][y+1] == self.last_move and self.mass[x+2][y+2] == 0):
            return True
        return False

    def check_next_move(self, x, y):
        # Функция проверяет для шашки, совершившей последний ход, возможность продолжить его
        enemy_side = self.last_move % 2 + 1
        if self.mass[x][y] == self.last_move:
            if (x > 1 and y > 1 and self.mass[x - 1][y - 1] == enemy_side and self.mass[x - 2][y - 2] == 0) \
                    or (x > 1 and y < 6 and self.mass[x - 1][y + 1] == enemy_side and self.mass[x - 2][y + 2] == 0) \
                    or (x < 6 and y > 1 and self.mass[x + 1][y - 1] == enemy_side and self.mass[x + 2][y - 2] == 0) \
                    or (x < 6 and y < 6 and self.mass[x + 1][y + 1] == enemy_side and self.mass[x + 2][y + 2] == 0):
                return True
        if self.mass[x][y] == self.last_move + 2:
            x_t = x - 1
            y_t = y - 1
            while x_t >= 1 and y_t >= 1:
                if self.mass[x_t][y_t] == self.last_move or self.mass[x_t][y_t] == self.last_move + 2:
                    break
                if (self.mass[x_t][y_t] == enemy_side or self.mass[x_t][y_t] == enemy_side + 2) \
                        and self.mass[x_t - 1][y_t - 1] == 0:
                    return True
                x_t -= 1
                y_t -= 1
            x_t = x + 1
            y_t = y - 1
            while x_t <= 6 and y_t >= 1:
                if self.mass[x_t][y_t] == self.last_move or self.mass[x_t][y_t] == self.last_move + 2:
                    break
                if (self.mass[x_t][y_t] == enemy_side or self.mass[x_t][y_t] == enemy_side + 2) \
                        and self.mass[x_t + 1][y_t - 1] == 0:
                    return True
                x_t += 1
                y_t -= 1
            x_t = x - 1
            y_t = y + 1
            while x_t >= 1 and y_t <= 6:
                if self.mass[x_t][y_t] == self.last_move or self.mass[x_t][y_t] == self.last_move + 2:
                    break
                if (self.mass[x_t][y_t] == enemy_side or self.mass[x_t][y_t] == enemy_side + 2) \
                        and self.mass[x_t - 1][y_t + 1] == 0:
                    return True
                x_t -= 1
                y_t += 1
            x_t = x + 1
            y_t = y + 1
            while x_t <= 6 and y_t <= 6:
                if self.mass[x_t][y_t] == self.last_move or self.mass[x_t][y_t] == self.last_move + 2:
                    break
                if (self.mass[x_t][y_t] == enemy_side or self.mass[x_t][y_t] == enemy_side + 2) \
                        and self.mass[x_t + 1][y_t + 1] == 0:
                    return True
                x_t += 1
                y_t += 1
        return False

    def output(self,ans=""):
        img = Image.new('RGBA', (405, 450), 'gray')
        idraw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", size=28)
        if ans != "":
            idraw.text((10, 10), ans, font=font)

        x_draw = 50
        y_draw = 96
        z= True
        for y in range(7,-1,-1):
            for x in range(8):
                if z%2 == True:
                    idraw.rectangle((x_draw-10,y_draw-10 ,x_draw+35 ,y_draw+35), fill='white', outline=(255, 255, 255))
                    z=False
                else:
                    idraw.rectangle((x_draw-10, y_draw-10, x_draw+35, y_draw+35), fill='brown', outline=(255, 255, 255))
                    z=True
                if self.mass[y][x]== 1:
                    idraw.ellipse((x_draw-5, y_draw-5, x_draw + 25, y_draw + 25), 'white')
                if self.mass[y][x]== 2:
                    idraw.ellipse((x_draw-5, y_draw-5, x_draw + 25, y_draw + 25), 'black')
                if self.mass[y][x]== 3:
                    idraw.ellipse((x_draw-5,y_draw-5, x_draw+25,y_draw+25),'white')
                    idraw.ellipse((x_draw+5, y_draw+5, x_draw + 15, y_draw + 15), 'black')
                if self.mass[y][x]== 4:
                    idraw.ellipse((x_draw-5, y_draw-5, x_draw + 25, y_draw + 25), 'black')
                    idraw.ellipse((x_draw+5, y_draw+5, x_draw + 15, y_draw + 15), 'white')

                x_draw += 45
            y_draw += 45
            x_draw = 50
            if z==False:
                z=True
            else:
                z=False
        #img.save('meow.png')
        # img = ImageOps.mirror(img)
        text = "HGFEDCBA"
        font = ImageFont.truetype("arial.ttf", size=28)
        y = 90
        for i in range(len(text)):
            idraw.text((10, y), text[i], font=font)
            # idraw.line(((0, y-10),(450,y-10)))
            y += 45
        x = 45
        for i in range(len(text)):
            text = str(i + 1)
            idraw.text((x, 45), text=text, font=font)
            # idraw.line(((x-10, 40),(x-10,450)))
            x += 45
        filename = os.path.join(
            f"{self.temp_path}",
            f"{''.join(random.choice(string.ascii_lowercase) for _ in range(21))}.png",
        )
        img.save(filename)
        self.temp_files.append(filename)
        return nextcord.File(filename)
        

    @nextcord.ui.button(label="Начать ход!", style=nextcord.ButtonStyle.grey)
    async def next_steep(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        await interaction.response.send_modal(NextStep(checkers=self, message=interaction.message))
















