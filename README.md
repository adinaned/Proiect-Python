Game of Mancala in Python. There are no known bugs.
The game depends on the folder images for run time.

Mancala Rules:

OBJECTIVE: Collect the most stones in your mancala (mancalas / stores
are the large cups at each end of the board).
 
Player 1 starts by scooping up all the stones from one of his small cups (players may never start 
from a mancala or from the opponent's six cups). Player 1 drops one stone into the next cup on the right,
one stone into the second cup on the right, continuing around the board (counterclockwise) until he has no
more stones in his hand. If Player 1 reaches his own mancala, he drops a stone into it. Players do not drop
stones into their opponents' mancalas, they skip them and continue dropping stones, one at a time, from 
their hand until they run out of stones. Players take turns moving. At the end of the game, players count 
the stones in their mancalas - the player with the most stones wins.
	If a player drops the last stone into his mancala, he gets to move again. The game ends when one 
player no longer has stones in his cup. The other player (who still has stones on  his side) places 
all remaining stones into his own mancala.
	There is also a computer game of play, in which the computer makes his moves randomly, but 
acoordingly to the game rules. 

Game MODULES:
    mancala_controller.py contains all functions responsible for moving the stones, updating
the score, checking the final state and the mouse click to be done in a valid cup, etc. It also 
manages the 2 game modes: computer and 2 players.
    mancala_initialization.py contains all global variables for images, each element's
position and dimension, and also has the initialization functions, which computes the stones' 
scores' and cups' positions.
    mancala_UI.py contains all functions that load the images from memory and display them on
the board by using the positions given in mancala_controller.py
    main.py starts the game, validates the input option.
