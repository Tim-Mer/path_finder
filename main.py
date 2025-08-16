from funcs.graphics import Window
from funcs.cell import Cell

def main():
    height = 800
    width = 600
    win = Window(height, width)
    
    c1 = Cell(win)
    c1.bottom = False
    c1.draw(200, 200, 220, 220)
    c2 = Cell(win)
    c2.top = False
    c2.draw(200, 250, 220, 270)
    c1.draw_move(c2)
    win.wait_for_close()
    
    
    
main()
    
