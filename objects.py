class Cell:
    
    def __init__(self, value, isOpened, isSafe):
        
        self.value = value
        self.isOpened = isOpened
        self.isSafe = isSafe
        self.neighbor = None

class Clue:
    
    def __init__(self, cells, numberOfCells, unexploredBomb):
        
        self.cells = cells
        self.numberOfCells = numberOfCells
        self.unexploredBomb = unexploredBomb
    
    def __lt__(self, nxt):
        
        if self.unexploredBomb == nxt.unexploredBomb:
            return self.numberOfCells < nxt.numberOfCells
        return self.unexploredBomb < nxt.unexploredBomb
        
    def IsDifferentClue(self, cells, unexploredBomb):
    
        n = len(cells)
        
        if n != len(self.cells):
            return True
        
        else:
            for i in cells:
                if i not in self.cells:
                    return True
                        
        return False    
        

class MineField:
    
    def __init__(self, field, rows, cols):
        
        self.field = field
        self.rows = rows
        self.cols = cols
        self.areas = set()
        self.hintCells = self.FindHintCells()
    
    def FindHintCells(self):
        
        temp = set()
        
        for i in range(self.rows):
            for j in range(self.cols):
                
                if self.field[i][j].isOpened == True and self.field[i][j].value != 0 :
                    temp.add((i, j))
                    
        return temp
    
    def FindAllAdjacentCell(self, pos):
    
        x, y = pos
        adjCells = []
        
        for i in {-1, 0, 1}:
            for j in {-1, 0, 1}:
                
                if not (i == 0 and j == 0) and x + i >= 0 and x + i < self.rows and y + j >= 0 and y + j < self.cols:
                    adjCells.append((x + i, y + j))
                
        return adjCells
    
    def FindAllAdjacentCellsInArea(self, pos, area):
        
        if pos in area:
            return
        area.append(pos)
        adjCells = self.FindAllAdjacentCell(pos)
        
        for i in adjCells:
            
            x_i, y_i = i
            if self.field[x_i][y_i].isSafe == True and self.field[x_i][y_i].value != 0:
                newAdjCells = self.FindAllAdjacentCell(i)
                
                for j in newAdjCells:
                    
                    x_j, y_j = j
                    if j != pos and j in adjCells and self.field[x_j][y_j].isSafe != True:
                        print(pos, 'open', i)
                        self.FindAllAdjacentCellsInArea(i, area)
        
    def SeperateField(self):
        
        areas = []
        exploredCells = []
        
        for i in self.hintCells:
            
            if i not in exploredCells:
                
                temp = []
                self.FindAllAdjacentCellsInArea(i, temp) 
                areas.append(temp)
                for j in temp:
                    exploredCells.append(j)
                    
        return areas
    
