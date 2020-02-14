
import SudokuSolver
import Visualizer
import Board
import time

def main():
    sudokuSolver = SudokuSolver.SudokuSolver()
    visualizer = Visualizer.Visualizer()
    #creates the board starting message
    currentBoard = ["..23....4",
                    ".8..69...",
                    "4592.716.",
                    "145.92.38",
                    "67..1..4.",
                    "2.....651",
                    ".17..63..",
                    ".......75",
                    "8.45...1."]
    board = Board.Board(currentBoard)

    visualizer.drawBoard(board)

    solved = False
    while solved == False:
        solved = sudokuSolver.next(board)
        if solved == False:
            visualizer.drawBoard(board)
            print("--------------------------------------------------")
            #time.sleep(0.5)
    print("solved!")
    time.sleep(1)
    exit()

main()