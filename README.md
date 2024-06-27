# text-based-sudoku
Sudoku game in python terminal.<br>
<br>
Usage:<br>
The user is prompted for the directory for the board file.<br>
Then, the user is prompted for their move.<br>
User's move can either be:<br>
Help: Input "H" or "h"<br>
Quit: Input "Q" or "q"<br>
Updating board: Input {row} {column} {value} without the brackets.<br>
Clearing position: Input {row} {column} {"C"} without the brackets.<br>
Until the game has been won, the user will be prompted repeatedly for their move.<br>

Example:
```
Please insert the name of a board file: boards/board_one.txt
685|13 | 47 0
7  |   | 1  1
 1 |764| 5  2
-----------
9  | 7 |5 4 3
8 1|  9| 72 4
4 3|  6|    5
-----------
   |427|39  6
 4 |9  | 68 7
1 7|   |4   8

012 345 678
Please input your move: H
Need help?
H = Help
Q = Quit
Hint: Make sure each row, column, and square contains only one of each number from 1 to 9.

685|13 | 47 0
7  |   | 1  1
 1 |764| 5  2
-----------
9  | 7 |5 4 3
8 1|  9| 72 4
4 3|  6|    5
-----------
   |427|39  6
 4 |9  | 68 7
1 7|   |4   8

012 345 678
Please input your move: 0 5 8
685|138| 47 0
7  |   | 1  1
 1 |764| 5  2
-----------
9  | 7 |5 4 3
8 1|  9| 72 4
4 3|  6|    5
-----------
   |427|39  6
 4 |9  | 68 7
1 7|   |4   8

012 345 678
Please input your move:
```
