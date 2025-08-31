from funcs.graphics import Window
from funcs.maze import Maze

def main():
    width = 704
    height = 704
    win = Window(width, height)
    
    m1 = Maze(32, 32, 20, 20, 32, 32, win)
    print("Solving Maze")
    m1.solve()
    
    win.wait_for_close()
    
    
    
main()
    
