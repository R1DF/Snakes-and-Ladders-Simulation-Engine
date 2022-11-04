# Snakes and Ladders Simulation Engine (SLSE)
Snakes and Ladders Simulation Engine is a program that allows people to simulate Snakes and Ladders in the terminal with the usage of a .JSON file that contains the needed data for a game. It uses the command line and simulates the game by asking every player their commands on what they want to do.

# What is Snakes and Ladders?
_Snakes and Ladders_ is a well-known board game for multiple players where every player starts on a grid and has to repeatedly take turns rolling dice and moving, getting close to the final spot which declares victory. Some spots can have **ladders**, which will send the player up to a certain square. Other spots may have **snakes**, which can send players down. The game is purely dependent on luck. More information can be found in [this](https://en.wikipedia.org/wiki/Snakes_and_ladders) Wikipedia article.

# What does SLSE change?
In SLSE, the core mechanics remain completely, but have a few additions. First, players need to answer a question correctly when they reach a snake to move up. There's also **redemption points** scattered across the map, which can be collected by answering other questions correctly. When a player reaches a snake, they can use a redemption point to not down. Redemption points are stackable, but there is a limit.<br>
The questions themselves are all stored in the .JSON file that contains the game.

# Commands
* **HELP** - Gives out the list of commands in the game.
* **CLEAR** - Clears the command line.
* **LOCATIONS**/**MAP**/**WHERE** - Shows you the map with labelled ladders, snakes, and redemption points. Multiple colours are used for snakes and ladders to represent the locations they send you to more clearly.
* **PLAYERS** - Shows you the map and labels the locations which have players. It also shows you at which location is every player at for more conciseness.
* **ROLL**/**MOVE** - Rolls the die and moves the player, ending their turn.
* **STATUS**/**DISTANCE** - Shows the player's location and distance from the finishing point.
* **INSPECT SNAKE**, **INSPECT LADDER** - Lets the user find more information about a certain snake/ladder by its number on the map, specifically its destination.
* **SURRENDER** - Removes the player from the game as they give up.

# Download
The latest version is **v1.0.0**.<br>
As of now, SLSE is only available to Windows users. Please check out the Releases section of the repository to find its latest release.<br>
The game, however, can also be played on Mac and Linux (albeit I haven't tested) by downloading its source code and running the game with Python 3.10 or later. To do this, you will need to install the following libraries:
* questionary
* toml
* requests
* colorama

Feel free to edit the program or take a look at its code.

