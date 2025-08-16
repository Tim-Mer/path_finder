from funcs.graphics import Point, Line, Window

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
        if self.win is None:
            return
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
    
    def midpoint(self):
        return Point(self.x1, self.y1) + ((Point(self.x1, self.y1) - Point(self.x2, self.y2))/2)
            
    def draw_move(self, to_cell: "Cell", undo=False): 
        colour = "red"
        if undo:
            colour = "grey"
        self.win.draw_line(Line(self.midpoint(), to_cell.midpoint()), colour)
        