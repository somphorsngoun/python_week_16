#   @param grid   (an array 2D)
#   @param rowIndex  (integer)
#   @param sign  (string)
#   @return True if the ROW at the given rowIndex is composed ONLY of the given sign
def signOnRow(grid, rowIndex, sign):
    number = 0
    for row in range(len(grid[rowIndex])):
        if grid[rowIndex][row] == sign:
            number +=1
    if number == 3:
        return True     # TO CHANGE !!

#   @param grid   (an array 2D)
#   @param columnIndex  (integer)
#   @param sign  (string)
#   @return True if the ROW at the given columnIndex is composed ONLY of the given sign
def signOnColumn(grid, columnIndex, sign):
    # TODO !!
    number = 0
    for column in range(len(grid[columnIndex])):
        if grid[column][columnIndex] == sign:
            number +=1
    if number == 3:
        return True

#   @param grid   (an array 2D)
#   @param sign  (string)
#   @return True if a DIAGONAL is composed ONLY of the given sign
def signOnDiagonal(grid, sign):
     # TODO !!   
    if grid[1][1] == sign:
        return True

#   @param grid   (an array 2D)
#   @param sign  (string)
#   @return True if the given sign has WON
def hasSignWon(grid, sign):
    # TODO ! 
    #  It true if : 
    #  - one of the 2 diagonal is composed of this sign
    #  - or if 1 of the 3 rows is composed of this sign
    #  - or if 1 of the 3 columns is composed of this
    if signOnDiagonal(grid, sign):
        if grid[0][0] == grid[2][2] or grid[2][0] == grid[0][2]:
            return True
    else:
            
        for r in range(len(grid)):
            if signOnColumn(grid,r, sign):
                return True
            
            for c in range(len(grid)):
                if signOnColumn(grid,c, sign):
                    return True
            return False
    
# MAIN PROGRAM (nothing to change here !)
grid = eval(input())
if hasSignWon(grid, "A"):
    print("A WON")

elif hasSignWon(grid, "B"):
    print("B WON")

else:
    print("NO WINNER")
