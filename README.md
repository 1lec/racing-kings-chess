# Racing Kings
Racing Kings is a Python implementation of the racing kings chess variant, a twist on the typical chess ruleset. This
implementation follows the same ruleset as [lichess](https://lichess.org/variant/racingKings), but uses a different
[starting position](starting_position.png).

## Installation
To install and run Racing Kings, follow these steps:
1. Download [racing_kings.py](racing_kings.py).
2. This program was written in Python 3, which you will need to run the program. You can download the latest version
[here](https://www.python.org/downloads/).
3. To run the program, open your command prompt and navigate to the folder where you saved racing_kings.py. Once in the
correct folder, type `python3 racing_kings.py`.

## How To Play
Racing Kings is simple to play. Follow these steps:
1. Launch the game by running `python3 racing_kings.py` in your terminal.
2. The [starting position](starting_position.png) will be printed in your terminal, and you will be prompted for white's
first move.
*Note: If the Unicode pieces are not displaying, you may need to change your terminal font. Alternatively, you can run
the program with an IDE or your choice.*
3. To make a move, first enter the start square of the piece you'd like to move. For example, `a2`.
4. Next, enter the end square to complete your move. For example, `a3`. Your do not need to specify which piece to move.
5. Once the game is over, you will be asked if you'd like to play again.

## Future Improvements
1. Supporting standard algebraic notation. Instead of entering the start and end squares of a move, make the move in a
single command, using both the piece name and end square. For example, instead of `g1` and `f3`, use the simpler `Nf3`.
2. Create an intuitive, visually-appealing graphical user interface.
