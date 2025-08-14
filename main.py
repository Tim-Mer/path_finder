from funcs.graphics import Window, Line, Point, Cell

def main():
    height = 800
    width = 600
    win = Window(height, width)
    
    c1 = Cell(win)
    c1.draw(200, 200, 220, 220)
    c2 = Cell(win)
    c2.bottom = False
    c2.draw(100, 100, 120, 120)
    c3 = Cell(win)
    c3.left = False
    c3.right = False
    c3.draw(300, 300, 320, 320)
    c4 = Cell(win)
    c4.bottom = False
    c4.top = False
    c4.draw(400, 400, 420, 420)
    c5 = Cell(win)
    c5.right = False
    c5.left = False
    c5.bottom = False
    c5.draw(500, 500, 520, 520)
    win.wait_for_close()
    
    
    
main()
    
