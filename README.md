# Battleships Game

The Battleships Game is an online version of the popular board game, Battleships, where two opponents go head to head to try and sink the other's ships. The game is set up so that each opponent can see their ships but cannot see the others. Each player enters a coordinate and the opponent lets them know if they have ‘hit’ a ship, ‘missed’ a ship or if they have already mentioned that coordinate. 

For this online version the user will have the opportunity to play against the computer and select different game board sizes to increase difficulty and the length of the game. The game is targeted at people who enjoy the original board game and would like to practise against the computer.

The live link to this game is below:
#################Battleships Game#########################


![Am I Responsive Mockup](https://github.com/sams4566/rock-paper-scissors-lizard-spock/blob/main/media/am-i-responsive.jpg)

## Features
- __Start Game__

  - The game starts off by asking the user to enter their name and then choose a game board size. 
  - They have the option of choosing three board sizes (either 3x3, 4x4 or 5x5).
  - If the user enters a number that is not 3, 4 or 5 an error message will appear and ask the user to enter a correct value.

![Start Game](https://github.com/sams4566/battleships-game/blob/main/media/start-game.jpg)

- __Game Boards__

  - The user is then presented with two boards. The first board is the users with ships randomly assigned to it and the second board is the computer’s with no ships visible. 
  - A key is also presented to the user so they are aware of what the different symbols mean along with the format of the coordinates.
  - Both boards are clearly labeled and have numbers along the top and left of the board to help the user pick their coordinates.


![Game Boards](https://github.com/sams4566/rock-paper-scissors-lizard-spock/blob/main/media/game-options.jpg)

- __Choosing Coordinates__
  - The user is then prompted to choose a row and then a column to pin-point a dot (`.`) on the computer’s board. 
  - If the user enters a value outside of the numbers on the board the user will receive an error message and will be prompted to enter another coordinate. 
  - The user will also be prompted to enter a new coordinate if they have already entered that coordinate.

![Choosing Coordinates](https://github.com/sams4566/rock-paper-scissors-lizard-spock/blob/main/media/starting-the-game.jpg)

- __Scoring__
  - Once the user has entered a valid coordinate they are presented with both boards again. 
  - The user's board has either a `X` (hit) or a `~` (miss) at the position of the computer's chosen coordinate. This coordinate is also printed out above the board to make it clear for the user the exact position.
  - The computer's board also has either a `X` (hit) or a `~` (miss) at the position of the user’s chosen coordinate. The user’s coordinate is printed above the computer's board.
  - The scores for both users are printed out below the computer's board. After every ‘hit’ the score is increased by 1.
  - The user and computer both continue to pick coordinates until all the ships are ‘hit’.


![Scoring](https://github.com/sams4566/rock-paper-scissors-lizard-spock/blob/main/media/game-area.jpg)

- __End of Game__
  - Once one or both players ‘hit’ all of their opponents ships a message declaring the winner appears at the bottom. 
  - If the game is a draw, the message declares that both players have lost as there are no ships left.
  - The game automatically restarts when the winner/losers has been announced.


![End of Game](https://github.com/sams4566/rock-paper-scissors-lizard-spock/blob/main/media/collecting-points.jpg)

- __Future features__
  - Future features would include playing against a friend on another device and adding in the positions of your own ships. I would also like to add in an option where the user can choose a number of different game board shapes.

## Data Model
  - The below diagram shows how I set out my project before I started coding. This allowed me to work out where to start and what the different parts of the game would be. 
  - I started off the project by getting the name and board size as both of these variables would be filtered through to other functions. 
  - I then created the boards so that I could then work on modifying them.
  - The `run_game` function is the main function where all the other functions return back to. Having the `for` loop in this function allowed the game to continue in a circular motion like the diagram below.

![Data Model](https://github.com/sams4566/rock-paper-scissors-lizard-spock/blob/main/media/collecting-points.jpg)

## Testing
  - I have tested the code thoroughly on Heroku and the terminal on Gitpod and there are no issues or errors.
  - I have added code that prevents the game from crashing if the user inputs a value that cannot be processed.
No errors were returned when passing through PEP8 Online################

### Bugs
#### Solved Bugs 

- I had an issue where a ValueError was crashing the terminal when I inputted the `rows` value as either the `row` or `column` value of the coordinate. Due to the maximum inputtable coordinate value being `rows - 1` (due to the first coordinate starting at ‘0’) I had to change the `correct_input` functions `user_row > rows` to `user_row >= rows` as shown below: 

  ![Bug1](https://github.com/sams4566/rock-paper-scissors-lizard-spock/blob/main/media/bug1.jpg)

- I had an `or` between SCORE1 and SCORE2 which meant that instead of the winner being announced the draw statement was announced. I changed the `or` to an `and` which resolved the issue as shown below:

  ![Bug2](https://github.com/sams4566/rock-paper-scissors-lizard-spock/blob/main/media/bug2.jpg)

#### Unfixed Bugs
- No unfixed bugs

## Deployment
This project was deployed using Code Institute’s mock terminal for Heroku. Below are the steps for deployment:
  - Fork or clone this repository 
  - Go onto Heroku and click ‘Create new app’
  - You then need to add two buildpacks from the Settings tab. The ordering is as follows:
    1. `heroku/python`
    2. `heroku/nodejs`
  - You must then create a _Config Var_ called `PORT`. Set this to `8000`
  - After link the Heroku app to this repository on GitHub
  - Click on ‘Deploy’

## Credits
  - The code for learning how to print a loop horizontally was from - https://dev.to/theoretician/how-to-write-for-loops-horizontally-3h70 
  - For learning how to combine two for loops together in a zip I used the following website - https://realpython.com/python-zip-function/ 