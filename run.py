from random import randint

    

GUESSES = 10
BOARD_SIZE_X = 10
BOARD_SIZE_Y = 10

#Represents elements on the board
HIDDEN = "O"
SHIP = "S"
GUESS = "X"


    
def user_input(min_value: int = 1,max_value: int = 10) -> int:
    """
    Reads an integer that will provide a min and max value
     """
    while True:
        line = input(prompt)
        try: 
            value = int(line)
            if value < min_value:
                print(f"The minium value is {min_value}. Try again.")
            elif value > max_value:
                print(f"The maxium value is {max_value}. Try again.")
            else: 
                return value
        except ValueError:
            print("Not a number, try again")
             



def player_guesses(self,already_guessed: Callable[[int, int], bool]) -> tuple[int,int]:
    while True:
     # reads row and column
        guess_row = user_input("Guess row: ", max_value=10) - 1
        guess_col = user_input("Guess column: ", max_value=10) - 1
        
     # if guess is value return guessed row and column
        if not already_guessed(guess_row, guess_col):
            return guess_row, guess_col

class BattleshipBoard:

    def __init__(self, size_x: int, size_y: int) -> None:
        #Create the Grid
        self.grid = [[HIDDEN] * size_x for _ in range(size_y)]

        # place a random ship on the grid 
        self.ship_row = rand.randint(0,size_x - 1)
        self.ship_col = rand.randint(0,size_y - 1)
        self.grid[ship_row][ship_col] = SHIP 

    def is_ship(self, row: int, col: int) -> bool:
        return self.grid[row][col] == SHIP

    def already_guessed(self,row:int,col: int) -> bool:
        return self.grid[row][col] == GUESS

    def place_guess(self,row: int, col: int) -> None:
        if not self.is_ship(row,col):
            self.grid[row][col] = GUESS

    def to_string(self, show_ship: bool = False) -> str:
        rows_str: list[str] = []
        for row in self.grid:
            row_repr = [HIDDEN if col == SHIP and not show_ship else col for col in row]
            rows_str.append(" ".join(row_repr))
        return "\n".join(rows_str)

def turn(board:BattleshipBoard) -> bool:
    """
    Single Players Turn
    """

    print(board.to_string())

    #let the player guess
    guess_row, guess_col = read_guess(board.already_guessed)
    board.place_guess(guess_row, guess_col)

    return board.is_ship(guess.row, guess_col)

def play_game(player_count: int, board: BattleshipBoard) -> None:
    """
    Play a game of Battleship with a given number of players
    """

    os.system("clear")
    
    total_guesses = 0 

    while total_guesses < GUESSES_COUNT * player_count:
        # determine the current player and the remaining guesses for that player
        current_player = (total_guesses % player_count) + 1
        remaining_guesses = GUESSES_COUNT - total_guesses // player_count

        print(f"Player {current_player}'s turn: {remaining_guesses} guesses left.")
        
        if turn(board):
            print(f" Player {current_player} sank the ship")
            break
        else:
            print("You missed!" )

        total_guesses += 1

class Game:
    def __init__(self,players):
        self.player_list = []
        for player in range(players):
            self.player_list.append(GUESSES_COUNT)
            self.current_player = 1
        self.board = BattleshopBoard(BOARD_SIZE_X, BOARD_SIZE_Y)
           


def game_logic(self):
    guess_row, guess_col = read_guess(self.board.already_guessed)

    if (
        self.board[guess_row][guess_col]
        == self.board[self.ship_row][self.ship_col]

    ):

        return True 
    else:
        if self.player_list[self.current_player - 1] > 0:
            print("You missed")
            self.board[guess_row][guess_col] = "X"
            self.board_visible[guess_row][guess_col] = "X"
            self.player_list[self.current_player - 1] -= 1
            self.print_board(self.board_visible)

            if len(self.player_list) > 1:
                self.current_player += 1
            if self.current_player > len(self.player_list):
                self.current_player = 1
            return self.game_logic()
        else:
            print("Player {} ran out of guesses". format(self.current_player))
            return False











def main() -> None:
    os.system("clear")
    player_count = user_input("Enter how many Players are playing", max_value=2)
    battleship = Game(player_count)
    battleship.main()

if __name__ == "__main__":
    main()
