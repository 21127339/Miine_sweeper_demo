from objects import *
from func import *
from random import randint
from queue import PriorityQueue

def GenerateMinesField(rows, cols):
    
    cells = rows * cols
    amountOfMines = int()
    if cells <= 100:
        amountOfMines = ((cells // 10) * 1.5) // 1
    else:
        amountOfMines = ((cells // 10) * 1.8) // 1
    count = 0
    field = [[Cell(0, False, False) for _ in range(cols)] for _ in range(rows)]
    mines = []
    
    while (count < amountOfMines):
        
        x = randint(0, rows - 1)
        y = randint(0, cols - 1)
        
        if field[x][y].value == 0:
            field[x][y] = Cell('X', False, False)
            mines.append((x, y))
            count += 1
              
    for i in mines:
        (x, y) = i
        
        adjCells = FindAllAdjacentCell(rows, cols, x, y)
        for j in adjCells:
            x_i, y_i = j
            if field[x_i][y_i].value != 'X':
                field[x_i][y_i].value += 1
                
    return field, mines

def FindAZeroCell(field, rows, cols):

    temp = 0
    for i in range(rows):
        for j in range(cols):
            
            if field[i][j].value == 0:
                temp = (i , j)
                      
                return temp
              
def OpenACell(field, rows, cols, x, y):

    count = 0 
    if field[x][y].isOpened == True:
        return 0
    field[x][y].isOpened = True
    if field[x][y].value == 'X':
        return 0
        
    adjCells = FindAllAdjacentCell(rows, cols, x, y)
    count += 1
    print(count, x, y)
    for i in adjCells:
        
        x_i, y_i = i
        if field[x_i][y_i].value == 0 and field[x_i][y_i].isOpened == False:
            temp = OpenACell(field, rows, cols, x_i, y_i)
            count += temp
            
        elif field[x_i][y_i].value != 'X' and field[x_i][y_i].isOpened == False:
            field[x_i][y_i].isOpened = True
            count += 1

    return count

def Create():

    field, mines = GenerateMinesField(10, 10)   
    PrintOpenedMinesField(field, 10, 10)        
    x, y = FindAZeroCell(field, 10, 10)
    count = OpenACell(field, 10, 10, x, y)
    
    MAX_OPENED_BOOM = 2
    opened_booms = randint(0, min(count // 10, MAX_OPENED_BOOM))
    
    for _ in range(opened_booms):
        x, y = mines[randint(0, len(mines) - 1)]
        field[x][y].isOpened = True
    
    PrintMinesFieldIntoFile(field, 10, 10)
