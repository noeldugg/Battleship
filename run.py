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

def turn(board: BattleshipBoard) -> bool:
    """
    Execute a single turn of the game.
    """
    print(board.display())
    guess_row, guess_col = player_guesses(board.already_guessed)
    board.place_guess(guess_row, guess_col)
    return board.is_ship(guess_row, guess_col)

def play_game(player_count: int, board: BattleshipBoard) -> None:
    """
    Main game loop for playing Battleship.
    """
    os.system("clear")
    total_guesses = 0

    while total_guesses < GUESSES * player_count:
        current_player = (total_guesses % player_count) + 1
        remaining_guesses = GUESSES - total_guesses // player_count

        print(f"Player {current_player}'s turn: {remaining_guesses} guesses left.")
        
        if turn(board):
            print(f"Player {current_player} sank the ship!")
            break
        else:
            print("You missed!")
        total_guesses += 1

    if total_guesses >= GUESSES * player_count:
        print("Game Over. The ship wasn't found.")
    print(board.display(show_ship=True))

def main() -> None:
    os.system("clear")
    print("Welcome to Battleship! Locate and sink your enemy's ship.")
    while True:
        player_count = user_input("Enter the number of players (1-2): ", max_value=2)
        board = BattleshipBoard(BOARD_SIZE_X, BOARD_SIZE_Y)
        play_game(player_count, board)
        if input("Do you want to play again? (yes/no): ").strip().lower() != 'yes':
            print("Thank you for playing Battleship!")
            break

if __name__ == "__main__":
    main()
