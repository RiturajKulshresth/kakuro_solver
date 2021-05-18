"""
In order to load any of the puzzles in the kakuro solver copy the code after each 
puzzle marker in puzzles.txt and place it in the kakuro solver at the marked position

"""


"""
You can also create your personal Puzzle 

All instruction to create a puzzle can be found below 

"""




In order to create a puzzle you must trim the top row and the left column 
which do not contain any empty block. 
Then mark all the remaining blocks numerically starting from 0 from the top left of the puzzle

Now write the number of rows and columns
Then add the constraints which are the numbers given to us previously in the puzzle and 
the associated empty blocks both row wise and column wise 
for all the constraints 

Then add the list of all blocks positions that are blanks 

For further explaination check the pictures of puzzles given in the folder 'Puzzles'
and check the associated information in ouzzles.txt under puzzle 2

"""

rows=
columns=
kakuro = kakuro(rows,columns)

Add_Constraint(kakuro,Game_Constraint(Sum,(position of all the blocks,position2)))
Add_Constraint(kakuro,Game_Constraint(Sum,(position of all the blocks,position2)))
.
.
.

Add_Blanks(kakuro,[a,b,..,v])
