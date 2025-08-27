from funcs.cell import Cell
from funcs.graphics import Window
import time
import random

class Maze:
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window | None = None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        self.cells = []
        print("Creating Cells")
        self.create_cells()
        
        print("Creating Entrance and Exit")
        self.break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        
        print("Breaking walls...")
        self.break_walls_r(int(self.num_cols/2)-1, int(self.num_rows/2)-1)
        
        print("Ressetting visited status")
        self.reset_cells_visited()
        
    def create_cells(self):
        for i in range(self.num_cols):
            self.cells.append([])
            for j in range(self.num_rows):
                self.cells[i].append(Cell(self.win))
                self.draw_cell(i, j)
        
    def draw_cell(self, i, j):
        x = int(self.cell_size_x * i) + self.x1
        y = int(self.cell_size_y * j) + self.y1
        self.cells[i][j].draw(x, y, x+self.cell_size_x, y+self.cell_size_y)
        self.animate()
        
    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        #time.sleep(0.01)
        
    def break_entrance_and_exit(self):
        self.cells[0][0].directions["top"] = False
        self.draw_cell(0,0)
        self.cells[self.num_cols-1][self.num_rows-1].directions["bottom"] = False
        self.draw_cell(self.num_cols-1, self.num_rows-1)
        
    def break_walls_r(self, i: int, j: int):
        if 0 > i or i > self.num_cols-1 or 0 > j or j > self.num_rows-1:
            return
        # Check if cell is visited
        if self.cells[i][j].visited:
            return
            
        # Visit self
        self.cells[i][j].visited = True
        
        # Possible directions
        options = {"left": (i-1, j),
                   "right": (i+1, j),
                   "bottom": (i, j+1),
                   "top": (i, j-1)}
        
        opposites = {"left": "right",
                     "right": "left",
                     "bottom": "top",
                     "top": "bottom"}
        
        choices = list(options.keys())
        #for l in range(len(list(options.keys()))):
        #    choices.append(random.choice(list(options.keys())))
        
                            
        while len(choices):
            print("----------------------------------------------")
            # Choose direction
            choice = choices.pop(random.randrange(len(choices)))
            print(f"Going: {choice}")
            new_i, new_j = options[choice]

            # Confirm direction is valid
            print(f"i: {new_i}, j: {new_j}")
            if not (0 > new_i or new_i > self.num_cols-1 or 0 > new_j or new_j > self.num_rows-1):
                if self.cells[new_i][new_j].visited == False:
                    # Break walls to new direction
                    self.cells[i][j].directions[choice] = False
                    self.cells[new_i][new_j].directions[opposites[choice]] = False
                    self.draw_cell(i, j)
                    self.draw_cell(new_i, new_j)
                    self.break_walls_r(new_i, new_j)

    def reset_cells_visited(self):
        for i in range(self.num_cols-1):
            for j in range(self.num_rows-1):
                self.cells[i][j].visited = False