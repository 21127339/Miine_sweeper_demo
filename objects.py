class InitCell:
#Class de bieu dien cho 1 o trong ma tran khoi tao    
    def __init__(self, value, isOpened):
        
        self.value = value
        self.isOpened = isOpened

class Cell:
#Class de bieu dien 1 o trong ma tran    
    def __init__(self, value, isSafe):
        
        self.value = value
        self.isSafe = isSafe
        self.neighbor = None

class Clue:
#Class de bieu dien du kien ve ma tran cua 1 o
#Gom cac o xung quanh cua 1 o va so luong bom quanh no    
    def __init__(self, cells, numberOfCells, unexploredBomb):
        
        self.cells = cells
        self.numberOfCells = numberOfCells
        self.unexploredBomb = unexploredBomb
    
    def __lt__(self, nxt):
        
        if self.unexploredBomb == nxt.unexploredBomb:
            return self.numberOfCells < nxt.numberOfCells
        return self.unexploredBomb < nxt.unexploredBomb
        
    def IsDifferentClue(self, cells, unexploredBomb):
    #Ham kiem tra 2 du kien co khac nhau hay khong
        n = len(cells)
        
        if n != len(self.cells):
        #Neu so luong o cua 2 du kien khac nhau thi chung khac nhau
            return True
        
        else:
        #Neu so luong o cua 2 du kien giong nhau nhung co 1 o khong nam trong du kien con lai thi chung khac nhau
            for i in cells:
                if i not in self.cells:
                    return True
                        
        return False    
        

class MineField:
#Class bieu dien ma tran    
    def __init__(self, field, rows, cols):
        
        self.field = field
        self.rows = rows
        self.cols = cols
        self.areas = set()
        self.hintCells = self.FindHintCells()
    
    def FindHintCells(self):
    #Ham tim tat ca cac o la o an toan va co du kien    
        temp = set()
        
        for i in range(self.rows):
            for j in range(self.cols):
            #Tim tat ca cac o du kien (cac o an toan va khac 0)    
                if self.field[i][j].isSafe == True and self.field[i][j].value != 0 :
                    temp.add((i, j))
                    
        return temp
    
    def FindAllAdjacentCell(self, pos):
    #Ham tim tat ca cac o xung quanh cua 1 o
        x, y = pos
        adjCells = []
        
        for i in {-1, 0, 1}:
            for j in {-1, 0, 1}:
                
                if not (i == 0 and j == 0) and x + i >= 0 and x + i < self.rows and y + j >= 0 and y + j < self.cols:
                    adjCells.append((x + i, y + j))
                
        return adjCells
    
    def FindAllAdjacentCellsInArea(self, pos, area):
    #Ham tim tat ca cac o xung quanh cua 1 o ma cung 1 khu vuc voi no    
        if pos in area:
            return
        
        area.append(pos)
        adjCells = self.FindAllAdjacentCell(pos)
        #Neu 1 o khong o trong khu vuc hien tai thi them vao
        
        for i in adjCells:
        #Tim tat ca cac o xung quanh (1) cua o pos  
            x_i, y_i = i
            if self.field[x_i][y_i].isSafe == True and self.field[x_i][y_i].value != 0:
                newAdjCells = self.FindAllAdjacentCell(i)
                #Tim cac o xung quanh (2) cua o (1)
                
                for j in newAdjCells:
                #Neu pos va o (1) co cung 1 o xung quanh vaf o do chua xac dinh thi pos va o (1) co cung khu vuc  
                    x_j, y_j = j
                    if j != pos and j in adjCells and self.field[x_j][y_j].isSafe != True:
                        self.FindAllAdjacentCellsInArea(i, area)
        
    def SeperateField(self):
    #Ham chia tat ca cac o co du kien thanh cac khu vuc rieng   
        areas = []
        exploredCells = []
        
        for i in self.hintCells:
            
            if i not in exploredCells:
            #Neu o dang xet chua co khu vuc thi tao khu vuc moi va tim tat ca cac o cung khu vuc voi no    
                temp = []
                self.FindAllAdjacentCellsInArea(i, temp) 
                areas.append(temp)
                for j in temp:
                    exploredCells.append(j)
                    
        return areas

    def GetAllClues(self):
    #Ham tim tat ca cac du kien cua tat ca khu vuc       
        areas = self.SeperateField()
        result = []
        
        for eachArea in areas:
        #Xet tung khu vuc    
            clues = []
            count = 0
            cellsAsVariable = dict()
            
            for i in eachArea:                
            #Xet tung o cua khu vuc    
                x_i, y_i = i
                unexploredBomb = self.field[x_i][y_i].value
                adjCells = self.FindAllAdjacentCell(i)
                temp = []
                
                for j in adjCells:
                #Kiem tra cac o xung quanh cua o dang xet    
                    x_j, y_j = j
                    
                    if self.field[x_j][y_j].isSafe == None:
                        temp.append(j)
                        if j not in cellsAsVariable:
                            count += 1
                            cellsAsVariable.update({j : count})
                            
                    elif self.field[x_j][y_j].isSafe == False:
                        unexploredBomb -= 1
                
                if len(clues) == 0:
                    clues.append(Clue(temp, len(temp), unexploredBomb))
                else:
                    flag = True
                    
                    for j in clues:
                    #Kiem tra du kien co bi trung lap hay khong
                        if len(temp) == 0 and unexploredBomb == 0:
                            flag = False
                        else:
                            flag = j.IsDifferentClue(temp, unexploredBomb)
                        
                    if flag:   
                        clues.append(Clue(temp, len(temp), unexploredBomb))
            #clues = PriorityQueue(clues)
            print()
            print(cellsAsVariable)
            result.append((clues, cellsAsVariable))
        
        return result
