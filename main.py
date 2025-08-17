from funcs.graphics import Window
from funcs.maze import Maze

def main():
    width = 704
    height = 704
    win = Window(width, height)
    
    Maze(32, 32, 20, 20, 32, 32, win, 23)
    win.wait_for_close()
    
    
    
main()
    
