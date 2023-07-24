## Project description
The is problem 14 from the final projects list for summer 2023. Here is the description of the game:

*There are two players, A and B. At the beginning of the game, each starts with 4 coins, and there are 2 coins in the pot. A goes first, then B, then A, and so on. During a particular player’s turn, the player tosses a 6-sided die. If the player rolls a:
1, then the player does nothing.
2: then the player takes all coins in the pot.
3: then the player takes half of the coins in the pot (rounded down).
4,5,6: then the player puts a coin in the pot.*

*A player loses (and the game is over) if they are unable to perform the task (i.e., if they have 0 coins and need to place one in the pot). We define a cycle as A and then B completing their turns. The exception is if a player goes out; that is the final cycle (but it still counts as the last cycle). We are trying to determine the expected number (and maybe even the distribution) of cycles the game will last for. I’m guessing that you can use “first-step” analysis to get the expected value. Simulation seems the easiest thing to do to get the entire distribution.*


The game is stored in `game.py` and "first-step" analysis is provided in the notebook `analysis.ipynb`.

## Code 
1. game.py - game definition for Monte Carlo simulation
2. markov_chain_game.py - Markov chain implementain to get to steady state probabilities.
3. analysis.upynb - run the Monte Carlo and Markov chain implementations
4. analysis_distro_fitting.ipynb - Jupyter notebook to fit a distribution to the Monte Carl runs.