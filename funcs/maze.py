from funcs.cell import Cell
from funcs.graphics import Window
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win: Window | None = None, seed=None):
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
        # Check if cell is visited
        if self.cells[i][j].visited:
                print("visited")
                return
            
        # Visit self
        self.cells[i][j].visited = True
        
        # Possible directions
        options = {"left": (i-1, j), "right": (i+1, j), "bottom": (i, j-1), "top": (i, j+1)}
        opposites = {"left": "right", "right": "left", "bottom": "top", "top": "bottom"}
        
        all_visited = False
            
        while not all_visited:
            visitable = 4
            for k in options.keys():
                current_i, current_j = options[k]
                try:
                    if self.cells[current_i][current_j].visited:
                        visitable -= 1
                except:
                    visitable -= 1
            print(f"visitable: {visitable}")
            if visitable < 3:
                all_visited = True
            # Choose direction
            choice = random.choice(list(options.keys()))
            print(f"Going: {choice}")
            new_i, new_j = options[choice]

            # Confirm direction is valid and not visited
            print(f"i: {i}, j: {j}\n")
            if 0 > new_i  or new_i > self.num_rows-1:
                print("EDGE i")
                return
            if 0 > new_j  or new_j > self.num_cols-1:
                print("EDGE j")
                return
        
            # Break walls to new direction
            self.cells[i][j].directions[choice] = False
            self.cells[new_i][new_j].directions[opposites[choice]] = False
            self.draw_cell(i, j)
            self.draw_cell(new_i, new_j)
            time.sleep(0.01)
            self.break_walls_r(new_i, new_j)
