class TicTacToe:
    check_buzy_cell = bool

    def __init__(self):
        self.check1 = 0
        self.game = bool
        self.win_symb_1 = 0
        self.win_symb_2 = 0
        self.field = [] # field - поле


    def new_game(self):
        self.check1 = not self.check1
        self.check = not self.check1

        print("Новая игра")
        self.a = 3
        self.field = ['-'] * self.a
        for i in range(self.a):
            self.field[i] = ['-'] * self.a

    def choice_of_symbol(self):
        self.symb_1, self.symb_2 = input("введите два символа через пробел, которыми вы будете играть:\n").split()
        print(f"первый игрок: {self.symb_1} \nвторой игрок: {self.symb_2}")


    def get_field(self):
        for i in range(self.a):
            print(" ".join(self.field[i]))

    def make_move(self):
        self.check_buzy_cell = 1
        if self.check:
            while self.check_buzy_cell:
                row, column = map(int, input(f"ход {self.symb_1}\nВведите номер строки и номер столбца через пробел\n").split())
                if self.field[row - 1][column - 1] == "-":
                    self.field[row - 1][column - 1] = self.symb_1
                    self.check_buzy_cell = 0
                    self.check = 0
                else:
                    print("эта ячейка занята")


        else:
            while self.check_buzy_cell:
                row, column = map(int, input(f"ход {self.symb_2}\nВведите номер строки и номер столбца через пробел\n").split())
                if self.field[row - 1][column - 1] == "-":
                    self.field[row - 1][column - 1] = self.symb_2
                    self.check_buzy_cell = 0
                    self.check = 1
                else:
                    print("эта ячейка занята")

    def check_field(self):
        t = self.field
        for i in range(len(t)):
            for j in range(len(t[i])):
                if t[i][0] == t[i][1] == t[i][2] != "-" or t[0][j] == t[1][j] == t[2][j] != "-":
                    win = 1
                    return win

                elif t[0][0] == t[1][1] == t[2][2] != "-" or t[0][2] == t[1][1] == t[2][0] != "-":
                    win = 1
                    return win

                elif "-" not in t[0] + t[1] + t[2]:
                    win = 2
                    return win

    def who_win(self, a: int):
        if a == 1:
            if self.check:
                self.win_symb_2 += 1
                print(f"победил {self.symb_2}")
                self.game = 0
            else:
                self.win_symb_1 += 1
                print(f"победил {self.symb_1}")
                self.game = 0

        elif a == 2:
            print("игра окончена, никто не победил")
            self.game = 0

    def total_score(self):
        print(f"\nобщий счёт: \n{self.symb_1}: {self.win_symb_1} \n{self.symb_2}: {self.win_symb_2}\n")


p = TicTacToe()
p.choice_of_symbol()
while True:
    p.game = 1
    p.new_game()
    p.total_score()
    while p.game:
        p.make_move()
        print()
        p.get_field()
        print()

        p.who_win(p.check_field())

