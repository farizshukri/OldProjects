import tkinter as tk
from tkinter import messagebox

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.board = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                self.board[i][j].set('')
                self.entries[i][j] = tk.Entry(root, width=3, font=('Arial', 18),
                                              textvariable=self.board[i][j], justify='center')
                self.entries[i][j].grid(row=i, column=j)
        
        solve_button = tk.Button(root, text="Solve Sudoku", command=self.solve_sudoku)
        solve_button.grid(row=9, columnspan=9)

    def solve_sudoku(self):
        board = [[0]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                try:
                    value = int(self.board[i][j].get())
                    if 1 <= value <= 9:
                        board[i][j] = value
                    else:
                        messagebox.showerror("Error", "Please enter numbers between 1 to 9")
                        return
                except ValueError:
                    board[i][j] = 0

        if self.solve(board):
            for i in range(9):
                for j in range(9):
                    self.board[i][j].set(board[i][j])
        else:
            messagebox.showerror("Error", "No solution exists")

    def solve(self, board):
        find = self.find_empty(board)
        if not find:
            return True
        else:
            row, col = find

        for num in range(1, 10):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num

                if self.solve(board):
                    return True

                board[row][col] = 0

        return False

    def is_valid(self, board, num, pos):
        # Check row
        for i in range(len(board[0])):
            if board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check 3x3 box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()
