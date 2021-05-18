from FunctionsFile import *

class kakuro:
    def __init__(self, rows,columns):
        self.rows=rows
        self.columns=columns
        self.size= rows*columns
        self.grid=[]
        i=0
        while(i < self.size):
            self.grid.append(-1)
            i+=1
        # print (self.grid)
        self.Constraints=list()


"""
In order to load a puzzle add the copied code from 'Puzzles' or your personal puzzle below this paragraph

Remove all the code previously present between this paragraph and the next one

"""
# rows=6
# columns=6
# kakuro = kakuro(rows,columns)

# Add_Constraint(kakuro,Game_Constraint(8,(0,1)))
# Add_Constraint(kakuro,Game_Constraint(17,(6,7,8)))
# Add_Constraint(kakuro,Game_Constraint(11,(14,15,16)))
# Add_Constraint(kakuro,Game_Constraint(23,(19,20,21,22)))
# Add_Constraint(kakuro,Game_Constraint(9,(24,25,26)))
# Add_Constraint(kakuro,Game_Constraint(14,(30,31)))
# Add_Constraint(kakuro,Game_Constraint(8,(4,5)))
# Add_Constraint(kakuro,Game_Constraint(7,(10,11)))
# Add_Constraint(kakuro,Game_Constraint(16,(28,29)))
# Add_Constraint(kakuro,Game_Constraint(8,(34,35)))

# Add_Constraint(kakuro,Game_Constraint(11,(0,6)))
# Add_Constraint(kakuro,Game_Constraint(13,(1,7)))
# Add_Constraint(kakuro,Game_Constraint(26,(4,10,16,22,28,34)))
# Add_Constraint(kakuro,Game_Constraint(10,(5,11)))
# Add_Constraint(kakuro,Game_Constraint(11,(8,14,20,26)))
# Add_Constraint(kakuro,Game_Constraint(14,(15,21)))
# Add_Constraint(kakuro,Game_Constraint(15,(19,25,31)))
# Add_Constraint(kakuro,Game_Constraint(12,(24,30)))
# Add_Constraint(kakuro,Game_Constraint(9,(29,35)))

# Add_Blanks(kakuro,[2,3,9,12,13,17,18,23,27,32,33])

# rows=3
# columns=4
# kakuro=kakuro(rows,columns)

# Add_Constraint(kakuro,Game_Constraint(3,(2,3)))
# Add_Constraint(kakuro,Game_Constraint(10,(4,5,6,7)))
# Add_Constraint(kakuro,Game_Constraint(3,(8,9)))

# Add_Constraint(kakuro,Game_Constraint(4,(4,8)))
# Add_Constraint(kakuro,Game_Constraint(3,(5,9)))
# Add_Constraint(kakuro,Game_Constraint(6,(2,6)))
# Add_Constraint(kakuro,Game_Constraint(3,(3,7)))

# Add_Blanks(kakuro,[0,1,10,11])


"""
Remove all the code above this paragraph upto the just above paragraph

"""
# print ("cat"+str(guidisplay(kakuro)))

"""
Do not tamper with the below code

if you are not using the GUI then uncomment below lines
"""

# display(kakuro)
# if not Is_Solvable(kakuro):
#     print ("Not Solvable")
# puzzle1=backtrack(kakuro)
# if Is_Solved(puzzle1):
#     print ("\nPuzzle Solved\n")
#     display(puzzle1)
# else:
#     print ("Couldnt solve the puzzle")
