from objects import *
from func import *
from init import *
from method1 import *

def ReadData(fileName):
    
    fi = open(fileName, "r")
    rows = 0
    cols = 0
    field = []
    temp = fi.readline()
    
    while(temp):
        
        rows += 1
        tempArray = []
        
        for i in temp:
            if i != ' ' and i != '\n':
                
                if i == 'X':
                    newCell = Cell(i, False, False)
                elif i == '-':
                    newCell = Cell(None, False, None)
                else:
                    newCell = Cell(int(i), True, True)
                
                cols += 1      
                tempArray.append(newCell)

        field.append(tempArray)
        temp = fi.readline()
    cols = cols // rows
    PrintUnopenedMinesField(field, rows, cols)
    return MineField(field, rows, cols)

def SolveEachArea(clues, cellsAsVariable):
    
    numberOfClues = len(clues)
    numberOfCells = len(cellsAsVariable)
    matrix = [[0 for _ in range(numberOfCells)] for _ in range(numberOfClues)]
    
    for i in range(numberOfClues):
        
        print("Check matrix", i)
        for j in clues[i].cells:
            index = cellsAsVariable[j]
            matrix[i][index] = 1
            print(index, j)
        
        
        matrix[i].append(clues[i].unexploredBomb) 
    PrintMatrix(matrix)
    print()
    PrintMatrix(Gauss_elimination(matrix))
    print()
    Conclusion(Gauss_elimination(matrix), cellsAsVariable)
    
def Solve(mineField):
        
    areas = mineField.SeperateField()
    
    for eachArea in areas:
        
        clues = []
        count = -1
        cellsAsVariable = dict()
        
        for i in eachArea:                
            
            x_i, y_i = i
            unexploredBomb = mineField.field[x_i][y_i].value
            adjCells = mineField.FindAllAdjacentCell(i)
            temp = set()
            
            for j in adjCells:
                
                x_j, y_j = j
                
                if mineField.field[x_j][y_j].isSafe == None:
                    temp.add(j)
                    if j not in cellsAsVariable:
                        count += 1
                        cellsAsVariable.update({j : count})
                        
                elif mineField.field[x_j][y_j].isSafe == False:
                    unexploredBomb -= 1
            
            if len(clues) == 0:
                print("Clue: ", temp, unexploredBomb)   
                clues.append(Clue(temp, len(temp), unexploredBomb))
            else:
                flag = True
                
                for j in clues:
                    if len(temp) == 0 and unexploredBomb == 0:
                        flag = False
                    else:
                        flag = j.IsDifferentClue(temp, unexploredBomb)
                    
                if flag:
                    print("Clue: ", temp, unexploredBomb)        
                    clues.append(Clue(temp, len(temp), unexploredBomb))
        #clues = PriorityQueue(clues)
        print()
        print(cellsAsVariable)     
        SolveEachArea(clues, cellsAsVariable)
   
mineField = ReadData("input.txt")
Solve(mineField)
