from arrays import Array


class Grid():

    def __init__(self, columns, rows):
        self.rows = rows
        self.columns = columns
        self.grid = list()

        for row in range(self.rows):
            self.grid.append(Array(capacity=columns))
    
    def get_height(self):
        return len(self.grid)
    
    def get_width(self):
        return len(self.grid[0])
    
    def __str__(self):
        result = ""

        for fila in range(self.get_height()):
            for columna in range(self.get_width()):
                print(fila)
                result += str(self.grid[fila][columna]) + " "
            
            result += "\n"
        
        return result
    
    def __add_column__(self, num, value):
        pass
    
    
grid = Grid(columns=4, rows=3)
print(grid)
