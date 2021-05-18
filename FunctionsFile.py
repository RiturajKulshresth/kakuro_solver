text_box1=None

class  Game_Constraint:
    def __init__(self, constraint, variables):

        """ 
        For this project we have assumed that in a game of Kakuro all the numbers written initially on the
        left and top of a row or column respectively are the constraints.

        In this class we define the contraint with two variables:

        1. constraint: Is the number which all the inputs must be equal to when summed together and is initially
            provided.
        2. variables: List of all the variables that must be accounted for the sum of a constraint.
        """
        
        self.variables = variables
        # print ((self.variables))
        self.constraint = constraint
        
        

def backtrack(kakuro):

    """ 
    This function is the backbone of the project and its purpose is to use the backtracking algorithm and find
    the solution to the Kakuro puzzle if possible.

    """

    """
    First we check if the puzzle is solved so that when we perform recursion on the backtracking algorithm 
    the initial command is to check if its solved and save computation

    """
    if Is_Solved(kakuro):
        return kakuro
    
    """
    The below code has been inspired by a number of approaches made to solving a sudoku 
    where firstr we check for all the unsolved positions 
    then we put a possible value at the position and again perform backtracking algorithm on it
    if a correct  solution is returned we let it be the answer otherwise other possible solutions are checked

    """
    for i in range(kakuro.size):
        if kakuro.grid[i] == -1: 
            for n in range(1,10):
                if(Is_Solvable(kakuro)):
                    kakuro.grid[i] = n
                    temp_kakuro = backtrack(kakuro)

                    # if(Is_Solved(kakuro)):
                    #     return kakuro

                    if(temp_kakuro != None):
                        return temp_kakuro
                    else:
                        kakuro.grid[i] = -1

            return None

def Is_Solvable(kakuro):
        for l in kakuro.Constraints:
            if(Check_Constraint(kakuro,l) !=True):
                return False

        return True



def Is_Solved(kakuro):

    """
    This function checks for all constraints present in a game to finally check if the game is solved
    or not
    For this it checks if there is an unsolved position in the game 
    and checks if the sum of the variables values that are set are equal to the constraint given
    """


    for l in kakuro.Constraints:
        for f in l.variables:
            if kakuro.grid[f] == -1:
                return False
    for l in kakuro.Constraints:
        cat=0;
        for f in l.variables:
            cat+=kakuro.grid[f]
        if cat != l.constraint:
            return False

    return True



def Add_Constraint(kakuro,Constr):
    kakuro.Constraints.append(Constr)

def Add_Blanks(kakuro,fieldList):
    for field in fieldList:
        kakuro.grid[field] = -2

def display(kakuro):

    templist=kakuro.grid[:]
    # print (templist)
  
    for i in range(len(templist)):
        if (templist[i-1] == -2):
            templist[i-1]='.'
        if (templist[i-1] == -1):
            templist[i-1]='_'
    
    for i in range(kakuro.rows):
        for j in range(kakuro.columns):
                print (templist[kakuro.columns*i+j],end=' ')
        print ()

def display2(kakuro):

    templist=kakuro.grid[:]
    # print (templist)
  
    for i in range(len(templist)):
        if (templist[i-1] == -2):
            templist[i-1]='.'
        if (templist[i-1] == -1):
            templist[i-1]='_'
    
    for i in range(kakuro.rows):
        for j in range(kakuro.columns):
                print (templist[kakuro.columns*i+j],end=' ')
        print ()
        print ("templist  ",templist)
    print ("rando   ")

def Check_Constraint(kakuro,Constr):

    """ 
    Note that we do not check for completeness of a consttraint here
    that is checked in the Is_Solved() function
    """
    """
    For all the variables of the constraint if they have been altered and changed, below lines will check 
    this and add them to the list of values for the constraint 
    this helps to check a constraints correctness after values are added

    """

    values=[]
    for f in Constr.variables:
        if (kakuro.grid[f] > 0):
            values.append(kakuro.grid[f])
    """
    first we check if the constraint given has been exceeeded by the values stored

    """

    if Constr.constraint<sum(values):
        return False

    """
    Then we check if the numbers have been repeated ever in the values

    """

    """
    CAN CHANGE THIS
    
    """
    if len(set(values)) != len(values):
        return False
    
    """
    Then we check if the sum of all the values set is not equal to the constraint given even when the 
    number of valus is equal 
    
    """
    if len(values) == len(Constr.variables):
        if sum(values) != Constr.constraint:
            return False
   
    return True

def guidisplay2(kakuro):

    templist=kakuro.grid[:]
    s1= ""
    # print (templist)
  
    for i in range(len(templist)):
        if (templist[i-1] == -2):
            templist[i-1]='.'
        if (templist[i-1] == -1):
            templist[i-1]='_'
    
    for i in range(kakuro.rows):
        for j in range(kakuro.columns):
                s1+= str(templist[kakuro.columns*i+j]) + " "
        s1+=str("\n")
    print ("templist  ",templist)
    print ("rando   ",s1)
    return s1


def guidisplay(kakuro):

    templist=kakuro.grid[:]
    s1= ""
    # print (templist)
  
    for i in range(len(templist)):
        if (templist[i-1] == -2):
            templist[i-1]='.'
        if (templist[i-1] == -1):
            templist[i-1]='_'
    
    for i in range(kakuro.rows):
        for j in range(kakuro.columns):
                s1+= str(templist[kakuro.columns*i+j]) + " "
        s1+=str("\n")
    # print ("templist  ",templist)
    # print ("rando   ",s1)
    return s1

def runtimer(kakuro):
    display(kakuro)
    if not Is_Solvable(kakuro):
        print ("Not Solvable")
    puzzle1=backtrack(kakuro)
    if Is_Solved(puzzle1):
        print ("\nPuzzle Solved\n")
        display(puzzle1)
    else:
        print ("Couldnt solve the puzzle")



def guiruntimer(kakuro):
    text_box1.delete(1.0, "end-1c")
    text_box1.insert("end-1c", str(guidisplay(kakuro))+"\n")

    print (guidisplay(kakuro))
    if not Is_Solvable(kakuro):
        print ("Not Solvable")
        text_box1.insert("end-1c", "Not Solvable"+"\n")
    puzzle1=backtrack(kakuro)
    if Is_Solved(puzzle1):
        print ("\nPuzzle Solved\n")
        text_box1.insert("end-1c", "Puzzle Solved\n"+"\n")
        text_box1.insert("end-1c", str(guidisplay(kakuro))+"\n")
        display(puzzle1)
    else:
        text_box1.insert("end-1c", "Couldn't solve the puzzle"+"\n")
        print ("Couldn't solve the puzzle")