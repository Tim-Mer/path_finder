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
        self.create_cells()
        
        self.break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
            
        self.break_walls_r(self.num_cols, self.num_rows)
        
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
        time.sleep(0.01)
        
    def break_entrance_and_exit(self):
        self.cells[0][0].top = False
        self.draw_cell(0,0)
        self.cells[self.num_cols-1][self.num_rows-1].bottom = False
        self.draw_cell(self.num_cols-1, self.num_rows-1)
        
    def break_walls_r(self, i, j):
        pass