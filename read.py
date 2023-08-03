from init import *

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
                    newCell = Cell(i, True)
                elif i == '-':
                    newCell = Cell(None, False)
                else:
                    newCell = Cell(i, True)
                
                cols += 1      
                tempArray.append(newCell)

        field.append(tempArray)
        temp = fi.readline()
    cols = cols // rows
    PrintMinesField(field, rows, cols)
    return field, rows, cols
    
def FindAllAvailableClues(field, rows, cols):
        
        for i in range(rows):
            for j in range(cols):
                
                if field[i][j].value != 'X' and field[i][j].value != 0 and field[i][j].value != None:
                    a = 0    
   
    
ReadData("output.txt")