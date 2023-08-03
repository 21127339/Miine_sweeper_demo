from random import randint

class Cell:
    
    def __init__(self, value, isOpened):
        
        self.value = value
        self.isOpened = isOpened
        self.area = None

def FindAllAdjacentCell(rows, cols, x, y):
    
    adjCells = []
    
    if x > 0:    
        if y > 0: 
            adjCells.append((x - 1, y - 1))
                
        if y < cols - 1:
            adjCells.append((x - 1, y + 1))
                
        adjCells.append((x - 1, y))
    
    if y > 0: 
        adjCells.append((x, y - 1))
            
    if y < cols - 1: 
        adjCells.append((x, y + 1))
    
    if x < rows - 1:     
        if y > 0: 
            adjCells.append((x + 1, y - 1))
        if y < cols - 1: 
            adjCells.append((x + 1, y + 1))
        
        adjCells.append((x + 1, y))
            
    return adjCells


    
    adjCells = []
    
    if x > 1:    
        if y > 1: 
            adjCells.append((x - 2, y - 2))
                
        if y < cols - 2:
            adjCells.append((x - 2, y + 2))
                
        adjCells.append((x - 2, y))
    
    if y > 1: 
        adjCells.append((x, y - 2))
            
    if y < cols - 2: 
        adjCells.append((x, y + 2))
    
    if x < rows - 2:     
        if y > 1: 
            adjCells.append((x + 2, y - 2))
        if y < cols - 2: 
            adjCells.append((x + 2, y + 2))
        
        adjCells.append((x + 2, y))
            
    return adjCells

def PrintMinesField(field, rows, cols):
    
    fo = open("output.txt", "w")
    
    for i in range(rows):
        for j in range(cols):
            
            if field[i][j].value == 0 and field[i][j].isOpened == True:
                print(' ', end = ' ')
                fo.write(str(field[i][j].value) + ' ')
            elif field[i][j].isOpened == True:
                print(field[i][j].value, end = ' ')
                fo.write(str(field[i][j].value) + ' ')
            else:
                print('-', end = ' ')
                fo.write('- ')
                
        print()
        fo.write('\n') 
    fo.close()
        
def PrintOpenedMinesField(field, rows, cols):
    
    for i in range(rows):
        for j in range(cols):
                print(field[i][j].value, end = ' ')
        print()       

def GenerateMinesField(rows, cols):
    
    cells = rows * cols
    amountOfMines = int()
    if cells <= 100:
        amountOfMines = ((cells // 10) * 1.2) // 1
    else:
        amountOfMines = ((cells // 10) * 1.5) // 1
    count = 0
    field = [[Cell(0, False) for _ in range(cols)] for _ in range(rows)]
    mines = []
    
    while (count < amountOfMines):
        
        x = randint(0, rows - 1)
        y = randint(0, cols - 1)
        
        if field[x][y].value == 0:
            field[x][y] = Cell('X', False)
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
                temp =(i , j)
                print(temp)         
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
            print("   vsev",temp, x, y)
        elif field[x_i][y_i].value != 'X' and field[x_i][y_i].isOpened == False:
            field[x_i][y_i].isOpened = True
            count += 1
            print("  e123ev",count, x_i, y_i)

    return count

def Create():

    field, mines = GenerateMinesField(10, 10)   
    PrintOpenedMinesField(field, 10, 10)        
    x, y = FindAZeroCell(field, 10, 10)
    count = OpenACell(field, 10, 10, x, y)
    print('     ',count)
    PrintMinesField(field, 10, 10)
    
    MAX_OPENED_BOOM = 3
    opened_booms = min(count // 15, MAX_OPENED_BOOM)
    
    for _ in range(opened_booms):
        x, y = mines[randint(0, len(mines) - 1)]
        field[x][y].isOpened = True
    
    PrintMinesField(field, 10, 10)
    
Create()