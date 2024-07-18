
# Battleship Game
Welcome to the Battleship Game, a terminal-based implementation of the classic board game where you try to sink the opponent's ship.
This is a Python terminal game, which runs on Heroku.

The Battleship Game is a Python terminal application where players take turns guessing the location of the opponent's hidden ship on a 5x5 grid. The game supports up to 1 player as you play against the computer and includes features such as input validation and turn-based gameplay.

Here is a live version:https://p3-battleships.herokuapp.com/
![Screenshot 2024-07-18 17 32 33](https://github.com/user-attachments/assets/00b6ff21-7d86-4294-9cd6-583377c3f34e)

 ## How to Play
Each player takes turns guessing the location of the hidden ship by entering the row and column numbers.
The game will display the board with updates after each guess.
The game ends when a player sinks the ship or when all guesses are exhausted.

## Rules
- Each player has a 5x5 grid where they can place their ships.
- The objective is to guess the location of the opponent's ship and sink it before they sink yours.
- Players take turns guessing the coordinates of the opponent's ships.
- The game ends when one player successfully sinks the other's ship, or all guesses are exhausted.


## Features
Player Input: Allows players to enter guesses for row and column positions.
Random Ship Placement: The ship's location is randomly placed on the board at the start of each game.

![Screenshot 2024-07-18 17 59 32](https://github.com/user-attachments/assets/baa37de6-d609-4a00-9301-3da659be9994)

Input Validation: Ensures that player inputs are valid numbers within the grid range and not previously guessed locations.
Game Status Display: Displays the current state of the board after each guess.
Win/Lose Conditions: The game ends when a player successfully sinks the ship or runs out of guesses.

### Symbols Used
- **O**: Hidden space on the board.
- **S**: Ship location.
- **X**: Guessed location.
- 
![Screenshot 2024-07-18 18 08 17](https://github.com/user-attachments/assets/26a875b8-dff9-4334-a168-012082ae2713)



## Implementation Details
- **user_input**: Function to handle user input and ensure it is within the valid range.
- **player_guesses**: Function to obtain valid guess coordinates from the player.
- **computer_guesses**: Function to generate valid guess coordinates for the computer opponent.
- **BattleshipBoard Class**: Manages the game board including ship placement, checking guesses, and displaying the board.
- **turn Function**: Executes a single turn of the game, either for the player or the computer.
- **play_game Function**: Main game loop that manages turns between the player and the computer, tracks guesses, and determines the game outcome.
- **main Function**: Entry point of the program that initializes the game setup and controls the flow of the game.

# Data Model
BattleshipBoard Class: This class represents the game board. It encapsulates the state of the board (grid), including the placement of ships and the status of each cell (hidden, ship, guessed). Methods within this class handle operations such as checking if a coordinate contains a ship (is_ship), marking a guessed position (place_guess), checking if a position has already been guessed (already_guessed), and displaying the board (display).

## Technologies Used
Python: The main programming language used for the game logic.
Heroku: Deployment platform for hosting the game.
Setup and Installation
Prerequisites
Python 3.9 or later
Git
Installation Steps
Clone the repository to your local machine:

## Configuration
- **GUESSES**: Total number of guesses allowed per player.
- **BOARD_SIZE_X** and **BOARD_SIZE_Y**: Dimensions of the game board (5x5 in this case).

## Testing
Manual Testing
Input Validation: Tested by entering various types of invalid inputs (e.g., non-numeric, out of range, duplicate guesses) to ensure proper handling and error messages.
Game Flow: Played multiple rounds to verify the game progresses correctly, displays the board accurately, and ends under the right conditions.
Automated Testing
The code has been passed through the PEP8 online checker to ensure it follows Python's style guidelines.

## Known Issues
None identified at this time.

## How to Run
1. Clone the repository.
2. Navigate to the directory containing `battleship.py`.
3. Run `python battleship.py` to start the game.
4. Follow the on-screen instructions to play Battleship.

Have fun playing Battleship!

## Deployment
The project is deployed on Heroku. Follow these steps to deploy your own version:

Create a new Heroku app and set the buildpacks:
heroku/python
heroku/nodejs
Set the PORT environment variable to 8000.
Push the code to Heroku:
Copy code
git push heroku main
The game will be available at your Heroku app's URL.

## Credits
Developed by Noel Duggan as part of the Code Institute's Python Essentials project.
Inspired by the classic board game Battleship.













