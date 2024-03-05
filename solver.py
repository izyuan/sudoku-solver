import random
import time
#essentially my goal here to generate a solvable sudoku and then put in random zeros 

#intitializing the grid
sudokugrid = [[0 for i in range(9)] for j in range(9)]


def valid_location(sudokugrid, row, col, number):
    """
    Function to detemrine whether the sudoku grid is valid 
    Args:
        sudokugrid (_type_): sudoku grid
        row (_type_): row
        col (_type_): column 
        number (_type_): number of sudoku 

    Returns:
        Boolean: True means that it is a valid sudoku, false means its not
    """
    for i in range(9):
        if sudokugrid[row][i] == number or sudokugrid[i][col] == number: #determining whether there are multiple of the same in a row / column
            return False
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    #checking to see if there are any repeats in the 3 by three columns
    for i in range(3):
        for j in range(3):
            if sudokugrid[i + startRow][j + startCol] == number:
                return False
    return True


def find_empty_square(sudokugrid):
    """This function checks to see if there are any empty cells

    Args:
        sudokugrid (array): the Sudoku Grid

    Returns:
        int: returns the indices of the empty cells, if there are none it returns none
    """
    for i in range(9):
        for j in range(9):
            if sudokugrid[i][j] == 0:
                return i, j
    return None


def generate_solution(sudokugrid):
    """This function attempts to generate a complete solution for the Sudoku puzzle by using backtracking

    Args:
        sudokugrid (_type_): Sudoku Grid

    Returns:
        Boolean: True if a solution is found, False if its not found 
    """
    find = find_empty_square(sudokugrid)
    if not find:
        return True  
    else:
        row, col = find
        
    number_list = [n for n in range(1, 10)]
    random.shuffle(number_list)  
    for number in number_list:
        if valid_location(sudokugrid, row, col, number):
            sudokugrid[row][col] = number
            if generate_solution(sudokugrid):
                return True
            sudokugrid[row][col] = 0  

    return False  


def insert_zeros(sudokugrid, zeros_count): #function to insert 0s you can change the number of zeros in the next if statement
    """function to insert 0s at random 

    Args:
        sudokugrid (_type_): Sudoku Grid
        zeros_count (_type_): The amount of zeros you want. 64 is the maximum amt of zeros possible to still be solvable I think 
    """
    count = 0 
    
    try:
        zeros_count = int(input("How many empty cells would you like? Maximum of 64 (hardest)\n"))
    except:
        print("error, did not enter int, giving you maximum difficulty")
        time.sleep(4)
        
    if zeros_count > 64: 
        zeros_count = 64
        print("zeros count cannot exceed 64")
    while count < zeros_count:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if sudokugrid[row][col] != 0: 
            sudokugrid[row][col] = 0
            count += 1  
    
        
if generate_solution(sudokugrid):
    insert_zeros(sudokugrid, 80) #change the second int value to whatever\
    print("random sudoku board, try to solve it!: ")
    for row in sudokugrid:
        print(row)  
else:
    print("No solution exists.")
    
    
def solve_sudoku (sudokugrid):
    find = find_empty_square(sudokugrid)
    if not find: 
        return True
    else:
        row, col = find
        
    for number in range (1,10):
        if valid_location (sudokugrid, row, col, number):
            sudokugrid[row][col] = number 
            if solve_sudoku(sudokugrid):
                return True
            sudokugrid[row][col] = 0 
            
    return False

keyword = input('Type "solve" if you want the solution \n')
while keyword.lower() != "solve":
    keyword = input('Type "solve" if you want the solution \n')

if solve_sudoku(sudokugrid) and keyword.lower() == "solve":
    print("Sudoku puzzle solved")
    for row in sudokugrid:
        print(row)
else:
    print("No solution found for the puzzle.")