import random as rand
import os
from typing import Callable

# Constants for the game configuration
GUESSES = 10
BOARD_SIZE_X = 5
BOARD_SIZE_Y = 5

# Symbols used on the board
HIDDEN = "O"
SHIP = "S"
GUESS = "X"

def user_input(prompt: str, min_value: int = 1, max_value: int = BOARD_SIZE_X) -> int:
    """
    Prompt the user for input and ensure it is within the specified range.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input, please enter a number.")

def player_guesses(already_guessed: Callable[[int, int], bool]) -> tuple[int, int]:
    """
    Obtain valid guess coordinates from the player.
    """
    while True:
        guess_row = user_input("Guess row (1-5): ", max_value=BOARD_SIZE_Y) - 1
        guess_col = user_input("Guess column (1-5): ", max_value=BOARD_SIZE_X) - 1
        if not already_guessed(guess_row, guess_col):
            return guess_row, guess_col
        else:
            print("That spot has already been guessed. Try again.")

def computer_guesses(already_guessed: Callable[[int, int], bool], size_x: int, size_y: int) -> tuple[int, int]:
    """
    Generate valid guess coordinates for the computer.
    """
    while True:
        guess_row = rand.randint(0, size_y - 1)
        guess_col = rand.randint(0, size_x - 1)
        if not already_guessed(guess_row, guess_col):
            return guess_row, guess_col

class BattleshipBoard:
    def __init__(self, size_x: int, size_y: int) -> None:
        """
        Initialize the board and place the ship.
        """
        self.grid = [[HIDDEN] * size_x for _ in range(size_y)]
        self.ship_row = rand.randint(0, size_y - 1)
        self.ship_col = rand.randint(0, size_x - 1)
        self.grid[self.ship_row][self.ship_col] = SHIP

    def is_ship(self, row: int, col: int) -> bool:
        """
        Check if the given coordinates contain the ship.
        """
        return self.grid[row][col] == SHIP

    def already_guessed(self, row: int, col: int) -> bool:
        """
        Check if the given coordinates have already been guessed.
        """
        return self.grid[row][col] == GUESS

    def place_guess(self, row: int, col: int) -> None:
        """
        Mark the guessed position on the board.
        """
        if not self.is_ship(row, col):
            self.grid[row][col] = GUESS

    def display(self, show_ship: bool = False) -> str:
        """
        Display the board to the player.
        """
        rows_str = []
        for row in self.grid:
            rows_str.append(" ".join([HIDDEN if col == SHIP and not show_ship else col for col in row]))
        return "\n".join(rows_str)

def turn(board: BattleshipBoard, player: str) -> bool:
    """
    Execute a single turn of the game.
    """
    if player == "Player":
        print("Your Board:")
        print(board.display(show_ship=True))
        guess_row, guess_col = player_guesses(board.already_guessed)
    else:  # Computer's turn
        guess_row, guess_col = computer_guesses(board.already_guessed, BOARD_SIZE_X, BOARD_SIZE_Y)
        print(f"Computer guesses row {guess_row + 1}, column {guess_col + 1}")
    
    board.place_guess(guess_row, guess_col)
    return board.is_ship(guess_row, guess_col)

def play_game() -> None:
    """
    Main game loop for playing Battleship.
    """
    os.system("clear")
    player_board = BattleshipBoard(BOARD_SIZE_X, BOARD_SIZE_Y)
    computer_board = BattleshipBoard(BOARD_SIZE_X, BOARD_SIZE_Y)
    total_guesses = 0

    while total_guesses < GUESSES * 2:
        current_player = "Player" if total_guesses % 2 == 0 else "Computer"
        remaining_guesses = GUESSES - total_guesses // 2

        print(f"{current_player}'s turn: {remaining_guesses} guesses left.")

        if current_player == "Player":
            if turn(computer_board, current_player):
                print("You sank the computer's ship!")
                break
            else:
                print("You missed!")
        else:
            if turn(player_board, current_player):
                print("Computer sank your ship!")
                break
            else:
                print("Computer missed!")

        total_guesses += 1

    if total_guesses >= GUESSES * 2:
        print("Game Over. The ships weren't found.")
    print("Final Boards:")
    print("Your Board:")
    print(player_board.display(show_ship=True))
    print("Computer's Board:")
    print(computer_board.display(show_ship=True))

def main() -> None:
    os.system("clear")
    print("Welcome to Battleship! Locate and sink your enemy's ship.")
    while True:
        play_game()
        if input("Do you want to play again? (yes/no): ").strip().lower() != 'yes':
            print("Thank you for playing Battleship!")
            break

if __name__ == "__main__":
    main()
