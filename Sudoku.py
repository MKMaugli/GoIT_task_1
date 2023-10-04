import tkinter as tk
import random

class SudokuGame:
    def __init__(self, level):
        self.level = level
        self.board = self.generate_board()
        self.solution = self.solve_board(self.board)
        self.remaining_cells = self.get_remaining_cells()
        self.errors = 0

    def generate_board(self):
        board = [[0 for _ in range(9)] for _ in range(9)]

        # Заполняем диагонали квадратов 3x3 случайными числами
        for i in range(0, 9, 3):
            self.fill_square(board, i, i)

        # Решаем доску и сохраняем решение
        self.solution = self.solve_board(board)

        # Удаляем некоторое количество чисел в зависимости от уровня сложности
        self.remove_numbers(board)

        return board
    
    def fill_square(self, board, row, col):
        nums = list(range(1, 10))
        random.shuffle(nums)

        for i in range(3):
            for j in range(3):
                board[row + i][col + j] = nums.pop()

    def remove_numbers(self, board):
        num_to_remove = 0

        if self.level == "Сложный":
            num_to_remove = 54
        elif self.level == "Средний":
            num_to_remove = 57
        elif self.level == "Легкий":
            num_to_remove = 63

        for _ in range(num_to_remove):
            while True:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
                if board[row][col] != 0:
                    board[row][col] = 0
                    break

    def solve_board(self, board):
        empty_cell = self.find_empty_cell(board)
        if not empty_cell:
            return True  # Доска решена, нет пустых клеток

        row, col = empty_cell

        for num in range(1, 10):
            if self.is_valid_move(board, row, col, num):
                board[row][col] = num

                if self.solve_board(board):
                    return True  # Решение найдено

                board[row][col] = 0  # Откат изменений

        return False  # Решение не найдено

    def find_empty_cell(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return (row, col)
        return None

    def get_remaining_cells(self):
        remaining_cells = []

        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    remaining_cells.append((row, col))

        return remaining_cells
    
    def is_valid_move(self, board, row, col, num):
        # Проверяем, что число num не встречается в строке
        if num in board[row]:
            return False

        # Проверяем, что число num не встречается в столбце
        if num in [board[i][col] for i in range(9)]:
            return False

        # Проверяем, что число num не встречается в квадрате 3x3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def check_board(self):
        if not self.is_board_filled():
            return False  # Есть пустые клетки

        return self.is_valid_sudoku()

    def is_board_filled(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return False
        return True

    def is_valid_sudoku(self):
        for row in range(9):
            for col in range(9):
                num = self.board[row][col]
                if not self.is_valid_move(self.board, row, col, num):
                    return False
        return True

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Судоку")

        self.level = tk.StringVar()
        self.level.set("Легкий")

        self.game = None

        self.create_menu()
        self.create_board()
        self.create_buttons()
        self.generate_new_board()

    def create_menu(self):
        menu = tk.Menu(self.root)
        root.config(menu=menu)

        difficulty_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Уровень", menu=difficulty_menu)
        difficulty_menu.add_radiobutton(label="Легкий", variable=self.level, value="Легкий")
        difficulty_menu.add_radiobutton(label="Средний", variable=self.level, value="Средний")
        difficulty_menu.add_radiobutton(label="Сложный", variable=self.level, value="Сложный")

    def create_board(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.cells = []
        for row in range(9):
            row_cells = []
            for col in range(9):
                cell = tk.Entry(self.board_frame, width=2, font=("Arial", 16), justify="center")
                cell.grid(row=row, column=col)
                row_cells.append(cell)
            self.cells.append(row_cells)

    def create_buttons(self):
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        # Кнопка "Проверить доску"
        check_button = tk.Button(self.button_frame, text="Проверить доску", command=self.check_board)
        check_button.pack()

        # Кнопка "Переделать поле"
        generate_button = tk.Button(self.button_frame, text="Переделать поле", command=self.generate_new_board)
        generate_button.pack()

    def generate_new_board(self):
        # Создать новую игру судоку с выбранным уровнем сложности
        self.game = SudokuGame(self.level.get())

        # Очистить все ячейки на доске и интерфейсе
        for row in self.cells:
            for cell in row:
                cell.delete(0, tk.END)

        # Заполнить игровую доску новой генерированной доской
        for row in range(9):
            for col in range(9):
                value = self.game.board[row][col]
                if value != 0:
                    self.cells[row][col].insert(0, str(value))

    def check_board(self):
        # Получить значения из всех ячеек на игровой доске в виде двумерного списка
        current_board = []
        for row in self.cells:
            row_values = []
            for cell in row:
                value = cell.get()
                if value.isdigit():
                    row_values.append(int(value))
                else:
                    row_values.append(0)
            current_board.append(row_values)

        # Проверить, правильно ли заполнена доска
        is_correct = self.game.check_board(current_board)
        print ("Доска правильно заполнена!")

        # Вывести сообщение о результате проверки
        if is_correct:
            message = "Доска правильно заполнена!"
        else:
            message = "Есть ошибки в доске. Пожалуйста, проверьте её ещё раз."
            print ("Доска с ошибками!")

        result_label = tk.Label(self.root, text=message)
        result_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGUI(root)
    root.mainloop()
