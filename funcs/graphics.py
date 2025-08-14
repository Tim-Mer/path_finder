from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __add__(self, value):
        if type(value) == int:
            value = Point(value, value)
        return Point(self.x + value.x, self.y + value.y)
    
    def __subtract__(self, value):
        if type(value) == int:
            value = Point(value, value)
        return Point(self.x - value.x, self.y - value.y)
    
    def __truediv__(self, value):
        return Point(int(self.x/value), int(self.y/value))

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas: Canvas, fill_colour: str):
        x1 = self.p1.x
        x2 = self.p2.x
        y1 = self.p1.y
        y2 = self.p2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_colour, width=2)

class Window:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Path Finder")
        self.can = Canvas(self.root, bg="white", height=height, width=width)
        self.can.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
        
    def wait_for_close(self):
        self.running = True
        while(self.running):
            self.redraw()
        print("Window closed...")
        
    def close(self):
        self.running = False
    
    def draw_line(self, line: Line, fill_colour: str = "black"):
        line.draw(self.can, fill_colour)

class Cell:
    def __init__(self, win: Window):
        self.left = True
        self.right = True
        self.top = True
        self.bottom = True
        self.x1 = -1
        self.y1 = -1
        self.x2 = -1
        self.y2 = -1
        self.win = win
        
    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)
        if self.left:
            self.win.draw_line(Line(top_left, bottom_left))
        if self.right:
            self.win.draw_line(Line(top_right, bottom_right))
        if self.top:
            self.win.draw_line(Line(top_left, top_right))
        if self.bottom:
            self.win.draw_line(Line(bottom_left, bottom_right))
    
    def midpoint(self, other):
        return self + (self - other)/2
            
    def draw_move(self, to_cell, undo=False):
        colour = "red"
        if undo:
            colour = "grey"
        
        