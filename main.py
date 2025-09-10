from funcs.graphics import Window
from funcs.maze import Maze
import sys


def main():
    width = 1408
    height = 704
    win = Window(width, height)
    sys.setrecursionlimit(10**6)
    
    m1 = Maze(32, 32, 80, 160, 8, 8, win)
    print("Solving Maze")
    m1.solve()
    
    win.wait_for_close()
    
    
    
main()
    
