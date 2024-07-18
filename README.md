# ULTIMATE Battleship

Ultimate Battleship is a Python terminal game that challenges players to find and sink their opponent's ship before their own ship is discovered. This game runs in a terminal environment.

[Here is the live version of my project.](https://battleshipsss-b1a21ca3ddfb.herokuapp.com/)





## How to play

Ultimate Battleship is based on the classic pen-and-paper game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).

![Game Screenshot](https://github.com/user-attachments/assets/00b6ff21-7d86-4294-9cd6-583377c3f34e)
In this version, the player enters their name and two boards are randomly generated.

- The player can see where their ships are, indicated by an `S`, but cannot see where the computer’s ships are.
- Guesses are marked on the board with an `X`. Hits are indicated by `*`.
- The player and the computer take turns to make guesses and try to sink each other’s battleships.
- The winner is the player who sinks all of their opponent’s battleships first.

## Features

### Existing Features

- **Random board generation**
  - Ships are randomly placed on both the player and computer boards
  - The player cannot see where the computer’s ships are
  - ![Screenshot 2024-07-18 18 59 30](https://github.com/user-attachments/assets/fdaa6771-364f-4c6d-8ca1-93f6f3e1acb0)


- **Play against the computer**
- **Accepts user input**
- **Maintains scores**
- **Input validation and error-checking**
  - You cannot enter coordinates outside the size of the grid
  - You must enter numbers
  - You cannot enter the same guess twice

![Screenshot 2024-07-18 19 02 09](https://github.com/user-attachments/assets/6071fe34-9644-483b-97c8-e355f83774b2)

- **Data maintained in class instances**

### Future Features

- Allow player to select the board size and number of ships
- Allow player to position ships themselves
- Have ships larger than 1x1

## Data Model

I decided to use a `BattleshipBoard` class as my model. The game creates two instances of the `BattleshipBoard` class to hold the player's and the computer’s boards.

The `BattleshipBoard` class stores the board size, the number of ships, the position of the ships, the guesses against that board, and details such as the board type (player’s board or computer) and the player’s name.

The class also has methods to help play the game, such as a `display` method to print out the current board, an `already_guessed` method to check if the spot has already been guessed, and a `place_guess` method to add a guess and return the result.

## Testing

I have manually tested this project by doing the following:

- Passed the code through a PEP8 linter and confirmed there are no problems
- Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice
- Tested in my local terminal

## Bugs

### Solved Bugs

- **Index Errors**: Fixed errors due to lists being zero-indexed by adding `size - 1` where necessary.
- **False Positives**: Resolved issues with `validate_coordinates` function by restructuring the `if` statement properly.

### Remaining Bugs

- No bugs remaining

## Validator Testing

- **PEP8**: No errors were returned from PEP8online.com

## Deployment

This project was deployed using a standard terminal.

### Steps for deployment:

1. Fork or clone this repository
2. Create a new terminal project
3. Set the buildbacks to Python
4. Link the terminal to the repository
5. Click on Deploy

## Credits

- [Code Institute](https://codeinstitute.net) for the deployment terminal
- [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)) for the details of the Battleship game
