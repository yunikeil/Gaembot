import nextcord

from typing import List, Optional




class TicTacToeStartView(nextcord.ui.View):
    def __init__(self, *, timeout: float | None = 180, auto_defer: bool = True) -> None:
        super().__init__(timeout=timeout, auto_defer=auto_defer)
        self.category_id: int = 1093504369648996473
    
    @nextcord.ui.button(label="Начать игру!", style=nextcord.ButtonStyle.green)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message(view=TicTacToe())

    ...


class TicTacToeButton(nextcord.ui.Button["TicTacToe"]):
    """
    Класс представляющий кнопку на поле TicTacToe. Служит для отображения 
    текущего состояния игры в виде крестиков и ноликов.

    Атрибуты:
        x (int): Позиция кнопки по горизонтали.
        y (int): Позиция кнопки по вертикали.

    Методы:
        callback: Обработчик событий нажатия на кнопки.

    """

    def __init__(self, x: int, y: int):
        super().__init__(style=nextcord.ButtonStyle.secondary, label="\u200b", row=y)
        self.x = x
        self.y = y

    async def callback(self, interaction: nextcord.Interaction):
        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.x]
        if state in (view.X, view.O):
            return

        if view.current_player == view.X:
            self.style = nextcord.ButtonStyle.danger
            self.label = "X"
            self.disabled = True
            view.board[self.y][self.x] = view.X
            view.current_player = view.O
            content = "It is now O's turn"
        else:
            self.style = nextcord.ButtonStyle.success
            self.label = "O"
            self.disabled = True
            view.board[self.y][self.x] = view.O
            view.current_player = view.X
            content = "It is now X's turn"

        winner = view.check_board_winner()
        if winner is not None:
            if winner == view.X:
                content = "X won!"
            elif winner == view.O:
                content = "O won!"
            else:
                content = "It's a tie!"

            for child in view.children:
                child.disabled = True

            view.stop()

        await interaction.response.edit_message(content=content, view=view)


class TicTacToe(nextcord.ui.View):
    """
    Класс представляющий поле игры TicTacToe. Служит для создания и отображения 
    игрового поля с кнопками.

    Атрибуты:
        children (List[TicTacToeButton]): Список кнопок на доске.
        X (int): Константа для обозначения игрока X.
        O (int): Константа для обозначения игрока O.
        Tie (int): Константа для обозначения ничьей.
        current_player (int): Текущий игрок на доске.
        board (List[List[int]]): Двумерный список для хранения состояния доски.

    Методы:
        check_board_winner: проверяет завершилась игра или нет.
    """
    children: List[TicTacToeButton]
    X = -1
    O = 1
    Tie = 2

    def __init__(self):
        super().__init__()
        self.current_player = self.X
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y))

    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        for line in range(3):
            value = self.board[0][line] + \
                self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None
